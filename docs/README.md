## Why we started over

RogueForge has restored Rogue and its descendants since the early 2000s.
Those restorations began from source code that happened to survive:
copies passed between sites, edited, ported and edited again. None of
them could say for certain what the code that Berkeley compiled in 1981
actually looked like.

In 2026 the Rogue Restoration Project went back to first principles.
Three source trees survive that are likely close to their versions:
Rogue 3.6, 5.2 and 5.4. And the programs themselves survive: the BSD
distribution trees kept on Kirk McKusick's CSRG archive discs and at
The Unix Heritage Society hold copies of the original executables. Start from the
nearest source tree. Work out what the binary says it really was. Prove
it by compiling with the compilers of the day and getting the same file,
byte for byte. [Read the whole story](story/starting-over.md).

## How a version is rebuilt

<ol class="steps">
<li><strong>Find the binary.</strong> Take the executable or object file from a dated distribution, such as Rogue 3.4 from 2.8BSD or Rogue 5.3 from 4.2BSD.</li>
<li><strong>Read the machine code.</strong> Disassemble and decompile it with Ghidra and radare2, after fixing their PDP-11 and VAX support well enough to trust.</li>
<li><strong>Write the C.</strong> Start from the closest surviving source, then change it function by function until each one compiles to the instructions in the binary.</li>
<li><strong>Prove it.</strong> Build with the original compiler, assembler and linker, ported to modern Linux, and compare the whole file. Done means the checksums match.</li>
</ol>

Claude did most of the reading, rewriting and recompiling, working
alongside a person who decided what counted as evidence.
[How that worked](story/working-with-claude.md).

## Where things stand

| Version | Rebuilt from | Result |
|---|---|---|
| [Rogue 3.4](games/rogue-3-4.md) | 2.8BSD, PDP-11, May 1981 | Byte-identical |
| [Rogue 3.6](games/rogue-3-6.md) | 4.1BSD, VAX, October 1981 | Byte-identical |
| | 2.9BSD, PDP-11, March 1983 | Byte-identical |
| [Rogue 4.22](games/rogue-4-22.md) | 4.1aBSD, VAX, March 1982 | Byte-identical |
| [Rogue 5.2](games/rogue-5-2.md) | 4.1BSD last tape, VAX, July 1982 | Byte-identical |
| [Rogue 5.3](games/rogue-5-3.md) | 4.2BSD, VAX, August 1983 | Byte-identical, symbol table included |
| [Rogue 5.4](games/rogue-5-4.md) | 4.3BSD, VAX, January 1986 | Identical code, after two small patches |

Every rebuilt version has its own repository under
[github.com/rogueforge](https://github.com/rogueforge), named for the
date and system of the binary it matches.
