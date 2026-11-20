---
short: PC Rogue 1.48
year: 1983–86
machine: IBM PC
status: soon
summary: The IBM PC Rogue that Epyx sold. It grew from Berkeley's Rogue 5.2, and shares part of its work with Rogue 5.3.
released: A.I. Design 1983; Epyx 1.45 to 1.49, 1985–86 (1.48 source dated 30 December 1985)
origin: A.I. Design source for version 1.48
toolchain: Lattice C, then Microsoft C, for MS-DOS
verified: Source ported to 4.3BSD in 2026; the DOS binaries are not yet rebuilt
---
# PC Rogue 1.48

Rogue came to the IBM PC through A.I. Design, short for Artificial
Intelligence Design, a small company in Santa Clara, California. Michael
Toy met Jon Lane at Olivetti, where Lane suggested a commercial version
for the IBM PC. Lane adapted the game with Mel Sibony, who also made its
international versions. A.I. Design published PC Rogue itself in 1983;
Epyx took it on as publisher in 1984 and sold it from 1985. For
many people it was the first Rogue they played: the PC's own
line-drawing characters, a title screen, and copy protection.

The source of version 1.48, dated 30 December 1985, survives in three
copies. The oldest has its original 1984–85 file dates and K&R style; the
other two are a reformatted copy and a modernised one, both made from it.

## Where it came from

PC Rogue is not a port of Rogue 5.4, although it shipped in the same
years. Comparing the code function by function, PC Rogue follows Rogue
5.2: where 5.2 and 5.3 differ, PC Rogue's version is closer to 5.2 in
115 functions and to 5.3 in 12. It keeps 5.2's crossbows, its potions of
paralysis and thirst quenching and its scrolls of blank paper, all of
which Berkeley dropped in 5.3.

But it also has the new monsters that first appear at Berkeley in
5.3: the aquator, griffin, ice monster, jabberwock, kestrel, medusa,
phantom, quagga, rattlesnake, venus flytrap and xeroc, along with 5.3's
scroll of food detection and its poison dart trap. PC Rogue's list
differs in a few places: a slime where Berkeley has a snake, an ur-vile
where Berkeley has a black unicorn, and "kestral" where Berkeley spells
it "kestrel". The PC's earliest surviving build, a 1983 beta, already
has the new monsters.

So the two lines shared some of their work and not the rest.

## The DOS releases

Four builds of the DOS game have been compared, alongside the 1.48
source:

| Build | Date | From | Compiler | Credits |
|---|---|---|---|---|
| ".1" beta | 1983 | A.I. Design | Lattice C 1.00 | (C) 1983 Artificial Intelligence Design Systems |
| 1.1 | — | A.I. Design | Lattice C 1.02 | Altered by a crack in the surviving copy |
| 1.45 | 1985 | Epyx | Microsoft C | (C) 1985 Epyx |
| 1.48 | 30 December 1985 | A.I. Design, for Epyx | Microsoft C | Source only |
| 1.49 | 1986 (copy dated 30 May) | Epyx | Microsoft C | (C) 1985 Epyx |

The credits change as the game moved from A.I. Design to Epyx. The 1983
beta says Rogue "was originated by Michael C. Toy and Kenneth C.R.C.
Arnold, adapted for the IBM PC by Jon Lane, with additional contributions
by Glenn Wichman and scores of others". By 1.45 it reads "designed by
Michael Toy and Glenn Wichman; various implementations by Ken Arnold,
Jon Lane and Michael Toy; adapted for the IBM PC by A.I. Design". The
builds also carry the programmers' own marks: "Mr. Mctesq was here",
"jll was here", and in the beta, "You Rang -- Dick Brain".

## What the source says

The 1.48 source keeps A.I. Design's own version stamps, from February
1984 to December 1985, and Michael Toy's signature on its replacement
`printf`: "Michael Toy, AI Design, January 1984". The copyright in
`main.c` belongs to "Mel Sibony, Jon Lane (AI Design update for the
IBMPC)", 1983.

Its title screen credits "Adapted for the IBM PC by A.I. Design,
(C)Copyright 1985 Epyx Incorporated"; built for the international
versions, it names Mel Sibony instead, with the copyright to AI Design.
The shareware demo ends by telling you to write to A.I. Design at
P.O. Box 3685, Santa Clara, California, if you want to do some more
exploring in the Dungeons of Doom.

A few other things show the company at work. The function that loads
Epyx's title picture is called `epyx_yuck()`. And the tombstone prints
its name and killer from two strings that start out as "Software Pirate"
and "Copy Protection Mafia", and it seems the copy protection swaps
them for your own name and killer on a genuine disk.

## The 2026 port

In 2026 the 1.48 source was carried back to 4.3BSD, as if PC Rogue had
been brought home to Berkeley next to Rogue 5.4. The port keeps the game
and drops the PC machinery: the BIOS screen code, A.I. Design's own
curses, the copy protection, the title picture, the shareware demo and
the fake-DOS boss key. Optional build settings bring back the PC credits
screen and clock, and the code page 437 map characters.

A Linux port with bug fixes follows the same pattern as the Berkeley
versions. Both are coming to GitHub soon.
