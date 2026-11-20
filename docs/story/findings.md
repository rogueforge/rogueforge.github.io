---
glyph: glyph-bang
summary: Rebuilding source to the byte turns up things no surviving copy recorded, from bugs that shipped to commands nobody knew Rogue 5.4 had.
---
# What the binaries told us

When the rebuilt source has to match the binary exactly, nothing in the
binary can be explained away. Every instruction has to come from
somewhere. Some of what that turned up:

## Bugs that shipped

- **Rogue 3.4** scores food as if it were a weapon, through a missing
  `break` in a `switch`. The 1981 binary has the same fall-through, so
  the bug is original.
- **Rogue 3.4**'s `missile()` tests whether the hero is confused where
  the surviving source tests whether the hero is blind.
- **Rogue 3.6** on the VAX was linked against a curses library with its
  own 1981 bug: `getcap` returns the result of `tgetent` instead of the
  capability it was asked for.
- **Rogue 4.22**'s machine-dependent file tests a character with
  `>= '0' || c <= '5'`, which is true of everything.
- **Rogue 5.3** calls `printw(0, 0, ...)` as though it were `mvprintw`,
  and leaves a pointer to a local `coord` behind after the function
  returns.

## Things the source forgot

- **Rogue 5.4** has features found in no surviving source, including
  the version Ken Arnold later published: an `a` command to repeat the
  last command, `,` to pick up an object, a mystery trap, and routines
  named `door_look()`, `replay()` and `reset_fight()`. The Arnold source
  turns out to be closer to Rogue 5.3.
- **Rogue 5.3**'s object file holds four declarations that do nothing
  except take up slots in the symbol table. Without them the table does
  not match, so they must have been in the original source.
- **Rogue 5.3** also keeps an orphan string, `after signal`, that no
  code in the surviving source uses.
- **Rogue 3.4** contains a debugging helper, `Decho()`, which has to sit
  at the top of its file for the binary to match, and sets the heaviest
  pack a hero can carry at 55, not 40.
- The **2.9BSD Rogue 3.6** built with overlays keeps its messages in a
  separate file, `roguestrings`, loaded from disk as needed to save
  memory on the PDP-11. That file is dated 12 December 1982.

## Fingerprints of the people and places

- **Rogue 4.22** and **5.2** recognise their author by user id: the
  site files check for uid 80.
- **Rogue 5.2**'s site file misspells "O exaulted one", and the
  rebuild keeps the typo because the binary has it.
- **Rogue 5.3**'s object files carry names from Berknet, Berkeley's
  campus network software: `terminal.o`, `rmove.o`, `network.o`. The
  linker recorded them in the symbol table, so the rebuild has to use
  them too.
- **Rogue 4.22**'s strings were extracted in alphabetical order of
  source file, with a second pass for `save.c`. Reproducing that order
  was necessary to put each string at the right address.

## The manual too

The roff source of *A Guide to the Dungeons of Doom*, Michael Toy's
manual for Rogue 3.4, is lost; the oldest that survives is a revised
edition from 1982. The 1981 text survives only as formatted output,
`rogue.doc`. Its source has been rebuilt, using the Version 7 `tbl`,
`nroff` and `col`, until it formats to exactly that file.

The timestamps tell their own story. The Rogue 3.4 binary was built at
04:41:44 on 21 May 1981, and that copy of the Guide was formatted at
04:41:57, thirteen seconds later.
