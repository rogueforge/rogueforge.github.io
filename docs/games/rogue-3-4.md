---
short: Rogue 3.4
year: 1981
machine: PDP-11
status: rebuilt
summary: The earliest Rogue whose binary survives, from 2.8BSD for the PDP-11, and the first version rebuilt byte for byte.
released: Version string dated 16 April 1981; built 21 May 1981
origin: 2.8BSD, /usr/bin.v7/ucb/rogue (CSRG Archive, Disc 1)
toolchain: 2.8BSD Ritchie C compiler and a pre-release 2.8BSD library
verified: Byte-identical, 3 July 2026
repo: rogue3.4
---
# Rogue 3.4

Rogue was written at UC Santa Cruz and UC Berkeley by Michael Toy and
Glenn Wichman, with Ken Arnold. Version 3.4 is the oldest that survives
as a program: a 70,364-byte PDP-11 executable on the 2.8BSD distribution,
built at 04:41 on the morning of 21 May 1981.

## The 2026 rebuild

Rogue 3.4 was the hardest of the rebuilds and the one that set the
standard for the rest. The binary is fully stripped, so none of its 266
functions arrived with a name. 145 of them are the game; the other 121
are the C library, and those had to match too. No source for 3.4
survives; the work began from the nearest 3.6 sources and moved back.

A first pass in March 2026 read every function against the
disassembly and judged them all correct. Compiling that source in June
proved otherwise. The byte-exact campaign took the game from 80
matching functions to 139 to all 145, and the whole file matched on
3 July. The last difference was a single rounding bit in a
floating-point constant in the C library.

The rebuilt game was then played against the original under a PDP-11
simulator with the same random seed: 28 of 28 opening dungeons were
identical, and more than 350 turns ran with no divergence.

See [What the binaries told us](../story/findings.md) for the bugs and
oddities the rebuild uncovered, including the 1981 *Guide to the
Dungeons of Doom*, whose source was rebuilt the same way.

## Repository

<https://github.com/rogueforge/rogue3.4>. The `restored` branch and the
`19810521-bsd28` tag hold the rebuild of the 2.8BSD binary of 21 May 1981.
