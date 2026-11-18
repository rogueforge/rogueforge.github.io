"""Draw the home page's dungeon map: a Rogue level whose rooms are versions.

The map is described in site.json under "map".  Each layout ("wide" for
an 80-column screen, "narrow" for phones) lists rooms and the corridors
between them:

  room:     {"id", "x", "y", "w", "h", "label", "sub", "href", "lit",
             "step", "items": [[dx, dy, "!"], ...]}
  corridor: {"points": [[x, y], ...], "lit", "step", "shared"}

x/y count from the top left of the map area, which sits under the message
line, as in the game.  w/h include the walls.  A corridor's first and last
points are its doors, on the walls of the rooms it joins.  "step" orders
the page-load sequence in which lit rooms light up; dark rooms stay dark.
"""

from __future__ import annotations

from html import escape


def _draw(layout: dict, page_href, hero_at=None):
    width, height = layout["width"], layout["height"]
    # Each cell: [char, kind, owner] where owner = (lit, step, href|None)
    grid = [[[" ", None, None] for _ in range(width)] for _ in range(height)]

    def put(x, y, ch, kind, owner):
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = [ch, kind, owner]

    for room in layout["rooms"]:
        x0, y0, w, h = room["x"], room["y"], room["w"], room["h"]
        state = "soon" if room.get("soon") else room.get("lit", False)
        owner = (state, room.get("step", 0), None)
        for x in range(x0, x0 + w):
            put(x, y0, "-", "w", owner)
            put(x, y0 + h - 1, "-", "w", owner)
        for y in range(y0 + 1, y0 + h - 1):
            put(x0, y, "|", "w", owner)
            put(x0 + w - 1, y, "|", "w", owner)
            for x in range(x0 + 1, x0 + w - 1):
                put(x, y, "." if owner[0] is True else " ", "f", owner)
        for dx, dy, ch in room.get("items", []):
            put(x0 + dx, y0 + dy, ch, "i", owner)
        link = (state, room.get("step", 0),
                page_href(room["href"]) if room.get("href") else None)
        # Label on the first interior row, the sub-label under it.
        for row, text in ((1, room.get("label", "")), (2, room.get("sub", "")),
                          (3, room.get("note", ""))):
            if not text:
                continue
            lx = x0 + 1 + (w - 2 - len(text)) // 2
            for i, ch in enumerate(text):
                put(lx + i, y0 + row, ch, "l" if row == 1 else "s", link)

    for corr in layout["corridors"]:
        owner = (corr.get("lit", False), corr.get("step", 0),
                 "shared" if corr.get("shared") else None)
        pts = corr["points"]
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            if ax != bx and ay != by:
                raise ValueError(f"corridor segment not straight: {(ax, ay)}->{(bx, by)}")
            sx = (bx > ax) - (bx < ax)
            sy = (by > ay) - (by < ay)
            x, y = ax, ay
            while True:
                if grid[y][x][1] not in ("w", "d"):
                    put(x, y, "#", "c", owner)
                if (x, y) == (bx, by):
                    break
                x, y = x + sx, y + sy
        for dx, dy in (pts[0], pts[-1]):
            put(dx, dy, "+", "d", owner)

    if hero_at:
        hx, hy = hero_at
        last = max([r.get("step", 0) for r in layout["rooms"]]
                   + [c.get("step", 0) for c in layout["corridors"]])
        put(hx, hy, "@", "h", (True, last + 1, None))
    return grid


def _row_html(cells) -> str:
    out = []
    run_key, run_text = None, []

    def flush():
        if run_key is None:
            out.append("".join(run_text))
            return
        kind, (lit, step, href) = run_key
        text = escape("".join(run_text))
        state = "is-soon" if lit == "soon" else ("is-lit" if lit else "is-dark")
        cls = f"m-{kind} {state}"
        if href == "shared":
            cls += " is-shared"
            href = None
        style = f' style="--s:{step}"' if lit else ""
        if href and kind == "l":
            out.append(f'<a class="{cls}" href="{escape(href)}" tabindex="-1"{style}>{text}</a>')
        else:
            out.append(f'<span class="{cls}"{style}>{text}</span>')

    for ch, kind, owner in cells:
        key = (kind, owner) if kind else None
        if key != run_key:
            if run_text:
                flush()
            run_key, run_text = key, []
        run_text.append(ch)
    if run_text:
        flush()
    return "".join(out).rstrip()


def _stickers(layout) -> str:
    """HTML labels laid over rooms, placed on the character grid: x in ch,
    y in lines (the message line comes first, hence the +1)."""
    out = []
    for room in layout["rooms"]:
        if not room.get("sticker"):
            continue
        # On the bottom floor row, nudged onto the wall below it.
        cx = room["x"] + room["w"] / 2 + 1
        cy = room["y"] + 1 + room["h"] - 1.3
        out.append(f'<span class="map-sticker" style="--cx:{cx};--cy:{cy};--s:{room.get('step', 0)}">'
                   f'<span>{escape(room["sticker"])}</span></span>')
    return "".join(out)


def _screen(layout, page_href, message, status, hero_at) -> str:
    grid = _draw(layout, page_href, hero_at)
    lines = [f'<span class="m-msg">{escape(message)}</span>']
    lines += [_row_html(row) for row in grid]
    lines.append(f'<span class="m-stat">{escape(status)}</span>')
    return "\n".join(lines) + _stickers(layout)


def render_map(spec: dict, page_href, stats: dict) -> str:
    status = spec["status"].format(**stats)
    parts = []
    for name in ("wide", "narrow"):
        layout = spec[name]
        parts.append(
            f'<pre class="dungeon dungeon--{name}" aria-hidden="true">'
            + _screen(layout, page_href, layout.get("message", spec["message"]),
                      layout.get("status", status).format(**stats),
                      layout.get("hero"))
            + "</pre>")
    return '<div class="map-frame">\n' + "\n".join(parts) + "\n</div>"
