---
short: Rogue 5.3
year: 1983
machine: VAX
status: rebuilt
summary: The Rogue of 4.2BSD, rebuilt to match both its distributed object file and the installed game, symbol table and all.
released: 2 August 1983
origin: 4.2BSD, distmod.obj and /usr/games/rogue (CSRG Archive, Disc 1)
toolchain: 4.2BSD VAX C compiler
verified: Byte-identical, 13 July 2026
repo: rogue5.3-19830802-bsd42
---
# Rogue 5.3

The copy of Rogue 5.3 found in the 4.2BSD tree, from 1983, is a
pre-compiled object file, `distmod.obj`, with a small machine-dependent
source file for each site to compile and link against it.

## The 2026 rebuild

The rebuild matches both forms. The 129,205-byte `distmod.obj` is
identical, including its symbol and string tables, which record every
local variable and the names of the object files it was built from. The
installed `/usr/games/rogue` from 4.2BSD is identical too.

Matching the symbol table meant reproducing details that do nothing at
run time: four declarations that exist only to take symbol slots, an
unused string `after signal`, and object files that carry names from
Berkeley's Berknet network software, such as `terminal.o` and
`network.o`, recorded by the linker. The rebuild
also keeps two genuine bugs: a call to `printw(0, 0, ...)` written as
though it were `mvprintw`, and a pointer to a local variable that
outlives its function.

## Repository

<https://github.com/rogueforge/rogue5.3-19830802-bsd42>
