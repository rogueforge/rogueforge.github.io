---
glyph: glyph-paren
summary: A rebuild is only proven if it compiles with the compiler that made the original. So the compilers of 1981 to 1985 had to be rebuilt first.
---
# Rebuilding the toolchains

A checksum match only means something if the compiler is the one Berkeley
used. Modern C compilers produce entirely different code, so each version
of Rogue needs its own period toolchain: the compiler, the optimizer, the
assembler, the linker and the C library, as they stood on the day the game
was built. None of them had run on a modern machine. All of them had to be
rebuilt from the original BSD sources before a single Rogue function could
be proven.

## The rule: porting fixes only

Every tool is built from authentic BSD sources and ported to 64-bit Linux.
The rule throughout was that ported tools get porting fixes only. Code that
assumed a 16-bit `int`, or a pointer that fits in one, is fixed so it works
on a modern machine. Nothing that changes what the tool outputs is touched.

The libraries matter as much as the compiler. Rogue 3.4 turned out to be
linked against a pre-release snapshot of the 2.8BSD library, not the one
that was released, and all 121 library routines in the binary had to match
as well as the game's own 145. The C library, curses and termcap were the
first things to match exactly, in June, and from then on the compiler could
be trusted.

## The PDP-11: Ritchie's compiler

The PDP-11 work began in June with Rogue 3.4. Its compiler is Dennis
Ritchie's, in its three passes `c0`, `c1` and `c2`, ported from the 2.8BSD
sources, with the assembler reimplemented in C and the linker, archiver and
libraries alongside. A 2.9BSD toolchain followed for Rogue 3.6, with the
overlays the PDP-11 needed to fit a game that size.

The proof that the port changed nothing came from the original tools
themselves. Run under the [simulator](simulators.md), the native 1981
compiler and assembler produce exactly the same output as the ported ones.

## The VAX: the Portable C Compiler

The VAX work began in the spring with Rogue 5.3 and 5.4, and grew into
toolchains for 4.1, 4.2 and 4.3BSD. The VAX compiler is Steve Johnson's
Portable C Compiler. Its output changed often while Berkeley worked on it,
so the same source compiles differently from one release to the next, and
each version of Rogue needs the compiler of its own moment. Rogue 3.6 on the
VAX needed 1981-era fixes to its libraries as well, including a genuine
1981 bug in the curses routine `getcap`.

## Dating a compiler

Rogue 5.4 needed a compiler that never shipped. Neither the compiler
released with 4.2BSD nor the one released with 4.3BSD reproduces its code
exactly. Two dated changes in the compiler's source fix the window: one in
`order.c` from 18 January 1985 that the game's code reflects, and one in
`table.c` from 10 December 1985 that it does not. A compiler rebuilt from
Berkeley's sources as of 19 March 1985 matches 232 of the game's 234
functions on its own. That agrees with the only date in the binary, the
version string `rogue 31/03/85`.

## One toolchain for every Unix

By August the tools had outgrown Rogue. Each machine's toolchains were
merged into one, chosen with a single `--universe` flag:

- [**pdp11-xdev**](https://github.com/nyxcraft/pdp11-xdev) targets every
  PDP-11 Unix from the First Edition of 1971 through 2.11BSD, System III
  and DEC's Ultrix-11. One C library serves them all, choosing the right
  system calls for each era when a program is linked. Its test suites run
  the original 1981 and 1983 tools and compare the results to the byte, all
  the way to a byte-identical overlaid kernel.
- [**vax11-xdev**](https://github.com/nyxcraft/vax11-xdev) does the same
  for the VAX, from 32V and 3BSD through 4.4BSD, System V, the Research
  editions, Ultrix and NetBSD. VAX floating point, in all four of its
  formats, is done in software, bit for bit.

The first toolchains, built just for Rogue, are kept as they were:
[pdp11-bsd28-toolchain](https://github.com/rogueforge/pdp11-bsd28-toolchain)
for Rogue 3.4 and
[vax-bsd42-toolchain](https://github.com/rogueforge/vax-bsd42-toolchain)
for Rogue 5.3.
