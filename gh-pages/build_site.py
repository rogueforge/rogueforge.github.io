#!/usr/bin/env python3
# RogueForge static-site builder.
#
# Reads:
#   gh-pages/site.json    - site metadata, groups, and the dungeon map spec
#   gh-pages/templates/   - layout.html + home/group/doc bodies
#   gh-pages/assets/      - site.css, fonts, logo images
#   docs/<group>/*.md     - markdown content (one file per page), each with
#                           optional "---" front matter of key: value lines
#   docs/README.md        - rendered into the home page's story section
#
# Writes (clobbering on each run):
#   gh-pages/public/      - the built static site, for GitHub Pages
#
# Requires markdown-it-py. Debian: `apt install python3-markdown-it` or
# `pip install markdown-it-py`.

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import unicodedata
from html import escape
from pathlib import Path

try:
    from markdown_it import MarkdownIt
except ImportError as exc:
    raise SystemExit(
        "markdown-it-py not found. Install with: apt install python3-markdown-it"
    ) from exc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dungeon import render_map  # noqa: E402


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "gh-pages"
TEMPLATES = SOURCE_DIR / "templates"
DOCS_SRC = ROOT / "docs"
OUTPUT_DIR = ROOT / "gh-pages" / "public"

STATUS_LABELS = {
    "rebuilt": "Rebuilt from the binary",
    "partial": "Rebuild in progress",
    "port": "Restored from author source",
    "soon": "Coming soon",
    "planned": "Not yet restored",
}


# ---------------------------------------------------------------- helpers

def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
    return slug or "section"


def render_template(name: str, context: dict) -> str:
    text = (TEMPLATES / name).read_text(encoding="utf-8")
    # One pass, so substituted values are never themselves re-expanded.
    return re.sub(r"\{\{ (\w+) \}\}",
                  lambda m: context.get(m.group(1), m.group(0)), text)


def relative_href(from_file: Path, to_file: Path) -> str:
    href = os.path.relpath(to_file, from_file.parent).replace(os.sep, "/")
    if href.endswith("index.html"):
        href = href[: -len("index.html")] or "./"
    return href


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_front_matter(text: str) -> tuple:
    """Split '---' key: value front matter from a markdown file."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta, text[end + 5:]


# --------------------------------------------------------------- markdown

class MarkdownRenderer:
    def __init__(self) -> None:
        self.md = MarkdownIt("commonmark", {"html": True, "typographer": True})
        self.md.enable("table")
        self.md.enable("strikethrough")

    def render(self, text: str, *, link_rewrite=None) -> dict:
        tokens = self.md.parse(text)
        slug_counts: dict = {}
        toc: list = []
        title = None
        first_h1_index = None

        for index, token in enumerate(tokens):
            if token.type == "heading_open":
                level = int(token.tag[1])
                inline = tokens[index + 1] if index + 1 < len(tokens) else None
                if inline is None or inline.type != "inline":
                    continue
                heading_text = "".join(
                    c.content for c in (inline.children or [])
                    if c.type in ("text", "code_inline")).strip()
                if not heading_text:
                    continue
                base_slug = slugify(heading_text)
                count = slug_counts.get(base_slug, 0)
                slug_counts[base_slug] = count + 1
                anchor = base_slug if count == 0 else f"{base_slug}-{count + 1}"
                token.attrSet("id", anchor)
                if level == 1 and title is None:
                    title = heading_text
                    first_h1_index = index
                elif level == 2:
                    toc.append({"anchor": anchor, "text": heading_text})
            elif token.type == "inline" and link_rewrite is not None:
                for child in token.children or []:
                    if child.type == "link_open":
                        href = child.attrGet("href") or ""
                        new = link_rewrite(href)
                        if new != href:
                            child.attrSet("href", new)

        if first_h1_index is not None:
            del tokens[first_h1_index:first_h1_index + 3]

        html = self.md.renderer.render(tokens, self.md.options, {})
        return {"title": title, "toc": toc, "html": html}


def make_link_rewriter(current_group: str | None):
    """Rewrite relative links to .md sources into pretty URLs.

    current_group is None for docs/README.md (rendered at the site root).
    """
    def rewrite(href: str) -> str:
        if not href or href.startswith(("http://", "https://", "#", "mailto:")):
            return href
        path, _, anchor = href.partition("#")
        anchor = "#" + anchor if anchor else ""
        if not path.endswith(".md"):
            return href
        parts = path[:-3].split("/")
        if current_group is None:
            return "/".join(parts) + "/" + anchor
        if parts[0] == "..":
            if len(parts) == 3:
                return f"../../{parts[1]}/{parts[2]}/{anchor}"
            return href
        return f"../{parts[-1]}/{anchor}"
    return rewrite


# ------------------------------------------------------------------- pages

def discover_pages(groups: list) -> dict:
    by_group: dict = {}
    group_slugs = {g["slug"] for g in groups}
    for group in groups:
        gdir = DOCS_SRC / group["slug"]
        found = ({p.stem: p for p in gdir.glob("*.md")} if gdir.is_dir() else {})
        order = list(group.get("order", []))
        if not order and group.get("families"):
            order = [s for fam in group["families"] for s in fam["slugs"]]
        for slug in order:
            if slug not in found:
                print(f"warning: site.json lists docs/{group['slug']}/{slug}.md "
                      "but the file is missing", file=sys.stderr)
        leftover = sorted(s for s in found if s not in order)
        if order and leftover:
            print(f"warning: docs/{group['slug']}/ has pages not listed in "
                  f"site.json: {leftover}", file=sys.stderr)
        by_group[group["slug"]] = [
            {"slug": s, "group": group["slug"], "source": found[s],
             "output_path": Path(group["slug"]) / s / "index.html"}
            for s in [s for s in order if s in found] + leftover
        ]
    for child in DOCS_SRC.iterdir():
        if child.is_dir() and child.name not in group_slugs:
            print(f"warning: docs/{child.name}/ is not a known group",
                  file=sys.stderr)
    return by_group


# -------------------------------------------------------------- fragments

def build_topnav(groups, current_output, output_dir, github_href,
                 current_group=None) -> str:
    items = []
    for group in groups:
        if group.get("hidden_from_nav"):
            continue
        href = relative_href(current_output, output_dir / group["slug"] / "index.html")
        current = ' aria-current="page"' if group["slug"] == current_group else ""
        items.append(f'<li><a href="{escape(href)}"{current}>'
                     f'{escape(group.get("nav_label", group["title"]))}</a></li>')
    items.append(f'<li><a href="{escape(github_href)}">GitHub</a></li>')
    return "\n".join(items)


def status_badge(status: str) -> str:
    if not status:
        return ""
    label = STATUS_LABELS.get(status, status)
    return f'<span class="status status--{escape(status)}">{escape(label)}</span>'


def build_version_index(group, pages, meta_by_page, titles, current_output,
                        output_dir) -> str:
    """The table of every version, split by family."""
    page_index = {p["slug"]: p for p in pages}
    sections = []
    for fam in group.get("families", []):
        rows = []
        for slug in fam["slugs"]:
            if slug not in page_index:
                continue
            page = page_index[slug]
            meta = meta_by_page[(group["slug"], slug)]
            href = relative_href(current_output, output_dir / page["output_path"])
            rows.append(
                "<tr>"
                f'<th scope="row"><a href="{escape(href)}">'
                f'{escape(meta.get("short", titles[(group["slug"], slug)]))}</a></th>'
                f'<td class="v-year">{escape(meta.get("year", ""))}</td>'
                f'<td class="v-machine">{escape(meta.get("machine", ""))}</td>'
                f'<td class="v-status">{status_badge(meta.get("status", ""))}</td>'
                "</tr>")
        if not rows:
            continue
        blurb = (f'<p class="family__blurb">{escape(fam["blurb"])}</p>'
                 if fam.get("blurb") else "")
        sections.append(
            '<section class="family">\n'
            f'<h3 class="family__name">{escape(fam["label"])}</h3>\n{blurb}\n'
            '<table class="versions">\n'
            '<thead><tr><th scope="col">Version</th><th scope="col">Year</th>'
            '<th scope="col">Machine</th><th scope="col">Status</th></tr></thead>\n'
            "<tbody>\n" + "\n".join(rows) + "\n</tbody>\n</table>\n</section>")
    return "\n".join(sections)


def build_page_list(pages, titles, meta_by_page, current_output, output_dir) -> str:
    items = []
    for page in pages:
        meta = meta_by_page[(page["group"], page["slug"])]
        href = relative_href(current_output, output_dir / page["output_path"])
        dek = (f'<p>{escape(meta["summary"])}</p>' if meta.get("summary") else "")
        img = glyph_img(meta, current_output, output_dir, "page-list__glyph")
        items.append(f'<li>{img}<div><a href="{escape(href)}">'
                     f'{escape(titles[(page["group"], page["slug"])])}</a>{dek}</div></li>')
    return '<ol class="page-list">\n' + "\n".join(items) + "\n</ol>"


FACT_KEYS = [
    ("released", "Released"),
    ("machine", "Machine"),
    ("origin", "Recovered from"),
    ("toolchain", "Rebuilt with"),
    ("verified", "Verified"),
]


def build_facts(meta: dict) -> str:
    rows = [f"<div><dt>{label}</dt><dd>{escape(meta[key]).replace('/', '/<wbr>')}</dd></div>"
            for key, label in FACT_KEYS if meta.get(key)]
    if meta.get("repo"):
        repos = []
        for repo in meta["repo"].split(","):
            repo = repo.strip()
            repos.append(f'<a href="https://github.com/rogueforge/{escape(repo)}">'
                         f'{escape(repo)}</a>')
        label = "Repositories" if len(repos) > 1 else "Repository"
        rows.append(f"<div><dt>{label}</dt><dd>{'<br>'.join(repos)}</dd></div>")
    if not rows and not meta.get("status"):
        return ""
    return ('<div class="facts">\n' + status_badge(meta.get("status", ""))
            + '\n<dl>\n' + "\n".join(rows) + "\n</dl>\n</div>")


def glyph_img(meta: dict, current_output: Path, output_dir: Path, cls: str) -> str:
    """A voxel glyph picture named by the page's "glyph" front matter."""
    if not meta.get("glyph"):
        return ""
    src = relative_href(current_output, output_dir / "assets" / "img" / f"{meta['glyph']}.webp")
    return (f'<img class="{cls}" src="{escape(src)}" alt="" width="160" height="160" '
            'loading="lazy" decoding="async">')


def build_toc(entries: list) -> str:
    if len(entries) < 2:
        return ""
    items = "\n".join(f'<li><a href="#{escape(e["anchor"])}">{escape(e["text"])}</a></li>'
                      for e in entries)
    return ('<nav class="toc" aria-label="On this page">\n'
            '<p class="toc__heading">On this page</p>\n'
            f'<ol>\n{items}\n</ol>\n</nav>')


def build_pager(pages, index, titles, current_output, output_dir) -> str:
    links = []
    for rel, cls, word in ((-1, "pager__prev", "Back up the stairs"),
                           (1, "pager__next", "Down the stairs")):
        j = index + rel
        if 0 <= j < len(pages):
            p = pages[j]
            href = relative_href(current_output, output_dir / p["output_path"])
            links.append(f'<a class="{cls}" href="{escape(href)}"><span>{word}</span>'
                         f'{escape(titles[(p["group"], p["slug"])])}</a>')
    if not links:
        return ""
    return '<nav class="pager" aria-label="More in this section">' + "".join(links) + "</nav>"


# -------------------------------------------------------------------- main

def main() -> int:
    parser = argparse.ArgumentParser(description="Build the RogueForge site.")
    parser.add_argument("--output", default=str(OUTPUT_DIR), help="Output directory")
    args = parser.parse_args()
    output_dir = Path(args.output).resolve()

    config = json.loads((SOURCE_DIR / "site.json").read_text(encoding="utf-8"))
    site_name = config["site_name"]
    github_href = config.get("github_href", "#")
    groups = config["groups"]
    group_by_slug = {g["slug"]: g for g in groups}

    pages_by_group = discover_pages(groups)
    renderer = MarkdownRenderer()
    titles: dict = {}
    metas: dict = {}
    rendered: dict = {}

    for group in groups:
        for page in pages_by_group[group["slug"]]:
            key = (group["slug"], page["slug"])
            meta, body = parse_front_matter(page["source"].read_text(encoding="utf-8"))
            out = renderer.render(body, link_rewrite=make_link_rewriter(group["slug"]))
            titles[key] = meta.get("title") or out["title"] or page["slug"].replace("-", " ").title()
            metas[key] = meta
            rendered[key] = out

    ensure_clean_dir(output_dir)
    shutil.copytree(SOURCE_DIR / "assets", output_dir / "assets", dirs_exist_ok=True)
    write_text(output_dir / ".nojekyll", "")

    import hashlib
    css_version = hashlib.sha1((SOURCE_DIR / "assets" / "site.css").read_bytes()).hexdigest()[:10]

    def page_shell(current_output, *, title, description, main_html,
                   body_class, current_group=None):
        return render_template("layout.html", {
            "title": escape(title),
            "description": escape(description),
            "css_href": relative_href(current_output, output_dir / "assets" / "site.css")
                        + "?v=" + css_version,
            "logo_href": relative_href(current_output, output_dir / "assets" / "rogue-icon.png"),
            "home_href": relative_href(current_output, output_dir / "index.html"),
            "site_name": escape(site_name),
            "topnav": build_topnav(groups, current_output, output_dir,
                                   github_href, current_group),
            "github_href": escape(github_href),
            "discussions_href": escape(config.get("discussions_href", "#")),
            "legacy_href": escape(config.get("legacy_href", "")),
            "body_class": body_class,
            "main": main_html,
        })

    # ---- home
    home_output = output_dir / "index.html"
    readme_meta, readme_md = parse_front_matter(
        (DOCS_SRC / "README.md").read_text(encoding="utf-8"))
    readme = renderer.render(readme_md, link_rewrite=make_link_rewriter(None))

    games = group_by_slug["games"]
    game_metas = [metas[("games", p["slug"])] for p in pages_by_group["games"]]
    stats = {
        "versions": str(len(game_metas)),
        "rebuilt": str(sum(m.get("status") == "rebuilt" for m in game_metas)),
        "ported": str(sum(m.get("status") == "port" for m in game_metas)),
        "redux": str(sum(1 for r in config["map"]["wide"]["rooms"] if r.get("lit"))),
    }

    def page_href(target: str) -> str:
        g, s = target.split("/")
        return relative_href(home_output, output_dir / g / s / "index.html")

    map_html = render_map(config["map"], page_href, stats)
    home_main = render_template("home.html", {
        "headline": escape(config["headline"]),
        "headline_note": escape(config.get("headline_note", "")),
        "lede": config["lede"],
        "map": map_html,
        "map_caption": config["map"]["caption"],
        "story_html": readme["html"],
        "versions_heading": escape(games["title"]),
        "versions_summary": escape(games["summary"]),
        "version_index": build_version_index(
            games, pages_by_group["games"], metas, titles, home_output, output_dir),
    })
    write_text(home_output, page_shell(
        home_output, title=f"{site_name}: {config['site_tagline']}",
        description=config["site_description"], main_html=home_main,
        body_class="page-home"))

    # ---- group index pages
    for group in groups:
        g_slug = group["slug"]
        group_output = output_dir / g_slug / "index.html"
        if group.get("single"):
            continue
        if group.get("families"):
            listing = build_version_index(group, pages_by_group[g_slug], metas,
                                          titles, group_output, output_dir)
        else:
            listing = build_page_list(pages_by_group[g_slug], titles, metas,
                                      group_output, output_dir)
        main_html = render_template("group.html", {
            "group_title": escape(group.get("heading", group["title"])),
            "group_sticker": (f'<span class="redux"><span class="visually-hidden">, </span>'
                              f'{escape(group["sticker"])}</span>'
                              if group.get("sticker") and not group.get("sticker_lead") else ""),
            "group_sticker_lead": (f'<span class="redux redux--lead">{escape(group["sticker"])}'
                                   f'<span class="visually-hidden"> </span></span>'
                                   if group.get("sticker_lead") else ""),
            "group_summary": escape(group["summary"]),
            "group_dek": (f'<div class="page-head__intro prose">\n'
                          f'{renderer.render(group["intro_md"])["html"]}</div>'
                          if group.get("intro_md") else
                          f'<p class="page-head__dek">{escape(group["summary"])}</p>'),
            "listing": listing,
        })
        write_text(group_output, page_shell(
            group_output, title=f"{group['title']}: {group.get('heading', group['title'])} | {site_name}"
            if group.get("heading") else f"{group['title']} | {site_name}",
            description=group["summary"], main_html=main_html,
            body_class=f"page-group page-group--{g_slug}", current_group=g_slug))

    # ---- content pages
    for group in groups:
        g_slug = group["slug"]
        pages = pages_by_group[g_slug]
        for i, page in enumerate(pages):
            key = (g_slug, page["slug"])
            page_output = output_dir / page["output_path"]
            if group.get("single"):
                page_output = output_dir / g_slug / "index.html"
            meta = metas[key]
            dek = (f'<p class="page-head__dek">{escape(meta["summary"])}</p>'
                   if meta.get("summary") and meta.get("hide_summary") != "true"
                   and g_slug != "games" else "")
            main_html = render_template("doc.html", {
                "group_href": ("../" if group.get("single") else
                               relative_href(page_output, output_dir / g_slug / "index.html")),
                "group_title": ("Home" if group.get("single") else escape(group["title"])),
                "page_title": escape(titles[key]),
                "dek": dek,
                "glyph": glyph_img(meta, page_output, output_dir, "page-head__glyph"),
                "facts": build_facts(meta),
                "toc": build_toc(rendered[key]["toc"]),
                "content": rendered[key]["html"],
                "pager": build_pager(pages, i, titles, page_output, output_dir),
            })
            write_text(page_output, page_shell(
                page_output, title=f"{titles[key]} | {site_name}",
                description=meta.get("summary", group["summary"]),
                main_html=main_html,
                body_class=f"page-doc page-doc--{g_slug}", current_group=g_slug))

    # ---- 404
    notfound = output_dir / "404.html"
    write_text(notfound, page_shell(
        notfound, title=f"Not found | {site_name}",
        description=config["site_description"],
        main_html=render_template("404.html", {}), body_class="page-404")
        .replace('href="', 'href="/').replace('href="/http', 'href="http')
        .replace('src="', 'src="/'))

    total = sum(len(p) for p in pages_by_group.values())
    print(f"Built {total} pages across {len(groups)} groups -> {output_dir}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
