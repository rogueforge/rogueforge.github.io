---
short: Rog-O-Matic XIV
year: 1984
machine: VAX
status: port
summary: The program from Carnegie Mellon that plays Rogue, and for a time played it better than anyone.
origin: Carnegie Mellon University
repo: rogomatic14
---
# Rog-O-Matic XIV

The program that plays Rogue by itself, developed at **Carnegie Mellon
University** by Michael Mauldin, Guy Jacobson, Andrew Appel and Leonard
Hamey. Rog-O-Matic was for a time the strongest known Rogue player,
human or machine, and it is one of the earliest substantial pieces of
game-playing AI to survive in source form.

Rog-O-Matic drives a real copy of Rogue through a terminal, reading the
screen as a player would. The CMU distribution was tied to particular
versions of the game: Rogue 3.6 and Rogue 5.2, whose binary came packaged
with supporting files for 5.3 (see [Rogue 5.2](rogue-5-2.md)).

## The paper

Michael L. Mauldin, Guy Jacobson, Andrew Appel and Leonard Hamey,
*ROG-O-MATIC: A Belligerent Expert System*. Fifth Biennial Conference of
the Canadian Society for Computational Studies of Intelligence, London,
Ontario, 16 May 1984. An earlier version is Carnegie-Mellon University
Technical Report CMU-CS-83-144, July 1983.

The paper describes Rog-O-Matic as an expert system that combines
algorithmic knowledge sources with production rules to explore a hostile,
partly hidden world: the Dungeons of Doom. It covers the program's
architecture, the experts that decide when to fight, flee, explore or
use an object, how it learns about monsters from game to game, and how
it compares with human players. In games against Rogue 5.2 at CMU from
January 1 to February 21, 1983, it had the best median score of any of
the strong players it was measured against.

- [ROG-O-MATIC: A Belligerent Expert System](../docs/rogomatic-paper.md),
  Fifth Biennial Conference of the Canadian Society for Computational
  Studies of Intelligence, 1984.
- [ROG-O-MATIC: A Belligerent Expert System](../docs/rogomatic-report.md),
  Technical Report CMU-CS-83-144, Carnegie-Mellon University, 1983.

A. K. Dewdney wrote about it in *Scientific American*'s Computer
Recreations column in February 1985:

- [An expert system outperforms mere mortals as it conquers the feared Dungeons of Doom](../docs/rogomatic-sciam.md),
  *Scientific American*, vol. 252, no. 2, February 1985, pp. 18–21.

## Rog-O-Matic and Rogue's authors

Rogue's authors knew about it. Ken Arnold made it his rule "that every
release of Rogue would break Rog-O-Matic", with small quirks such as
hallucination that made the game "more unpredictable and quirky without
changing the gameplay" ([panel, 2016](../talks/rogue-panel-2016.md), at
12:27; [video](https://www.youtube.com/watch?v=4IkrZkUV01I&t=747s)).

## Total winners

When Mauldin posted Rog-O-Matic XIV to net.sources in February 1985, he
listed the versions of Rogue it had beaten, retrieving the Amulet of Yendor
and coming back up alive:

- Rogue 3.6, at Carnegie Mellon, on September 26, 1982.
- Rogue 5.2, at the University of Waterloo, on October 10, 1983.
- Rogue 5.3, at the University of Texas, on February 16, 1984. Some of the
  changes made there by Dan Reynolds went into Rog-O-Matic XIV.

## The 2026 restoration

The `master` branch gathers the work that kept Rog-O-Matic playing after
CMU: Peter Schauer's fixes from 2008, Anthony Molinaro's support for
Rogue 5.4 and his release of it under the GNU GPL, and the project's own
2008 port to Linux, ncurses and 64-bit systems.

In November 2026 it gained `rgmloop`, which plays many seeded games
unattended, on a pseudo terminal, with memory-checked builds and a record
of where any game that hangs went wrong; `rgmrerun`, which types a logged
game back into Rogue; and a run of bug fixes found that way.

## Repository

<https://github.com/rogueforge/rogomatic14>. `master`, the default
branch, carries the current work. The `mlm`, `ant`, `leland`, `molinaro`
and `schauer` branches keep the lines of work it was gathered from, and
`oldmaster` the earlier restoration.

## Release history

### September 5, 2008

Continuing to patch the source. It now plays the repository versions of
Rogue 3.6 and 5.2, and Rogue 5.4 less well; that needs a fix to the
message parsing.

### August 25, 2008 — a home at RogueForge

After applying Peter Schauer's patches to Rogue 5.2, I tried his patches
for Rog-O-Matic XIV too, and watched it become a total winner six times
over as it played 10,000 games in about four hours. If nothing else it is
a useful tool for testing Rogue, so it now has a home here.
