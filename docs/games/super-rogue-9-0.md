---
short: Super-Rogue 9.0
year: 1983–84
machine: Unix
status: soon
summary: Robert Kindelberger's expansion of Rogue 3.6 at Bell Labs, restored from his source in 2005.
released: Circa May 1983 to July 1984
origin: Source from Robert D. Kindelberger, 2004
verified: Restored 2005; not yet rebuilt from a binary
repo: srogue9.0
---
# Super-Rogue 9.0

Super-Rogue was developed by a group of employees at **AT&T Bell Labs
between 1982 and 1983**, with the public face of the group being
**Robert D. Kindelberger**. Internal and friends-only releases include
versions 6.5, 7.2, 8.0, 8.3, culminating in 9.0 (circa 5/7/83 through
7/17/84).

Super-Rogue 9.0 is based on the Rogue 3.6 source code. Robert Kindelberger
provided the long-elusive source code in 2004.

The restoration of this version requires the standard updates for using
gcc / ANSI-style C compilers, fixes for some bugs inherited from Rogue 3.6,
and new save/restore code.

## Other surviving copies

- **A 1985 build for the AT&T UNIX PC.** An install package for the UNIX
  PC's office shell, "Rogue - Version 1.2 - 02/21/85", holds a 68000 binary
  of 9.0 whose version line is "9.0 ( 5/ 7/83) [SC was here 2/85]": built
  from the May 1983 state of 9.0, ported by S. Coffin, who asks in the
  install script for bug reports. It adds Rogue to the UNIX PC's Toybox menu,
  with Kindelberger's tutorial, dated 22 February 1985.
- **Super-Rogue 7.2** (Bell Labs, 28 October 1982), an earlier version,
  "essentially Super Rogue 7.0 as released from Bell Labs" with later fixes,
  survives in [Julian Onions's repository](https://github.com/JulianOnions/rogue-7.2).
  It reached him in 1987 from Strathclyde, which had it from Hasler in
  Switzerland.

## Repository

<https://github.com/rogueforge/srogue9.0>, with a branch for each line of
work:

- `master`: where the port and bug fixes will go. For now it is the same
  as `restored`.
- `restored`: Robert D. Kindelberger's source of 9.0 (July 17, 1984), with
  his February 1985 tutorial.
- `oldmaster`: the earlier restoration and its 9.0-1 release.

## Release history

### March 22, 2005 — 9.0-1

All obvious bugs worked out. Tarballs of binaries now active.

### March 6, 2005 — 9.0.1 beta2

Save/restore functional. Minimally tested. (Available by CVS checkout only
at the moment.)

### March 4, 2005 — 9.0.1 beta

Trivial port complete. Save/restore non-functional. (Available by CVS
checkout only.)
