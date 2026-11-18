---
glyph: amulet
summary: Forty-five years of Rogue, from a game written at Santa Cruz in 1980 to the rebuilds of 2026, and how the versions are related.
---
# History

<div class="t-legend">
<span class="status status--written">A version is written</span>
<span class="status status--restored">The project restores something</span>
<span class="status status--rebuilt">A version is rebuilt from its binary</span>
</div>

## Writing Rogue, 1980–1992

<ol class="timeline">
<li><span class="t-year">1980</span><ul>
<li class="ev ev--written">Michael Toy and Glenn Wichman write the first Rogue at UC Santa Cruz.</li>
</ul></li>
<li><span class="t-year">1981</span><ul>
<li class="ev ev--written"><a href="../games/rogue-3-4/">Rogue 3.4</a> is linked for the PDP-11 on 21 May, and turns up in 2.8BSD.</li>
<li class="ev ev--written"><a href="../games/rogue-3-6/">Rogue 3.6</a> goes out with 4.1BSD for the VAX, and later 2.9BSD for the PDP-11. Copies spread to sites everywhere.</li>
</ul></li>
<li><span class="t-year">1982</span><ul>
<li class="ev ev--written"><a href="../games/rogue-4-22/">Rogue 4.22</a> in March, then <a href="../games/rogue-5-2/">Rogue 5.2</a>, the start of the 5.x line, at Berkeley with Ken Arnold.</li>
<li class="ev ev--written"><a href="../games/super-rogue-9-0/">Super-Rogue</a> grows out of Rogue 3.6 at Bell Labs, with Robert Kindelberger, through 1984.</li>
</ul></li>
<li><span class="t-year">1983</span><ul>
<li class="ev ev--written"><a href="../games/pc-rogue-1-48/">PC Rogue</a>'s first beta from A.I. Design, grown from Rogue 5.2, with a new set of monsters.</li>
<li class="ev ev--written"><a href="../games/rogue-5-3/">Rogue 5.3</a> in August, found in 4.2BSD, with the same new monsters.</li>
</ul></li>
<li><span class="t-year">1984</span><ul>
<li class="ev ev--written"><a href="../games/advanced-rogue-5-8/">Advanced Rogue</a> begins at AT&amp;T, built on Rogue 3.6 with ideas from Super-Rogue.</li>
<li class="ev ev--written"><a href="../games/rogomatic/">Rog-O-Matic</a>, from Carnegie Mellon, plays Rogue better than most people.</li>
</ul></li>
<li><span class="t-year">1985</span><ul>
<li class="ev ev--written"><a href="../games/rogue-5-4/">Rogue 5.4</a>, its version string dated 31 March, later found with 4.3BSD.</li>
<li class="ev ev--written">Epyx sells PC Rogue; version 1.48 is dated 30 December.</li>
<li class="ev ev--written">Herb Chong writes <a href="../games/ultrarogue-1-07/">UltraRogue</a>, from an early Advanced Rogue, through 1986.</li>
</ul></li>
<li><span class="t-year">1986</span><ul>
<li class="ev ev--written"><a href="../games/advanced-rogue-7-7/">Advanced Rogue 7.7</a>, the last of the line.</li>
</ul></li>
<li><span class="t-year">1989</span><ul>
<li class="ev ev--written">Robert Pietkivitch begins <a href="../games/xrogue-8-0/">XRogue</a> for the AT&amp;T UNIX PC, from Advanced Rogue 7.7, through 1992.</li>
</ul></li>
</ol>

## Keeping it alive, 1992–2026

<ol class="timeline">
<li><span class="t-year">1992</span><ul>
<li class="ev ev--restored">Herb Chong sends the UltraRogue source. Bringing it up to ANSI C is the project's first restoration.</li>
</ul></li>
<li><span class="t-year">1996</span><ul>
<li class="ev ev--restored">Robert Pietkivitch sends the XRogue source, and helps bring it back to life.</li>
</ul></li>
<li><span class="t-year">2000</span><ul>
<li class="ev ev--restored">The project opens on SourceForge.</li>
</ul></li>
<li><span class="t-year">2002</span><ul>
<li class="ev ev--restored">Ken Arnold publishes his Rogue 5.4 source on SourceForge.</li>
<li class="ev ev--restored">Robert Pietkivitch dies on 3 December, before he could send the XRogue changes he had made since.</li>
</ul></li>
<li><span class="t-year">2004</span><ul>
<li class="ev ev--restored">Robert Kindelberger provides the long-lost Super-Rogue 9.0 source. rogueforge.net goes live.</li>
</ul></li>
<li><span class="t-year">2005</span><ul>
<li class="ev ev--restored">Super-Rogue 9.0-1 and UltraRogue 1.0.7 released.</li>
</ul></li>
<li><span class="t-year">2006</span><ul>
<li class="ev ev--restored">Advanced Rogue 5.8.2 and 7.7.1 released.</li>
</ul></li>
<li class="t-redux"><span class="t-year">2026</span><ul>
<li class="ev ev--restored">March: <a href="../story/">Redux</a> begins. Ghidra and radare2 are fixed for the PDP-11 and VAX, and every version is decompiled.</li>
<li class="ev ev--rebuilt">2 April: Rogue 5.4's object file matches, with two small patches. Then the work stalls for seven weeks.</li>
<li class="ev ev--restored">June: Claude Opus 4.8, then on 12 June Claude Fable 5. The 2.8BSD toolchain and simulator are built, and the stalled problems start to give. Late in June Fable is withdrawn for a while, and the work <a href="../story/models/">waits for it</a>.</li>
<li class="ev ev--rebuilt">3 July: Rogue 3.4 matches byte for byte, with a rebuilt 2.8BSD toolchain.</li>
<li class="ev ev--rebuilt">5 July: Rogue 3.6 for the PDP-11. Then, in July, Rogue 3.6 for the VAX and Rogue 4.22.</li>
<li class="ev ev--rebuilt">13 July: Rogue 5.3, object file and installed game. 19 July: Rogue 5.2.</li>
<li class="ev ev--restored">August: the PDP-11 and VAX tools become <a href="../story/toolchains/">pdp11-xdev and vax11-xdev</a>, toolchains and simulators for every Unix of their machines.</li>
<li class="ev ev--restored">November: Claude Fable 5.2 and Opus 5.5 get the stuck Linux ports moving; all six Berkeley versions are ported in a week. PC Rogue and Rog-O-Matic are next.</li>
</ul></li>
</ol>

## How the versions are related

Rogue was worked on at Santa Cruz and Berkeley, at A.I. Design for the
IBM PC, and at Bell Labs, by people who shared some of their work with
each other and not the rest. The rebuilt sources show which.

- **Rogue 3.6 → 4.22 → 5.2** is a straight line.
- **Rogue 5.3 grew from 5.2**, and **Rogue 5.4 grew from 5.3**.
- **PC Rogue grew from 5.2**, not from 5.4, though it was sold in the
  same years as 5.4.
- **PC Rogue and 5.3 share one batch of work**: a new set of monsters
  and a few new items. Each side then changed its copy.
- **Rog-O-Matic** is not part of the family. It plays Rogue; it was
  distributed to play Rogue 3.6 and 5.2.

### The evidence

Two comparisons, run over the rebuilt source of each Berkeley version
and the original A.I. Design source of PC Rogue 1.48.

**Function by function.** For every function two versions write
differently, which one is a third version closer to? Comments, layout
and local variable names are ignored, so this measures what the code
does. For the rebuilt versions, that is fixed by the binary.

| Question | First | Second |
|---|---|---|
| Is 5.2 closer to 3.6 or to 4.22? | 0 | 131 |
| Is 5.4 closer to 5.2 or to 5.3? | 4 | 147 |
| Is PC Rogue closer to 5.2 or to 5.3? | 115 | 12 |
| Is PC Rogue closer to 4.22 or to 5.2? | 5 | 38 |

**String by string.** Every message, name and prompt, checked for which
versions have it. For the rebuilt versions these are exactly the strings
in the surviving binaries.

| Found in | Strings | For example |
|---|---|---|
| 5.2 and PC Rogue only | 49 | crossbow, blank paper, "yum, that tasted good" |
| 5.3, 5.4 and PC Rogue, not 5.2 | 15 | aquator, griffin, jabberwock, quagga, xeroc |
| 5.3 and 5.4, not PC Rogue | 147 | hallucination, levitation, protect armor |
| 5.4 only | 52 | "pick something up" |
| 5.4 and PC Rogue only | 0 | |

### Rogue 5.4 and 5.3

Where 5.2 and 5.3 differ, Rogue 5.4 sides with 5.3 almost every time.
The exceptions are the score file. Rogue 5.3 reworked how scores were
kept and listed; in 5.4 the routine that opens the score file is
identical to 5.2's, and the one that records a score is closer to 5.2's
than to 5.3's. Rogue 5.4 also adds things neither 5.3 nor PC Rogue
has: a command to repeat the last command, one to pick things up, and a
mystery trap.

### What PC Rogue and 5.3 shared

PC Rogue's code is 5.2's. It keeps 5.2's wording, crossbows, potions of
paralysis and thirst quenching, and scrolls of blank paper, and has none
of 5.3's new potions and scrolls. Yet it has the new monster list that
appears at Berkeley in 5.3: the aquator, griffin, ice monster,
jabberwock, kestrel, medusa, phantom, quagga, rattlesnake, venus flytrap
and xeroc, along with the scroll of food detection and the poison dart
trap. A few pieces of code, such as how timed events are kept, are
written the same way in both.

The lists are not identical. PC Rogue has a **slime** where Berkeley has
a **snake**, an **ur-vile** where Berkeley has a **black unicorn**, and
spells the bird "kestral" where Berkeley has "kestrel".

Which side wrote the new monsters first is not settled. Two clues point
to the PC: its earliest surviving build, a 1983 beta, already has them,
and Rogue 5.3 dates from August 1983. And "kestrel" reads like a
correction of "kestral", not the other way round.

## Where they were found

No one institution kept Rogue. Most of the binaries come from Kirk
McKusick's [CSRG Archive](http://www.mckusick.com/csrg/) CD-ROMs, which
preserve Berkeley's own distribution trees, and from
[The Unix Heritage Society](https://www.tuhs.org/Archive/Distributions/UCB/).

| Version | Found in | Rebuilt |
|---|---|---|
| Rogue 3.4 | 2.8BSD | 2026 |
| Rogue 3.6 | 4.1BSD (TUHS); 2.9BSD; 2.9pucc | 2026 |
| Rogue 4.22 | 4.1aBSD | 2026 |
| Rogue 5.2 | 4.1BSD last tape; 4.1c.2BSD | 2026 |
| Rogue 5.3 | 4.2BSD | 2026 |
| Rogue 5.4 | 4.3BSD, object file only; 2.10BSD | 2026 |

Source came from FTP archives that are mostly gone now:
`emx.utexas.edu` for the BRL copy of Rogue 3.6, `uxc.cso.uiuc.edu` for
Rogue 5.2 in the early 1990s, and `robot-club.com` for Rogue 5.2 with
Rog-O-Matic.

## The people who kept it alive

Several versions exist only because someone kept a copy and sent it in.

<ol class="inventory">
<li><strong>Aydin Edguer</strong>: the NMT copies of Rogue 3.6 and 5.2.</li>
<li><strong>Herb Chong</strong>: the UltraRogue source, in 1992.</li>
<li><strong>Robert Pietkivitch</strong> (1955–2002): the XRogue source, in 1996, and years of encouragement.</li>
<li><strong>Robert D. Kindelberger</strong>: the Super-Rogue 9.0 source, in 2004.</li>
<li><strong>Ken Arnold</strong>: the Rogue 5.4 source, released on SourceForge.</li>
</ol>

The project itself ran on SourceForge from 2000, then on its own Trac
and Subversion server at rogue.rogueforge.net, and since 2026 on
[GitHub](https://github.com/rogueforge).
