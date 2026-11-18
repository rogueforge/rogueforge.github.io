---
glyph: glyph-percent
summary: For twenty years RogueForge restored Rogue from whatever source survived. In 2026 the Rogue Restoration Project went back to first principles.
---
# Starting over

## The first restoration

RogueForge began with UltraRogue. Herb Chong sent his source in 1992,
and over the next few years it was brought up to ANSI C and given new
code to save and restore a game. XRogue followed in 1996, from Robert
Pietkivitch, and Super-Rogue in 2004, from Robert Kindelberger. A
SourceForge project opened in 2000, then the rogueforge.net site, then a
Trac and Subversion server that carried the work for two decades.

Each of those restorations started from source somebody had kept. That
was the only way to do it, and it produced games people could play. It
also left questions nobody could answer. The Rogue 3.6 sources that
survive came from half a dozen sites and dates, between January 1982
and June 1984, and they disagree.
Which one is the game Berkeley released? Were any of them compiled
unchanged? For Rogue 4.22 and 5.3 there was almost nothing to start from.

## What survived

Two kinds of evidence survive, and the restart uses both.

The first is source. Three trees are likely to be close to the versions
they claim to be: **Rogue 3.6**, from the several site copies; **Rogue
5.2**, from the University of Illinois FTP archive; and **Rogue 5.4**, as
Ken Arnold later released it. None is guaranteed to be exactly what
Berkeley compiled, but each is a strong starting point, and the versions
between them can be worked out by moving forward or back from the
nearest one.

The second is the programs themselves, with provenance better than any
source tree's. Copies of Rogue turn up in Berkeley's BSD distribution
trees, preserved on the CSRG archive CD-ROMs and at The Unix Heritage
Society:

- Rogue 3.4 in 2.8BSD, linked on 21 May 1981 for the PDP-11.
- Rogue 3.6 in 4.1BSD for the VAX, and twice more in 2.9BSD for the
  PDP-11.
- Rogue 4.22 in 4.1aBSD, March 1982.
- Rogue 5.2 on the last 4.1BSD tape, July 1982.
- Rogue 5.3 in 4.2BSD, as both a distributed object file and the
  installed game.
- Rogue 5.4 in the 4.3BSD source tree, as a
  stripped object file, `main.obj`, with only its machine-dependent
  code as source.

Every one of these is a fixed point. Start from the nearest source
tree, change it until the period compiler turns it into exactly this
file, and you have the source as it was, whatever the surviving copies
say.

## The new standard

That became the rule for the restart: a version counts as restored when
its rebuilt source compiles, with the original toolchain, to a file
whose checksum matches the one on the tape. Reading the disassembly and
agreeing with it is not enough. As the 3.4 notes put it, *reading
disassembly convinces; only recompiling proves.*

The standard is strict on purpose. In March 2026 a first pass over Rogue
3.4 marked all 145 of its functions verified by reading. When the source
was finally compiled in June, the byte-for-byte comparison found dozens
of places where it was wrong. Every result on this site comes from the
second kind of check.

## The work, in brief

- **March 2026.** Ghidra and radare2 are taught enough PDP-11 and VAX to
  decompile every version. The Rogue 5.4 `main.obj` is the first to
  come close, on 2 April.
- **June and July.** Rogue 3.4 matches on 3 July, after the 2.8BSD
  compiler is rebuilt and proven against itself. Rogue 3.6 follows on
  both machines, then 5.3, 5.2 and 4.22.
- **November.** The rebuilt sources become the base for new Linux
  ports, with fixes for the bugs a modern system exposes.

The [method](method.md) describes each step, and the
[findings](findings.md) collect what the binaries revealed about the
code their authors wrote.

## What we don't do

- We are not writing a new roguelike. Where a version's gameplay differs
  from its parent, as UltraRogue's does, that comes from its original
  author, not from us.
- We don't round results up. If a rebuild matches everything but a
  symbol table, the page for that version says so.
- Fixes for modern systems go in the ports, as separate changes, never
  in the rebuilt source.
