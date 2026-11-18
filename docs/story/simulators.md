---
glyph: glyph-plus
summary: A cross toolchain needs proof that it is right, and that means running the original 1981 compiler. apsim runs it, on a modern machine, as an ordinary command.
---
# Building the simulators

To check a rebuilt compiler against the original, to play a rebuilt Rogue
against the one on the tape, or just to watch a 1981 program run, you need
a PDP-11 or a VAX. Nobody has those on their desk any more. So the restart
built them, in software, as two simulators that both go by the name
`apsim`.

## Why the cross toolchains weren't enough

A cross toolchain turns C into PDP-11 or VAX code on a modern machine. That
is half of what a rebuild needs. The other half is knowing the cross
toolchain is right. A ported compiler that is off by one register choice
would happily produce a "match" that the real 1981 compiler never would,
or miss one it would have made. The only proof that the port is faithful is
to run the original compiler on the same input and compare. That means
running PDP-11 and VAX programs.

The obvious way to do that is SIMH, which emulates the whole machine and
boots a real Unix from a disk image. In practice it was a poor fit. Every
Unix release needs its own installed and bootable disk image, and this work
touched many of them: 2.8 and 2.9BSD on the PDP-11; 4.1, 4.1a, 4.2 and
4.3BSD on the VAX. Getting files into each one and results back out, and
doing it thousands of times in an automated loop, was slow and fragile.

## Machines in user mode

So the restart built something smaller. `apsim` is a *user-mode*
simulator, in the spirit of Apout and qemu-user: it emulates the processor,
and when the program asks the Unix kernel for something (open a file, read
the terminal, start a process) it hands the request to Linux. A PDP-11 or
VAX program runs as an ordinary command, in a terminal window, next to
everything else.

No disk images, no booting, no copying files in and out: one simulator
runs the programs of any of those systems, chosen by a flag. That turns the
old binaries into tools again. The original compilers can be run and their
output compared with the ported ones, as a step in every test run. The original Rogue
can be played next to the rebuilt one. And the rebuilt toolchains' own
programs can be run, to check that what they build actually works.

## The PDP-11

The PDP-11 `apsim` grew up alongside the 2.8BSD toolchain in June and July.
It handles the PDP-11's separate instruction and data spaces, overlays, the
2.8BSD system calls, and a terminal good enough for curses: Rogue plays in
it.

Its floating point is the PDP-11's own, bit for bit: true 56-bit arithmetic
with the FP11's rounding rule, not the host computer's doubles. That
mattered. The very last byte of Rogue 3.4 to fall into place was a rounding
difference in one constant, `.03`, in the C library, and only a faithful
FP11 could settle it.

With it, the toolchain was checked against itself. The native June 1981
compiler and assembler run under `apsim`, and their output matches the
ported tools byte for byte. And the rebuilt Rogue 3.4 was played against the
original, with the random number generator seeded the same way: 28 of 28
opening dungeons were identical, and more than 350 turns ran without a
difference.

It goes further back than Rogue, too. Given a First Edition binary from
1971, `apsim` switches to that system's conventions, and the three First
Edition programs that survive run correctly.

## The VAX

The VAX `apsim` started out running programs from the 4.1BSD tapes. It
grew, era by era, until it ran the unmodified NetBSD 10 userland for the
VAX, with dynamic linking, threads, job control and `gdb`. Its signal
handling follows each era's rules, its sockets pass through to the host's,
and its floating point, like the PDP-11's, is bit-exact in software.

The assembler, the disassembler and the simulator share one table of the
VAX instruction set, so all three agree on every instruction. That is how
one of the best bugs of the whole project turned up.

## The bug in the 1981 assembler

The genuine Rogue from a Berkeley tape ran under `apsim`: it dug a dungeon
and drew the level. Then it walked off the end of an array and into the
memory allocator.

The cause was a typo in Berkeley's own operand table for the assembler,
which lists the destination of `mnegw`, a 16-bit instruction, as a 32-bit
operand. The assembler never noticed, because an operand's size doesn't
change the bytes it assembles. But a simulator uses it as the step through
an indexed array, so `mnegw` strode four bytes at a time instead of two.

The table is kept exactly as it was on the tape, typo and all. The
simulator corrects it in its own copy.

## Where they live

Each simulator is part of its machine's toolchain:
[pdp11-xdev](https://github.com/nyxcraft/pdp11-xdev) for the PDP-11 and
[vax11-xdev](https://github.com/nyxcraft/vax11-xdev) for the VAX.
