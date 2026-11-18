---
glyph: glyph-question
summary: From a file in a 1981 BSD distribution tree to C source that compiles back into it, and how we know when it does.
---
# How a version is rebuilt

<ol class="steps">
<li><strong>Find the binary.</strong> Take the executable or object file from a dated distribution, such as Rogue 3.4 from 2.8BSD or Rogue 5.3 from 4.2BSD.</li>
<li><strong>Read the machine code.</strong> Disassemble and decompile it with Ghidra and radare2, after fixing their PDP-11 and VAX support well enough to trust.</li>
<li><strong>Write the C.</strong> Start from the closest surviving source, then change it function by function until each one compiles to the instructions in the binary.</li>
<li><strong>Prove it.</strong> Build with the original compiler, assembler and linker, ported to modern Linux, and compare the whole file. Done means the checksums match.</li>
</ol>

## Finding the binary

Most of the targets come from Disc 1 of the CSRG Archive CD-ROMs, which
preserve Berkeley's own distribution trees. The 4.1BSD copy of Rogue 3.6
comes from The Unix Heritage Society's reconstruction of that release.

The binaries differ in how much help they give. Rogue 3.4 is fully
stripped: 70,364 bytes of PDP-11 code with no symbol names at all. The
3.6, 4.22 and 5.2 binaries keep between 1,600 and 2,000 symbols, so
every function and global variable arrives with its name. Rogue 5.4 is
an object file with its symbols stripped, which keeps the relocations
that say where each call goes.

## Reading the machine code

Three disassemblers were used side by side: the GNU `objdump` for the
PDP-11, radare2, and Ghidra running headless. None of them handled these
machines well at first, and each needed fixing:

- **radare2's PDP-11 decoder** read instructions through a four-byte
  buffer, too small for the longest PDP-11 instructions, which take six.
- **Ghidra's PDP-11 description** did not understand the `csv` and `cret`
  routines that every compiled C function calls on entry and exit, nor
  the floating-point instruction set, nor several addressing modes.
  After the fixes, clean decompiles of Rogue 3.4 went from none of its
  145 functions to 144.
- **Ghidra's VAX description** needed four corrections to its
  instruction semantics, and a script that repaired 2,145 relocations in
  the 5.4 object file. That recovered 234 functions and named 270
  globals.

The decompiled C is a guide, never an answer. Ghidra regularly got
argument counts wrong, misread stack frames, and moved code out of loops
in ways the 1981 compiler never would.

## Writing the C

Rebuilding starts from the closest of the three source trees that
survive near their versions: the site copies of Rogue 3.6, the Illinois
copy of Rogue 5.2, and Ken Arnold's Rogue 5.4. The versions in between
start from a neighbour; Rogue 3.4, for example, began as the 3.6 source
cut down and moved back. Then each function
is compiled on its own and compared with the binary, instruction by
instruction, with addresses masked out so that one function can match
before its neighbours do.

That is where period compilers show their personality. The PDP-11
compiler generates different code for `while (1)` than for `for (;;)`.
The VAX compiler picks registers in an order that depends on how
variables are declared. A chained assignment, or the order of two
declarations, can move a byte. Matching a function often means finding
the one way of writing it that the original author happened to choose.

## Proving it

The test is the whole file. The rebuilt source is compiled and linked
with the original toolchain, and the result is compared with the
binary from the tape by checksum. Two details are allowed for and stated
wherever they apply:

- Some tape copies are missing the zero padding that the linker adds at
  the end of the file, so the comparison covers the length on the tape.
- Rogue 5.4's `main.obj` survives with its symbols stripped, so the
  rebuild is stripped the same way before comparing.

The toolchains themselves are tested too. The 2.8BSD compiler was proven
by running the original 1981 compiler, assembler and linker under a
PDP-11 simulator and checking that they produce the same output as the
ported versions. More on that under [the toolchains](toolchains.md) and
[the simulators](simulators.md).

A matching file is not quite the end. The rebuilt Rogue 3.4 was also
played against the original with the random number generator seeded the
same way: 28 of 28 opening dungeons were identical, and more than 350
turns of play ran without any difference.

## Results

| Binary | Result |
|---|---|
| Rogue 3.4, 2.8BSD PDP-11 | Byte-identical |
| Rogue 3.6, 4.1BSD VAX | Byte-identical |
| Rogue 3.6, 2.9BSD PDP-11 | Byte-identical |
| Rogue 3.6, 2.9BSD PDP-11, overlaid | Code and data identical; 49 symbol table entries differ |
| Rogue 4.22, 4.1aBSD VAX | Byte-identical |
| Rogue 5.2, 4.1BSD VAX | Byte-identical |
| Rogue 5.3, 4.2BSD VAX, object file | Byte-identical, including symbol and string tables |
| Rogue 5.3, 4.2BSD VAX, installed game | Byte-identical |
| Rogue 5.4, 4.3BSD VAX, `main.obj` | Identical after stripping, with two small patches applied after compiling |

The remaining differences are reported as they are. For Rogue 5.4, two
spots still need patching by hand after the compiler runs: the exit from
`do_move()` and six bytes of register choice in `command()`. Closing
them probably needs a slightly different build of the 1985 compiler than
the one we have.
