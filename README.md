# rogueforge.github.io

Source for the **RogueForge** umbrella project site — the GitHub Pages
replacement for [rogueforge.net](http://www.rogueforge.net).

The published site lives at <https://rogueforge.net/> (also reachable as
<https://rogueforge.github.io/>, the organization's root Pages site).

## Layout

```
.
├── docs/                       Markdown sources, one file per page.
│   ├── README.md               The home page's story section.
│   ├── story/*.md              The restart: how versions are rebuilt.
│   ├── games/*.md              One page per version.
│   ├── docs/*.md               Guides.
│   └── history/*.md            Timeline, family tree, sources.
└── gh-pages/
    ├── site.json               Site metadata, sections, and the dungeon map.
    ├── templates/              layout.html wraps home/group/doc/404.html.
    ├── assets/                 site.css, fonts, logo images.
    ├── build_site.py           The static-site builder.
    ├── dungeon.py              Draws the home page's dungeon map.
    └── public/                 Built output (gitignored; CI publishes this).
```

## Build locally

Requires Python 3.7+ and `markdown-it-py`:

```bash
# Debian/Ubuntu:
apt install python3-markdown-it

# or:
pip install --user markdown-it-py
```

Then:

```bash
python3 gh-pages/build_site.py
```

The site renders into `gh-pages/public/`. Open
`gh-pages/public/index.html` in a browser, or:

```bash
cd gh-pages/public && python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy

CI is configured to build the site on every push to `main` and publish it
to GitHub Pages. See `.github/workflows/pages.yml`. To enable it:

1. **Settings → Pages → Source:** GitHub Actions.
2. Push to `main`. The workflow will build with `build_site.py` and
   publish `gh-pages/public/`.

## Adding a page

1. Drop a new markdown file under `docs/<section>/your-slug.md`, and add
   the slug to that section's `order` (or a family's `slugs`) in
   `gh-pages/site.json`. The filename becomes the URL: `/<section>/your-slug/`.
2. The first H1 becomes the page title. Each `##` heading is listed in
   the page's "On this page" box.
3. Optional front matter sets the page's summary and, for versions, the
   facts box and the row in the version table:

   ```
   ---
   short: Rogue 3.4          # name in the version table
   year: 1981
   machine: PDP-11
   status: rebuilt           # rebuilt | partial | port | planned
   summary: One sentence, shown under the title and in listings.
   released: ...
   origin: ...               # where the binary was recovered from
   toolchain: ...
   verified: ...
   repo: name, other-name    # repositories under github.com/rogueforge
   ---
   ```

4. Cross-page links: use relative markdown links (`../story/method.md`
   or `rogue-3-6.md`). The builder rewrites them to pretty URLs.

## The dungeon map

The home page map is drawn from `map` in `site.json`: rooms (position,
size, label, link, lit or dark, lighting order) and the corridors
between them, as lists of points. There are two layouts: `wide`, an
80-column Rogue screen, and `narrow`, for phones. The status line's
counts come from the version pages' front matter.

## Custom domain

The site is served at <https://rogueforge.net/>. The custom domain is set
in the repository's **Settings → Pages**; with the Actions-based deploy
no `CNAME` file is needed.
