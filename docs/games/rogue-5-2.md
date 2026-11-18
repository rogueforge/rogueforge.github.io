---
short: Rogue 5.2
year: 1982
machine: VAX
status: rebuilt
summary: The first of the 5.x line, rebuilt to match the copy on the last 4.1BSD tape.
released: Version string dated 11 April 1982; binary 20 July 1982
origin: 4.1BSD last tape, /usr/games/rogue (CSRG Archive, Disc 1)
toolchain: 4.1BSD VAX C compiler
verified: Byte-identical, 19 July 2026
repo: rogue5.2-19820720-bsd4.1, rogue5.2
---
# Rogue 5.2

Rogue 5.2 began the 5.x line, the redesign that became the Rogue most
Unix sites ran. It was developed for the VAX and PDP-11 running
BSD Unix.

## The 2026 rebuild

Two Rogue 5.2 binaries survive: one in 4.1c.2BSD from June 1982, and a
slightly larger one on the last 4.1BSD tape, dated 20 July 1982. The
rebuild matches the July binary, all 91,036 bytes.

It starts from the source as it stood on 19 May 1982 and adds what the
binary shows was there: a signal handler that is saved and never used,
the site's own machine-dependent file, and a rebuilt C start-up routine.
The site file's misspelling, "O exaulted one", is genuine.

## Restoration source material

### Binary releases

Extracted from BSD/Unix 4.1c.2
([rogue5.2-bsd4.1c.2.tar](http://rogue.rogueforge.net/files/rogue5.2/rogue5.2-bsd4.1c.2.tar)),
from the [CSRG Archive](http://www.mckusick.com/csrg/), Disc 1, directory 4.1c.2:

```
-rw-r--r--  1614 1983-02-12 13:14 4.1c.2/usr/man/man6/rogue.6
-rwsr-xr-x 90112 1982-06-08 10:35 4.1c.2/usr/games/rogue
-rw-r--r-- 22021 1982-07-20 11:32 4.1c.2/usr/doc/rogue
```

**Rogue 5.2 CMU (Rog-O-Matic)**:
[rogue53.tar.Z](http://rogue.rogueforge.net/files/rogue5.2/rogue53.tar.Z),
16 February 1986, originally from `http://robot-club.com/lti/rogue53.tar.Z`.
Despite its name this is a binary distribution of Rogue 5.2, with
supporting files for Rog-O-Matic that may have been meant for Rogue 5.3.
It includes the parts for customising the game to a site and building
the final executable, which is probably how Rogue 5.2 was distributed.

### Source releases

- **Rogue 5.2 NMT**: [rog52-nmt.tar](http://rogue.rogueforge.net/files/rogue5.2/rog52-nmt.tar),
  20 September 1993, provided by Aydin Edguer.
- **Rogue 5.2**: 11 October 1999. The original archive's dates are lost.
  It came from the anonymous FTP site at `uxc.cso.uiuc.edu/games/rogue`,
  now gone, in the early 1990s, and is probably close to unmodified.

## Repositories

- <https://github.com/rogueforge/rogue5.2-19820720-bsd4.1>: the 2026
  rebuild.
- <https://github.com/rogueforge/rogue5.2>: the earlier restoration.
