---
glyph: glyph-bracket
summary: The restart was done by one person working with Claude. What the model did, what the person did, and the rule that kept it honest.
---
# Working with Claude

The 2026 restart was carried out by Nicholas J. Kisseberth working with
Claude Code, Anthropic's coding agent. Over the year it ran on a
succession of Claude models: Claude Opus 4.6 and 4.8 early on, then
Claude Fable 5, and Claude Opus 5.5 for the Linux ports. How much those
upgrades mattered is its own story: [Waiting for better models](models.md). Most of the
commits in the toolchain and port repositories are co-authored by
Claude, and the working transcripts for Rogue 3.4 alone run to about
96 MB.

## What Claude did

The work suits a patient reader. Each version of Rogue is a few hundred
functions of machine code, and each function has to be read, rewritten
in C, compiled, compared and rewritten again until it matches. Claude
did most of that loop:

- reading PDP-11 and VAX disassembly and Ghidra's decompiler output;
- writing and revising C until a function compiled to the same
  instructions;
- writing the comparison tools that check one function, or one file,
  against the original;
- porting the old compilers and libraries to 64-bit Linux, and finding
  where they still differed from the originals;
- writing the Ghidra scripts that repaired relocations and named
  symbols.

Larger jobs were split among several Claude agents running in parallel,
each in its own copy of the source, with the results checked and merged.

## What the person did

The person running the work chose the targets, judged evidence, and
held to the rule that only a compiled match counts. Knowledge of the
history mattered too: which of the surviving 3.6 copies is older than
its file dates suggest, for example, or which library a 1981 binary was
likely linked against.

## Convinced is not proven

The most important lesson came early. In March, Claude read through all
145 functions of Rogue 3.4 and reported each one verified against the
disassembly. The reading was careful and the report was confident. When
the source was compiled and compared in June, it was wrong in dozens of
places.

> Reading disassembly convinces; only recompiling proves.

After that, nothing counted unless it compiled to the same bytes. Where
a match is incomplete, as with the symbol table of the overlaid Rogue
3.6 or the two patched spots in Rogue 5.4, the records say so rather than
round the result up.

## Why it matters

Reconstructing source this way used to be possible only in principle.
It takes thousands of small, exact steps, and few people have had the
time to take them for a 1981 game. With a model doing the reading and
recompiling, and a person setting the standard, six versions of Rogue
went from binary to proven source in a few months.
