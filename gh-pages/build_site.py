#!/usr/bin/env python3
# RogueForge static-site builder. Adapted from the rappture-monorepo
# gh-pages builder (same template/site.json/docs convention).
#
# Reads:
#   gh-pages/site.json    - site metadata + group definitions
#   gh-pages/templates/   - home.html, group.html, doc.html
#   gh-pages/assets/      - site.css, *.jpg, ...
#   docs/<group>/*.md     - markdown content (one file per page)
#   docs/README.md        - rendered into homepage "About this archive"
#
# Writes (clobbering on each run):
#   gh-pages/public/      - built static site, suitable for GitHub Pages
#     index.html
#     <group>/index.html
#     <group>/<page>/index.html
#     assets/...
#     .nojekyll
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


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "gh-pages"
DOCS_SRC = ROOT / "docs"
OUTPUT_DIR = ROOT / "gh-pages" / "public"


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
    return slug or "section"


def render_template(path: Path, context: dict) -> str:
    text = path.read_text(encoding="utf-8")
    for key, value in context.items():
        text = text.replace(f"{{{{ {key} }}}}", value)
    return text


def relative_href(from_file: Path, to_file: Path) -> str:
    return os.path.relpath(to_file, from_file.parent).replace(os.sep, "/")


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_tree(source: Path, destination: Path) -> None:
    if source.exists():
        shutil.copytree(source, destination, dirs_exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


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
                if index + 1 >= len(tokens):
                    continue
                inline = tokens[index + 1]
                if inline.type != "inline":
                    continue
                heading_text = inline.content.strip()
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
                elif level in (2, 3, 4):
                    toc.append({"level": level, "anchor": anchor,
                                "text": heading_text})
            elif token.type == "inline" and link_rewrite is not None:
                if token.children:
                    for child in token.children:
                        if child.type == "link_open":
                            href = child.attrGet("href") or ""
                            new = link_rewrite(href)
                            if new != href:
                                child.attrSet("href", new)

        if first_h1_index is not None:
            del tokens[first_h1_index:first_h1_index + 3]

        html = self.md.renderer.render(tokens, self.md.options, {})
        return {"title": title, "toc": toc, "html": html}


def discover_pages(docs_src: Path, groups: list) -> dict:
    by_group: dict = {}
    group_slugs = {g["slug"] for g in groups}
    for group in groups:
        gdir = docs_src / group["slug"]
        if not gdir.is_dir():
            by_group[group["slug"]] = []
            continue
        found = {md_path.stem: md_path for md_path in gdir.glob("*.md")}
        order_hint = group.get("order", [])
        if not order_hint and group.get("families"):
            order_hint = [s for fam in group["families"] for s in fam.get("slugs", [])]
        ordered_slugs = []
        for slug in order_hint:
            if slug in found:
                ordered_slugs.append(slug)
            else:
                print(f"warning: site.json lists docs/{group['slug']}/{slug}.md but file is missing",
                      file=sys.stderr)
        leftover = sorted(s for s in found if s not in set(order_hint))
        if order_hint and leftover:
            print(f"warning: docs/{group['slug']}/ contains pages not in site.json order: {leftover}",
                  file=sys.stderr)
        ordered_slugs.extend(leftover)
        pages = [{
            "slug": slug,
            "source": found[slug],
            "output_path": Path(group["slug"]) / slug / "index.html",
        } for slug in ordered_slugs]
        by_group[group["slug"]] = pages
    for child in docs_src.iterdir():
        if child.is_dir() and child.name not in group_slugs and not child.name.startswith("."):
            print(f"warning: docs/{child.name}/ is not a known group", file=sys.stderr)
    return by_group


def make_link_rewriter(current_group: str, current_slug: str):
    def rewrite(href: str) -> str:
        if not href or href.startswith(("http://", "https://", "#", "mailto:")):
            return href
        anchor = ""
        path = href
        if "#" in path:
            path, anchor = path.split("#", 1)
            anchor = "#" + anchor
        if not path.endswith(".md"):
            return href
        if path.startswith("../"):
            parts = path[3:].split("/")
            if len(parts) >= 2 and parts[-1].endswith(".md"):
                tgt_group = parts[0]
                tgt_slug = parts[-1][:-3]
            else:
                return href
        else:
            tgt_group = current_group
            tgt_slug = path[:-3] if path.endswith(".md") else path
        if tgt_group == current_group:
            return f"../{tgt_slug}/{anchor}"
        else:
            return f"../../{tgt_group}/{tgt_slug}/{anchor}"
    return rewrite


def build_nav(groups, pages_by_group, page_titles, current_output,
              output_dir, github_href, current_group=None, current_slug=None) -> str:
    """Full sidebar nav shared by the home page and every doc page.

    Mirrors rogue.rogueforge.net: every section is always fully expanded
    (the games group split into its family sub-lists), the current page —
    if any — gets an is-active highlight, and a trailing "Development"
    group links out to the GitHub org.

    A group may declare a "links" array in site.json for non-page entries
    (e.g. About's "Home" link to the site root). Each link is either
    {"label", "to": <path under output root>} or {"label", "url": <abs>}.
    """
    def item(href, label, active=False):
        cls = "nav__item is-active" if active else "nav__item"
        return (f'    <li><a class="{cls}" href="{escape(href)}">'
                f'{escape(label)}</a></li>')

    def page_item(page, g_slug):
        href = relative_href(current_output, output_dir / page["output_path"])
        active = (g_slug == current_group and page["slug"] == current_slug)
        title = page_titles.get((g_slug, page["slug"]), page["slug"])
        return item(href, title, active)

    chunks = []
    for group in groups:
        g_slug = group["slug"]
        body_parts = []

        link_items = []
        for link in group.get("links", []):
            if "url" in link:
                link_items.append(item(link["url"], link["label"]))
            else:
                target = output_dir / (link.get("to") or "index.html")
                href = relative_href(current_output, target)
                active = (current_group is None
                          and target.resolve() == current_output.resolve())
                link_items.append(item(href, link["label"], active))
        if link_items:
            body_parts.append('  <ul class="nav__list">\n'
                              + "\n".join(link_items) + "\n  </ul>")

        if group.get("families"):
            page_index = {p["slug"]: p for p in pages_by_group.get(g_slug, [])}
            for fam in group["families"]:
                fam_items = [page_item(page_index[s], g_slug)
                             for s in fam.get("slugs", []) if s in page_index]
                if not fam_items:
                    continue
                body_parts.append(
                    '  <div class="nav__family">\n'
                    f'    <p class="nav__family-label">{escape(fam["label"])}</p>\n'
                    '    <ul class="nav__list">\n'
                    + "\n".join(fam_items)
                    + "\n    </ul>\n"
                    '  </div>'
                )
        else:
            items = [page_item(p, g_slug) for p in pages_by_group.get(g_slug, [])]
            if items:
                body_parts.append('  <ul class="nav__list">\n'
                                  + "\n".join(items) + "\n  </ul>")

        group_index = output_dir / g_slug / "index.html"
        heading_href = relative_href(current_output, group_index)
        chunks.append(
            '<div class="nav__group">\n'
            f'  <a class="nav__heading" href="{escape(heading_href)}">'
            f'{escape(group["title"])}</a>\n'
            + "\n".join(body_parts)
            + '\n</div>'
        )

    chunks.append(
        '<div class="nav__group">\n'
        '  <span class="nav__heading nav__heading--static">Development</span>\n'
        '  <ul class="nav__list">\n'
        f'    <li><a class="nav__item" href="{escape(github_href)}">'
        f'github.com/rogueforge</a></li>\n'
        '  </ul>\n'
        '</div>'
    )
    return "\n".join(chunks)


def build_breadcrumb(crumbs: list) -> str:
    """crumbs: list of (label, href-or-None). The last is rendered as the
    current page (bold, no link)."""
    parts = []
    for i, (label, href) in enumerate(crumbs):
        last = (i == len(crumbs) - 1)
        if last or href is None:
            parts.append(f"<strong>{escape(label)}</strong>")
        else:
            parts.append(f'<a href="{escape(href)}">{escape(label)}</a>')
    return "You are here: " + " &raquo; ".join(parts)


def build_toc(entries: list) -> str:
    if not entries:
        return ""
    items = []
    for entry in entries:
        level = int(entry["level"])
        classes = f"toc__item toc__item--level-{level}"
        items.append(
            f'<li class="{classes}"><a href="#{escape(str(entry["anchor"]))}">'
            f"{escape(str(entry['text']))}</a></li>"
        )
    return (
        '<nav class="toc" aria-label="On this page">\n'
        '  <p class="toc__heading">On this page</p>\n'
        '  <ul class="toc__list">\n'
        + "\n".join(items)
        + "\n  </ul>\n"
        "</nav>"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the RogueForge site.")
    parser.add_argument("--output", default=str(OUTPUT_DIR), help="Output directory")
    args = parser.parse_args()
    output_dir = Path(args.output).resolve()

    config = json.loads((SOURCE_DIR / "site.json").read_text(encoding="utf-8"))
    site_name = config["site_name"]
    site_tagline = config["site_tagline"]
    site_description = config["site_description"]
    github_href = config.get("github_href", "#")
    groups = config["groups"]

    pages_by_group = discover_pages(DOCS_SRC, groups)
    renderer = MarkdownRenderer()
    page_titles: dict = {}
    rendered_pages: dict = {}

    for group in groups:
        for page in pages_by_group.get(group["slug"], []):
            rewriter = make_link_rewriter(group["slug"], page["slug"])
            md_text = page["source"].read_text(encoding="utf-8")
            rendered = renderer.render(md_text, link_rewrite=rewriter)
            title = rendered["title"] or page["slug"].replace("_", " ").replace("-", " ").title()
            page_titles[(group["slug"], page["slug"])] = str(title)
            rendered_pages[(group["slug"], page["slug"])] = rendered

    readme_path = DOCS_SRC / "README.md"
    if readme_path.exists():
        def readme_rewrite(href: str) -> str:
            if not href or href.startswith(("http://", "https://", "#", "mailto:")):
                return href
            anchor = ""
            path = href
            if "#" in path:
                path, anchor = path.split("#", 1)
                anchor = "#" + anchor
            m = re.match(r"^([^/]+)/([^/]+)\.md$", path)
            if m:
                return f"{m.group(1)}/{m.group(2)}/{anchor}"
            m = re.match(r"^([^/]+)/$", path)
            if m:
                return f"{m.group(1)}/{anchor}"
            return href
        readme_text = readme_path.read_text(encoding="utf-8")
        readme_rendered = renderer.render(readme_text, link_rewrite=readme_rewrite)
        readme_html = ('<div class="prose">\n'
                       + str(readme_rendered["html"])
                       + '\n</div>')
    else:
        readme_html = ""

    ensure_clean_dir(output_dir)
    copy_tree(SOURCE_DIR / "assets", output_dir / "assets")
    write_text(output_dir / ".nojekyll", "")

    home_output = output_dir / "index.html"
    home_nav_html = build_nav(
        groups, pages_by_group, page_titles,
        home_output, output_dir, github_href,
    )
    home_html = render_template(
        SOURCE_DIR / "templates" / "home.html",
        {
            "site_name": escape(site_name),
            "site_tagline": escape(site_tagline),
            "site_description": escape(site_description),
            "github_href": escape(github_href),
            "assets_href": "assets/site.css",
            "logo_href": "assets/rogue-icon.png",
            "home_href": ".",
            "breadcrumb": build_breadcrumb([("Home", None)]),
            "nav": home_nav_html,
            "readme_html": readme_html,
        },
    )
    write_text(home_output, home_html)

    for group in groups:
        g_slug = group["slug"]
        group_output = output_dir / g_slug / "index.html"
        page_items = []
        for page in pages_by_group.get(g_slug, []):
            ppath = output_dir / page["output_path"]
            href = relative_href(group_output, ppath)
            title = page_titles[(g_slug, page["slug"])]
            page_items.append(
                '<li>\n'
                '  <a href="{href}">\n'
                '    <span class="group-pages__title">{title}</span>\n'
                '    <span class="group-pages__slug">{slug}</span>\n'
                '  </a>\n'
                '</li>'.format(
                    href=escape(href), title=escape(title),
                    slug=escape(page["slug"]),
                )
            )
        nav_html = build_nav(
            groups, pages_by_group, page_titles,
            group_output, output_dir, github_href,
            current_group=g_slug,
        )
        home_href = relative_href(group_output, output_dir / "index.html")
        breadcrumb = build_breadcrumb([
            ("Home", home_href),
            (group["title"], None),
        ])
        group_html = render_template(
            SOURCE_DIR / "templates" / "group.html",
            {
                "site_name": escape(site_name),
                "group_title": escape(group["title"]),
                "group_summary": escape(group["summary"]),
                "github_href": escape(github_href),
                "assets_href": relative_href(group_output, output_dir / "assets" / "site.css"),
                "logo_href": relative_href(group_output, output_dir / "assets" / "rogue-icon.png"),
                "home_href": home_href,
                "breadcrumb": breadcrumb,
                "nav": nav_html,
                "page_count": str(len(pages_by_group.get(g_slug, []))),
                "page_list": "\n".join(page_items),
            },
        )
        write_text(group_output, group_html)

    for group in groups:
        g_slug = group["slug"]
        for page in pages_by_group.get(g_slug, []):
            page_output = output_dir / page["output_path"]
            rendered = rendered_pages[(g_slug, page["slug"])]
            title = page_titles[(g_slug, page["slug"])]
            nav_html = build_nav(
                groups, pages_by_group, page_titles,
                page_output, output_dir, github_href,
                current_group=g_slug, current_slug=page["slug"],
            )
            toc_html = build_toc(rendered["toc"])
            assets_href = relative_href(page_output, output_dir / "assets" / "site.css")
            logo_href = relative_href(page_output, output_dir / "assets" / "rogue-icon.png")
            home_href = relative_href(page_output, output_dir / "index.html")
            group_href = relative_href(page_output, output_dir / g_slug / "index.html")
            breadcrumb = build_breadcrumb([
                ("Home", home_href),
                (group["title"], group_href),
                (title, None),
            ])
            source_path = f"docs/{g_slug}/{page['slug']}.md"
            doc_html = render_template(
                SOURCE_DIR / "templates" / "doc.html",
                {
                    "site_name": escape(site_name),
                    "page_title": escape(title),
                    "page_summary": escape(group["summary"]),
                    "group_title": escape(group["title"]),
                    "group_href": escape(group_href),
                    "github_href": escape(github_href),
                    "assets_href": escape(assets_href),
                    "logo_href": escape(logo_href),
                    "home_href": escape(home_href),
                    "breadcrumb": breadcrumb,
                    "source_path": escape(source_path),
                    "nav": nav_html,
                    "toc": toc_html,
                    "content": str(rendered["html"]),
                },
            )
            write_text(page_output, doc_html)

    total_pages = sum(len(p) for p in pages_by_group.values())
    print(f"Built {total_pages} pages across {len(groups)} groups -> {output_dir}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
