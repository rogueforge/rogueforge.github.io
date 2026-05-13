# Project goals

RogueForge exists to **preserve and maintain** classic Rogue and its direct
descendants as living, buildable software — not as binary curios in a
museum vitrine.

## What "restoration" means here

For each version we aim to:

1. **Recover** the most authoritative source we can locate: original
   distribution tapes, BSD CSRG discs, archival FTP mirrors, personal
   correspondence with the original authors, and — when no source
   survives — reconstruction from preserved binaries via static and
   dynamic analysis (Ghidra, radare2/rizin, hand annotation).
2. **Compile** on modern systems. C89 → C99/C11 cleanups, sufficient
   `machdep` shims, replacement of disappeared system calls.
3. **Save/restore** the game state portably. Many originals used
   architecture-specific `core` files; we replace that with a portable
   binary or JSON format that survives across hosts.
4. **Document**. Manual pages, recovered design notes, a per-game guide,
   and — where the original authors are reachable — their first-hand
   recollections.

## Non-goals

- We are not building a new roguelike. Where gameplay diverges from the
  original (notably **UltraRogue**), that divergence is intentional and
  inherited from the original author's later work; we are not adding new
  features of our own.
- We are not maintaining ancient build environments. If the only way to
  rebuild a version is on a VAX, we'll wrap that in a modern toolchain
  before declaring it restored.

## Migration to GitHub

The original [rogueforge.net](http://www.rogueforge.net) site ran a
**CMS Made Simple** install on **Debian Squeeze (PHP 5.3)** since 2004 —
both long out of support. Development used a self-hosted **Trac /
Subversion** instance for two decades. In 2026 the project is moving to:

- **Code**: GitHub, under [`github.com/rogueforge`](https://github.com/rogueforge),
  one repository per restored game.
- **Site**: this GitHub Pages site, rebuilt from markdown.
- **Issue tracking**: GitHub issues, per repo.

See [history/sources](../../history/sources/) for where each version was
rescued from.
