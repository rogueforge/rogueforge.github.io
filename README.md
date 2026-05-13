# rogueforge.github.io

Source for the **RogueForge** umbrella project site — the GitHub Pages
replacement for [rogueforge.net](http://www.rogueforge.net).

The published site lives at <https://rogueforge.github.io/> (root URL, no
subdirectory — this works because the repo is named `rogueforge.github.io`
inside the `rogueforge` GitHub organization; GitHub Pages treats that name
as the org's root site).

## Layout

```
.
├── docs/                       Markdown sources, one file per page.
│   ├── README.md               Rendered into the homepage "About" section.
│   ├── games/*.md              The Games section.
│   ├── docs/*.md               Documentation section.
│   ├── history/*.md            History & provenance section.
│   └── about/*.md              About section.
└── gh-pages/
    ├── site.json               Site metadata + section (group) definitions.
    ├── templates/              home.html, group.html, doc.html.
    ├── assets/                 site.css, logo images.
    ├── build_site.py           The static-site builder.
    └── public/                 Built output (gitignored; CI publishes this).
```

The pattern is borrowed from the `rappture-monorepo` gh-pages builder, so
if you've worked on that, this will look familiar.

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

1. Drop a new markdown file under `docs/<section>/your-slug.md`.
   The filename becomes the URL slug (`/<section>/your-slug/`).
2. The first H1 in the markdown becomes the page title; the rest of the
   file is rendered as the page body.
3. Cross-page links: use relative markdown links
   (`../other-section/page.md` or `same-section-page.md`). The builder
   rewrites them to pretty URLs.
4. To add a whole new section, add an entry to `gh-pages/site.json`
   under `groups` and create a corresponding `docs/<slug>/` directory.

## Custom domain

To keep using `rogueforge.net` as the public URL, place the bare domain
name in a file called `CNAME` at the root of the built site (you can drop
it in `gh-pages/assets/CNAME` so it gets copied into `public/assets/` —
or, simpler, add a copy step in the workflow that writes it directly to
the deployed artifact). DNS configuration is documented at
<https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site>.
