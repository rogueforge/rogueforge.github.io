---
short: PC Rogue 1.48
year: 1983–85
machine: IBM PC
status: soon
summary: The IBM PC Rogue that Epyx sold. It grew from Berkeley's Rogue 5.2, and shares part of its work with Rogue 5.3.
released: Beta 1983; version 1.48 dated 30 December 1985
origin: A.I. Design source for version 1.48
toolchain: Lattice C, then Microsoft C, for MS-DOS
verified: Source ported to 4.3BSD in 2026; the DOS binaries are not yet rebuilt
---
# PC Rogue 1.48

Rogue came to the IBM PC through A.I. Design, with Jon Lane adapting it,
and Epyx sold it from 1985. For many people it was the first Rogue they
played: the PC's own line-drawing characters, a title screen, and copy
protection.

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

So the two lines shared some of their work and not the rest. See
[How the versions are related](../../history/#how-the-versions-are-related) for the
evidence.

## The DOS releases

Four builds of the DOS game have been compared:

| Build | Compiler | Credits |
|---|---|---|
| ".1" beta | Lattice C 1.00 | (C) 1983 Artificial Intelligence Design Systems |
| 1.1 | Lattice C 1.02 | Public domain, 1984, "not to be sold" |
| 1.45 | Microsoft C | (C) 1985 Epyx |
| 1.49 | Microsoft C | (C) 1985 Epyx |

The credits change as the game moved from A.I. Design to Epyx. The 1983
beta says Rogue "was originated by Michael C. Toy and Kenneth C.R.C.
Arnold, adapted for the IBM PC by Jon Lane, with additional contributions
by Glenn Wichman and scores of others". By 1.45 it reads "designed by
Michael Toy and Glenn Wichman; various implementations by Ken Arnold,
Jon Lane and Michael Toy; adapted for the IBM PC by A.I. Design". The
builds also carry the programmers' own marks: "Mr. Mctesq was here",
"jll was here", and in the beta, "You Rang -- Dick Brain".

## The 2026 port

In 2026 the 1.48 source was carried back to 4.3BSD, as if PC Rogue had
been brought home to Berkeley next to Rogue 5.4. The port keeps the game
and drops the PC machinery: the BIOS screen code, A.I. Design's own
curses, the copy protection, the title picture, the shareware demo and
the fake-DOS boss key. Optional build settings bring back the PC credits
screen and clock, and the code page 437 map characters.

A Linux port with bug fixes follows the same pattern as the Berkeley
versions. Both are coming to GitHub soon.
