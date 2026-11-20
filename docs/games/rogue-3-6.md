---
short: Rogue 3.6
year: 1981
machine: VAX and PDP-11
status: rebuilt
summary: The Rogue that went out with 4.1BSD and 2.9BSD, rebuilt to match both the VAX and the PDP-11 binaries.
released: Version string dated 21 April 1981; 4.1BSD binary 11 October 1981
origin: 4.1BSD (TUHS); 2.9BSD /usr/70/rogue and /usr/games/rogue (CSRG Archive, Disc 1)
toolchain: 4.1BSD VAX C compiler; 2.9BSD PDP-11 C compiler
verified: Byte-identical on the VAX and the PDP-11
repo: rogue3.6
---
# Rogue 3.6

Rogue 3.6 is the version most people met first. It shipped with 4.1BSD
for the VAX in 1981 and with 2.9BSD for the PDP-11 in 1983, and copies
of its source travelled to many other sites.

## The 2026 rebuild

There are three binaries, and the rebuilt source matches each of them:

- **4.1BSD, VAX** (93,184 bytes, 11 October 1981): byte-identical. All
  173 of the game's functions match. The binary turns out to be a mix,
  function by function, of two of the surviving site copies.
- **2.9BSD, PDP-11** (82,920 bytes, March 1983): byte-identical, matched
  on 5 July 2026, with all 174 game functions strict matches.
- **2.9BSD, PDP-11, overlaid** (February 1983): a debug build split into
  seven overlays, which keeps its messages in a separate file,
  `roguestrings`. Its code and data are identical; 49 entries in its
  symbol table still differ.

The surviving source copies are dated from January 1982 to June 1984 and
all carry the version string `3.6 (Berkeley) 4/21/81`. They disagree in
places, and the binaries settled which version of each function was compiled.

## Restoration source material

### Original binary releases

Found in the reconstructed 4.1BSD release of 1 September 1981, at
[The Unix Heritage Society](https://www.tuhs.org/Archive/Distributions/UCB/).

Extracted from BSD/Unix 2.9
([rogue3.6-bsd2.9.tar](http://rogue.rogueforge.net/files/rogue3.6/rogue3.6-bsd2.9.tar)),
from the [CSRG Archive](http://www.mckusick.com/csrg/), Disc 1, directory 2.9:

```
-rw-r--r--   1940 1983-08-01 19:08:58 2.9/usr/man/cat6/rogue.6
-rw-r--r--   1604 1983-08-01 17:28:58 2.9/usr/man/man6/rogue.6
-rw-rw-r--  15425 1983-07-26 14:08:26 2.9/usr/doc/rogue
-rwxrwxr-x  82920 1983-03-27 00:21:51 2.9/usr/70/rogue
-rws--x--x 126496 1983-02-06 21:19:14 2.9/usr/games/rogue
-r--------   5531 1982-12-12 22:01:28 2.9/usr/games/lib/roguestrings
```

Extracted from BSD/Unix 2.9pucc
([rogue3.6-bsd2.9pucc.tar](http://rogue.rogueforge.net/files/rogue3.6/rogue3.6-bsd2.9pucc.tar)),
CSRG Archive, Disc 1, directory 2.9pucc:

```
-rw-r--r-- 1492 1984-02-25 03:28:58 2.9pucc/usr/man/man6/rogue.6
```

### Source releases

- **Rogue 3.6 BRL**: [rogue-3.1.tar](http://rogue.rogueforge.net/files/rogue3.6/rogue-3.1.tar),
  5 August 1982. Originally from
  `ftp://emx.utexas.edu/pub/mnt/source/games/rogue-3.1.tar.Z`.
- **Rogue 3.6 NMT**: 23 June 1984, sent by Aydin Edguer.
- **Rogue 3.6 CMU (Rog-O-Matic)**: [r36.tar.Z](http://rogue.rogueforge.net/files/rogue3.6/r36.tar.Z),
  17 March 1985.

## Repository

<https://github.com/rogueforge/rogue3.6>, with a branch for each line of
work:

- `restored-bsd41-19811011`: the 2026 rebuild of the 4.1BSD binary.
- `restored-bsd2.9ov-19830207`: the 2026 rebuild of the overlaid 2.9BSD
  PDP-11 binary, with its messages in `roguestrings`.
- `restored-bsd2.9-19830327`: the 2026 rebuild of the 2.9BSD PDP-11
  binary `/usr/70/rogue`, byte for byte.
- `linux`: the Linux port, with bug fixes.
- `oldmaster`: the earlier restoration, with a branch for each of its
  3.6.x releases.

## Release history

Releases of the earlier restoration. Each has a [GitHub release](https://github.com/rogueforge/rogue3.6/releases)
with its changelog, from the original [Rogue 3.6](https://github.com/rogueforge/rogue3.6/releases/tag/v3.6) source onward.

### January 6, 2015 — [3.6.5](https://github.com/rogueforge/rogue3.6/releases/tag/v3.6.5)

An autoconf build, and updated portability and save-state code.

### September 4, 2008 — [3.6.4](https://github.com/rogueforge/rogue3.6/releases/tag/v3.6.4)

Fixes found by running Rog-O-Matic against it: a hang caused by the
floating eye, an endless loop placing an item in a full room, and daemons
not running while hasted. A manual random seed for testing.

### August 27, 2006 — [3.6.3](https://github.com/rogueforge/rogue3.6/releases/tag/v3.6.3)

Keypad support and native Windows console binaries. Cleaned-up save and
score file formats, incompatible with earlier versions. Many bug fixes.

### February 6, 2005 — [3.6.2](https://github.com/rogueforge/rogue3.6/releases/tag/v3.6.2)

Support for Cygwin and SFU/Interix on Windows; code updated for gcc 3.

### April 30, 2000 — [3.6.1](https://github.com/rogueforge/rogue3.6/releases/tag/v3.6.1)

The first re-release of Rogue, and the project's first release.
