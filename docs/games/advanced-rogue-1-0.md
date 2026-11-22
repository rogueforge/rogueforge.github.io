---
short: Advanced Rogue 1.0
year: 1983
machine: Unix
status: port
summary: The first Advanced Rogue, from Bell Labs in 1983, a fork of Super-Rogue 8.0 (December 1982).
released: Version string dated 23 April 1983
origin: Source copy with file dates of 4 December 1989
verified: Ported to Linux; not yet rebuilt from a binary
repo: arogue1.0
---
# Advanced Rogue 1.0

The first Advanced Rogue, from **AT&T Bell Labs**. Its version string
reads "1.0 (Bell Labs) 4/23/83", so it is two years older than Advanced
Rogue 5.8 and three older than 7.7, the versions that circulated widely.

Advanced Rogue began as a fork of Super-Rogue 8.0, taken at Bell Labs in
December 1982 or soon after. Under it is Rogue 3.6: several files
still carry their Berkeley stamps from June 1981. The files that make it
more than Rogue carry stamps of 7.0, from "Indian Hill" and "Bell Labs" in
October 1982, and 8.0 from December 1982. They match Super-Rogue 9.0's own:
the trading post is the same code, down to its "Welcome to Friendly Fiend's
Flea Market" screen, and so are the encumbrance and maze routines. What
Super-Rogue added after the fork is missing. Advanced Rogue's encumbrance
counts weight only, where Super-Rogue 9.0 also counts how much room a pack
has, and it has none of 9.0's version stamps.

Super-Rogue 7.2 survives as well (in [Julian Onions's
repository](https://github.com/JulianOnions/rogue-7.2), dated 28 October
1982), and comparing it settles the point: the fork came after 7.2.
Advanced Rogue 1.0 has things 7.2 lacks and 9.0 has: the three files
stamped 8.0 (`daemon.c`, `list.c` and `trader.c`, 16 December 1982, which
7.2 has at 7.0), maze levels ("You are surrounded by twisty passages!") and
dipping things in a pool. It has none of 9.0's later additions, such as the
item screens with weights and charges, or the graveyard tombstone.

It is not a superset of Super-Rogue, though. Advanced Rogue replaced
Super-Rogue's bestiary (the anhkheg, elasmosaurus, koppleganger and the
rest, in both 7.2 and 9.0) with its own, taken from the *Dungeons &
Dragons Monster Manual*, and dropped some of its items, such as the ring
of agility and the scroll of annihilate monster. The character classes, in
`player.c` stamped "7.0 (Indian Hill)", have no counterpart in Super-Rogue
7.2 or 9.0, so Advanced Rogue may have begun as a locally changed copy.
Already in 1.0 a player can be a fighter, magician, cleric or thief, and the
dungeon has mazes, a trading post and over a hundred monsters.

In December 1982 Ken Dalka, later one of Advanced Rogue's authors, wrote
to net.games.rogue from Indian Hill that the version he played was "called
Super Rogue 7.2", adding that it "might have local modifications".

Advanced Rogue spread quickly through AT&T. In January 1984 a player at AT&T
Consumer Products in Denver wrote that he had "used Advanced Version 1.0",
the earliest mention found. By spring 1984 version 1.3 was being installed
and ported at other sites: a player described its "option to pick one of
four character classes", its flea market and its mazes. A 2.0 followed by
November 1984, and alongside it versions numbered 5.0 to 5.5, the line that
led to the Advanced Rogue 5.8 and 7.7 that survive. Version 1.0 was still
being played in 1985, at Ohio State and St. Olaf College. UltraRogue's own
notes say it took changes "from Advanced Rogue 1.0 and/or SuperRogue".

## Restoration source material

The surviving copy is a single archive of 46 files, all dated 4 December
1989, which came to the project from a rogue enthusiast. It was copied
through MS-DOS: the lines end in CR-LF, and some file names were cut to
eight characters, `machxdep.h` for `mach_dep.h` and `newxleve.c` for
`new_level.c`. The code was written for System V Unix, and this copy was
set up to build at a later, unknown site, with its score file under
`/obelix/mnt/scottha`. Besides the game, the archive holds a description of
every monster (`monsters`), an older `rip.c`, a few small listing tools,
and a sample set of options:

```
setenv ROGUEOPTS "class=cleric,flush,jump,askme"
```

The version stamps found in the source:

| File | Stamp |
|---|---|
| `vers.c` | 1.0 (Bell Labs) 4/23/83 |
| `daemon.c`, `list.c`, `trader.c` | 8.0 (Bell Labs) 12/16/82 |
| `encumb.c` | 7.0 (Bell Labs) 10/08/82 |
| `player.c` | 7.0 (Indian Hill) 10/5/82 |
| `rip.c`, `save.c` | 3.13 and 3.9 (Berkeley) 6/16/81 |
| `rooms.c`, `passages.c` | 3.8 and 3.4 (Berkeley) 6/15/81 |
| `curses.h` | 1.14 (Berkeley) 7/4/83 |

## Repository

<https://github.com/rogueforge/arogue1.0>, with a branch for each line of
work:

- `master`: the port to Linux, with bug fixes. To build it,
  `cd src && make -f Makefile.linux`.
- `restored`: the source as it survives, dated April 23, 1983, with its
  file names put back.
