---
short: Rogue 5.4
year: 1985
machine: VAX
status: rebuilt
summary: The last Berkeley Rogue, found in the 4.3BSD tree as a stripped object file, rebuilt with a compiler dated to early 1985.
released: Version string "rogue 31/03/85"; in the 4.3BSD tree, 1986
origin: 4.3BSD, /usr/src/games/rogue/main.obj (CSRG Archive, Disc 1)
toolchain: CSRG VAX C compiler as of early 1985
verified: Identical after stripping, with two small post-compile patches
repo: rogue5.4
---
# Rogue 5.4

Rogue 5.4 is the version found with 4.3BSD, and the basis of almost
every modern port. In the 4.3BSD source tree it is a single object
file, `main.obj`, with its symbols stripped, together with the
machine-dependent source a site needed to finish the build. The only
date inside is the version string, `rogue 31/03/85`.

## The 2026 rebuild

Rogue 5.4 was the first version attempted, in March 2026, and the first
to come close. Ghidra's VAX support needed fixing before it could read
the object file at all; once it could, 234 functions and 270 globals
were recovered.

The source Ken Arnold published on SourceForge in 2002 was the starting
point, and it is close, but it is not quite the game in the binary:
in places it is an earlier state, nearer Rogue 5.3. The 1985 binary has
commands and routines that appear in no surviving source: `a` to repeat a command,
`,` to pick something up, a mystery trap, and functions named
`door_look()`, `replay()` and `reset_fight()`.

No released compiler reproduces the code. Two dated changes in the
compiler's own source bracket the one that did, between January and
December 1985. A compiler rebuilt from Berkeley's sources as of
19 March 1985 matches 232 of 234 functions, which fits the date in the
version string.

### What is still open

After stripping, the rebuild matches `main.obj` only with two small
patches applied after compiling: the exit from `do_move()`, and six
bytes of register choice in `command()`. The likely cause is a compiler
build a little different from the one reconstructed. The 4.3BSD
installed binary is not yet an exact match either.

## Restoration source material

### Binary releases

Extracted from BSD/Unix 4.3
([rogue5.4-bsd4.3.tar](http://rogue.rogueforge.net/files/rogue5.4/rogue5.4-bsd4.3.tar)),
from the [CSRG Archive](http://www.mckusick.com/csrg/), Disc 1, directory 4.3:

```
-r--r--r--   1589 1986-01-09 05:40 4.3/usr/src/games/rogue/machdep.h
-r--r--r--    633 1986-01-09 05:40 4.3/usr/src/games/rogue/Makefile
-r--r--r--    538 1986-01-09 05:40 4.3/usr/src/games/rogue/README
-r--r--r-- 125368 1986-01-10 23:47 4.3/usr/src/games/rogue/main.obj
-r--r--r--   8819 1986-01-10 23:47 4.3/usr/src/games/rogue/machdep.c
-r--r--r--   2283 1986-05-06 03:14 4.3/usr/man/man6/rogue.6
-rws--x--x 113664 1986-06-05 19:57 4.3/usr/games/rogue
-r--r--r--  24806 1986-04-28 06:05 4.3/usr/doc/usd/33.rogue/rogue.me
-r--r--r--    630 1986-04-27 12:01 4.3/usr/doc/usd/33.rogue/Makefile
```

Extracted from BSD/Unix 2.10
([rogue5.4-bsd2.10.tar](http://rogue.rogueforge.net/files/rogue5.4/rogue5.4-bsd2.10.tar)),
CSRG Archive, Disc 1, directory 2.10:

```
-r--r--r--  2283 1986-12-14 03:08 2.10/root/usr/man/man6/rogue.6
-r--r--r-- 15425 1983-07-26 14:08 2.10/root/usr/doc/2.10/rogue
-r--r--r-- 24806 1986-04-28 06:05 2.10/root/usr/doc/usd/33.rogue/rogue.me
-r--r--r--   630 1986-04-27 12:01 2.10/root/usr/doc/usd/33.rogue/Makefile
```

### Source releases

- **Ken Arnold's SourceForge release, first version**:
  [rogue-r1.1.tar.gz](http://rogue.rogueforge.net/files/rogue5.4/rogue-r1.1.tar.gz),
  22 April 2002, from <https://sourceforge.net/projects/rogue/>.
- **Ken Arnold's SourceForge release, current**:
  [rogue.tar.gz](http://rogue.rogueforge.net/files/rogue5.4/rogue.tar.gz),
  1 October 2013.

## Repository

<https://github.com/rogueforge/rogue5.4>, with a branch for each line of
work:

- `restored-bsd43-19860109`: the 2026 rebuild of `main.obj` from 4.3BSD.
- `restored-bsd42-19840331`: Ken Arnold's later source, back-ported to the
  C of the period to show what it might have looked like. It is not
  verified against any binary.
- `linux`: the Linux port, with bug fixes.
- `oldmaster`: the earlier restoration and its 5.4.x releases.

## Release history

Releases of the earlier restoration. Each has a [GitHub release](https://github.com/rogueforge/rogue5.4/releases)
with its changelog, from Ken Arnold's [Rogue 5.4](https://github.com/rogueforge/rogue5.4/releases/tag/v5.4) source onward.

### August 24, 2008 — [5.4.5](https://github.com/rogueforge/rogue5.4/releases/tag/v5.4.5)

The last release of the earlier restoration.

### September 5, 2007 — [5.4.4](https://github.com/rogueforge/rogue5.4/releases/tag/v5.4.4)

Save and restore fixed; a crash when calling a weapon fixed; autoconf
files in the source tarball; an RPM spec and desktop files contributed by
Wart; a port to Mac OS X.

### July 23, 2007 — [5.4.3](https://github.com/rogueforge/rogue5.4/releases/tag/v5.4.3)

Fixes to wielding and wearing; an autoconf build; issues raised by Fedora
packagers addressed.

### January 29, 2006 — [5.4.2](https://github.com/rogueforge/rogue5.4/releases/tag/v5.4.2)

Save and restore fixed, and keypad and cursor key support added.

### January 4, 2006 — [5.4.1](https://github.com/rogueforge/rogue5.4/releases/tag/v5.4.1)

The first release.
