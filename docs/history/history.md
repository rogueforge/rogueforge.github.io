---
glyph: amulet
summary: Forty-five years of Rogue, from a game written at Santa Cruz in 1980 to the rebuilds of 2026.
---
# History

<div class="t-legend">
<span class="status status--written">A version is written</span>
<span class="status status--restored">The project restores something</span>
<span class="status status--rebuilt">A version is rebuilt from its binary</span>
</div>

## Writing Rogue, 1980–1989

By Glenn Wichman's count Rogue has four creators: Michael Toy and Wichman,
who wrote it at Santa Cruz; Ken Arnold, who worked on it with Toy at
Berkeley; and Jon Lane, who made the PC version with Toy at A.I. Design.
He named them as "the rogue people" as early as 1984
([Usenet post](../talks/wichman-usenet-1984.md)) and "the four of us responsible for Rogue" in 2007
([interview](../talks/wichman-roguetemple-2007.md)), and the four have never all been in the
same room ([interview, 2021](../talks/wichman-interview-2021.md)), though three of
them shared a stage at the 2016 Roguelike Celebration
([panel](../talks/rogue-panel-2016.md)).

<ol class="timeline">
<li><span class="t-year">1980</span><ul>
<li class="ev ev--written">17 July: the earliest dated papers of Ken Arnold's curses library, in 2.79BSD.</li>
<li class="ev ev--written">In the fall, Michael Toy and Glenn Wichman write the first Rogue at UC Santa Cruz, in the apartment they share, on the campus PDP-11/70 and with Ken Arnold's curses library; Wichman names it. It is the most popular game on campus before it even has monsters (<a href="../talks/wichman-usenet-1984/">Wichman, 1984</a>), and goes through a series of early versions.</li>
</ul></li>
<li><span class="t-year">1981</span><ul>
<li class="ev ev--written">In January 1981 Michael Toy moves to UC Berkeley, and Ken Arnold, whose curses Rogue is built on, seeks him out and joins the team. Wichman keeps his own copy going at Santa Cruz for a while (<a href="../talks/wichman-history-1997/">Wichman, 1997</a>).</li>
<li class="ev ev--written">A Rogue binary reaches Bell Labs, where it is played as "UBL", for "Under Bell Labs" (<a href="https://www.youtube.com/watch?v=4IkrZkUV01I&amp;t=1177s">Toy, 2016</a>).</li>
<li class="ev ev--written"><a href="../games/rogue-3-4/">Rogue 3.4</a> is built for the PDP-11 on 21 May and turns up in 2.8BSD: the earliest version that survives with a number and a date.</li>
<li class="ev ev--written"><a href="../games/rogue-3-6/">Rogue 3.6</a> goes out with 4.1BSD for the VAX, and later 2.9BSD for the PDP-11. Copies spread to sites everywhere.</li>
<li class="ev ev--written">In the fall Michael Toy moves to Italy to work for Olivetti, and goes on working on Rogue from there.</li>
<li class="ev ev--written">At Carnegie Mellon, Andrew Appel, Leonard Hamey, Guy Jacobson and Michael Mauldin begin <a href="../games/rogomatic/">Rog-O-Matic</a>, a program that plays Rogue.</li>
</ul></li>
<li><span class="t-year">1982</span><ul>
<li class="ev ev--written"><a href="../games/rogue-4-22/">Rogue 4.22</a> is built at Berkeley on 13 March, and turns up in 4.1aBSD.</li>
<li class="ev ev--written"><a href="../games/rogue-5-2/">Rogue 5.2</a>, the start of the 5.x line, is built at Berkeley with Ken Arnold on 20 July, and goes out on the last 4.1BSD tape.</li>
<li class="ev ev--written">26 September: <a href="../games/rogomatic/">Rog-O-Matic</a> becomes a total winner for the first time, at Rogue 3.6 at Carnegie Mellon.</li>
</ul></li>
<li><span class="t-year">1983</span><ul>
<li class="ev ev--written">In January Michael Toy comes back from Italy.</li>
<li class="ev ev--written">Michael Toy and Jon Lane, who met at Olivetti, found A.I. Design in Santa Clara, and Lane and Mel Sibony adapt Rogue for the IBM PC. A.I. Design publishes <a href="../games/pc-rogue-1-48/">PC Rogue</a>, grown from Rogue 5.2, with a new set of monsters in place of those taken from Dungeons &amp; Dragons, to keep clear of TSR (<a href="../talks/craddock-making-of-rogue-2016/">Craddock</a>). At first they box and sell it themselves, from Lane's garage, and barely break even.</li>
<li class="ev ev--written"><a href="../games/rogue-5-3/">Rogue 5.3</a> in August, found in 4.2BSD, with the same new monsters.</li>
<li class="ev ev--written">10 October: Rog-O-Matic wins at Rogue 5.2, at the University of Waterloo.</li>
</ul></li>
<li><span class="t-year">1984</span><ul>
<li class="ev ev--written">16 February: Rog-O-Matic wins at Rogue 5.3, at the University of Texas.</li>
<li class="ev ev--written">Epyx, through Robert Botch, takes Rogue on as its publisher, and pays A.I. Design to port it to other computers.</li>
<li class="ev ev--written">At the University of Strathclyde, Allan R. Black rebuilds Rogue 5.3's source from the object file Berkeley shipped with 4.2BSD, keeping the names in its symbol table and inventing the rest: Strathclyde Rogue, "rogue (Strathclyde) 26/7/84", under SCCS by October. It survives in <a href="https://github.com/JulianOnions/rogue-5.3">Julian Onions's repository</a>.</li>
</ul></li>
<li><span class="t-year">1985</span><ul>
<li class="ev ev--written"><a href="../games/rogue-5-4/">Rogue 5.4</a>, its version string dated 31 March, later found with 4.3BSD.</li>
<li class="ev ev--written">Rog-O-Matic XIV is posted to comp.sources.unix in March.</li>
<li class="ev ev--written">Epyx publishes Rogue for the Apple Macintosh, written by Michael Toy with Jon Lane at a cabin near Lake Tahoe, with graphics by Glenn Wichman, who is paid with the used Mac he drew them on.</li>
</ul></li>
<li><span class="t-year">1986</span><ul>
<li class="ev ev--written">ASCII Corporation publishes A.I. Design's Rogue in Japan for the NEC PC-8801 and PC-9801.</li>
<li class="ev ev--written">Epyx brings Rogue to the Atari ST and the Amiga, written side by side by Glenn Wichman (the ST, with graphics by Epyx's Michael Kosaka) and Michael Toy (the Amiga). The $15,000 advance for the ST is the only money Wichman ever makes from Rogue (<a href="../talks/wichman-spillhistorie-2024/">Wichman, 2024</a>).</li>
<li class="ev ev--written">Published by Tandy, Rogue comes to the Color Computer 3: begun at A.I. Design, and finished in assembly language by Mike Leber, Ron Miller, James Long and Ed Rosenzweig.</li>
</ul></li>
<li><span class="t-year">1987</span><ul>
<li class="ev ev--written">On 11 May Tim Stoehr of Tektronix posts a Rogue of his own, written from scratch to play like Rogue 5.3, to comp.sources.games as "a rogue 5.3 clone": his Rogue Clone II.</li>
<li class="ev ev--written">On 30 November Stoehr sends Kirk McKusick at Berkeley Rogue Clone III, with a list of how it differs from Rogue 5.3.</li>
</ul></li>
<li><span class="t-year">1988</span><ul>
<li class="ev ev--written">Berkeley takes Stoehr's clone into 4.3BSD-Tahoe in place of the original Rogue, and it stays the BSD rogue from then on.</li>
<li class="ev ev--written">Mastertronic brings Rogue to the Commodore 64, ZX Spectrum, Amstrad CPC and Atari 8-bit, under licence from Epyx, developed by Icon Design, and reissues the Atari ST version.</li>
</ul></li>
<li><span class="t-year">1989</span><ul>
<li class="ev ev--written">Epyx goes bankrupt.</li>
</ul></li>
</ol>

## The forks, 1982–1991

Rogue 3.6 was the version everyone had, so when people away from
Berkeley set out to make a bigger Rogue, that is where they started.
Each fork borrowed from the ones before it.

<ol class="timeline">
<li><span class="t-year">1982</span><ul>
<li class="ev ev--written"><a href="../games/super-rogue-9-0/">Super-Rogue</a> grows out of Rogue 3.6 at AT&amp;T Bell Labs. Its earliest dated change, to the tombstone code, is from 17 February.</li>
<li class="ev ev--written">22 October: Super-Rogue 7.0.</li>
<li class="ev ev--written">16 December: Super-Rogue 8.0.</li>
</ul></li>
<li><span class="t-year">1983</span><ul>
<li class="ev ev--written">23 April: <a href="../games/advanced-rogue-1-0/">Advanced Rogue 1.0</a>, forked from Super-Rogue 8.0.</li>
<li class="ev ev--written">7 May: Super-Rogue 9.0, the last version, worked on until July 1984.</li>
</ul></li>
<li><span class="t-year">1984</span><ul>
<li class="ev ev--written">Advanced Rogue spreads through AT&amp;T: version 1.3 by the spring, then 2.0, and the <a href="../games/advanced-rogue-5-8/">5.x line</a> by the autumn. Michael Morgan and Ken Dalka are among its authors.</li>
<li class="ev ev--written">17 December: Herb Chong forks Advanced Rogue, probably 2.0, as "PreUltraRogue", the start of <a href="../games/ultrarogue-1-07/">UltraRogue</a>.</li>
</ul></li>
<li><span class="t-year">1985</span><ul>
<li class="ev ev--written">UltraRogue 0.00 is dated 15 January. 1.02 Beta follows ("Dr. C and Ivan were here 5/19/85").</li>
</ul></li>
<li><span class="t-year">1986</span><ul>
<li class="ev ev--written">UltraRogue 1.0.3 is dated 13 August, and goes round mostly as a binary.</li>
<li class="ev ev--written"><a href="../games/advanced-rogue-7-7/">Advanced Rogue 7.7</a>, the last of the line. AT&amp;T sells Advanced Rogue through its Toolchest for a time.</li>
</ul></li>
<li><span class="t-year">1987</span><ul>
<li class="ev ev--written">UltraRogue 1.03 is released, dated 13 January; a copy marked "Jeffro was here 10/15/87" goes round, probably from MIT.</li>
</ul></li>
<li><span class="t-year">1989</span><ul>
<li class="ev ev--written">Robert Pietkivitch begins <a href="../games/xrogue-8-0/">XRogue</a> for the AT&amp;T UNIX PC, from Advanced Rogue 7.7.</li>
</ul></li>
<li><span class="t-year">1991</span><ul>
<li class="ev ev--written">XRogue 8.0 is finished on 8 June.</li>
</ul></li>
</ol>

## Keeping it alive, 1992–2015

<ol class="timeline">
<li><span class="t-year">1992</span><ul>
<li class="ev ev--restored">Herb Chong sends the UltraRogue source. Bringing it up to ANSI C is the project's first restoration.</li>
<li class="ev ev--written">UltraRogue 1.04 is dated 24 October.</li>
</ul></li>
<li><span class="t-year">1993</span><ul>
<li class="ev ev--written">UltraRogue 2.00, with a portable save-file format: 2.00a in September, 2.00 dated 1 October.</li>
</ul></li>
<li><span class="t-year">1995</span><ul>
<li class="ev ev--written">UltraRogue 2.10 in October, the last of Herb Chong's versions to survive.</li>
</ul></li>
<li><span class="t-year">1996</span><ul>
<li class="ev ev--restored">Robert Pietkivitch sends the XRogue source, and helps bring it back to life.</li>
</ul></li>
<li><span class="t-year">2000</span><ul>
<li class="ev ev--restored">The project opens on SourceForge.</li>
<li class="ev ev--restored">Rogue 3.6.1 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">XRogue 8.0.1 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
</ul></li>
<li><span class="t-year">2002</span><ul>
<li class="ev ev--restored">Ken Arnold publishes his Rogue 5.4 source on SourceForge.</li>
<li class="ev ev--restored">In memory of Robert Pietkivitch, who passed away on 3 December. He will be missed.</li>
</ul></li>
<li><span class="t-year">2004</span><ul>
<li class="ev ev--restored">Robert Kindelberger provides the long-lost Super-Rogue 9.0 source. rogueforge.net goes live.</li>
</ul></li>
<li><span class="t-year">2005</span><ul>
<li class="ev ev--restored">Rogue 3.6.2 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">XRogue 8.0.2 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">UltraRogue 1.0.7 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Rogue 5.2.1 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Super-Rogue 9.0-1 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Advanced Rogue 5.8.1 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">XRogue 8.0.3 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
</ul></li>
<li><span class="t-year">2006</span><ul>
<li class="ev ev--restored">Rogue 5.4.1 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Rogue 5.4.2 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Advanced Rogue 7.7.1 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Advanced Rogue 5.8.2 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Rogue 3.6.3 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Rogue 5.2.2 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
</ul></li>
<li><span class="t-year">2007</span><ul>
<li class="ev ev--restored">Rogue 5.4.3 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Rogue 5.4.4 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
</ul></li>
<li><span class="t-year">2008</span><ul>
<li class="ev ev--restored">Rogue 5.4.5 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Rogue 3.6.4 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
<li class="ev ev--restored">Rogue 5.2.3 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
</ul></li>
<li><span class="t-year">2013</span><ul>
<li class="ev ev--restored">Glenn Wichman, Michael Toy and Ken Arnold agree to a BSD licence for Rogue.</li>
</ul></li>
<li><span class="t-year">2015</span><ul>
<li class="ev ev--restored">Rogue 3.6.5 released (<abbr title="Rogue Restoration Project">RRP</abbr>)</li>
</ul></li>
</ol>

## Redux, 2026

Starting over from the binaries, with Claude. The [Redux](../story/) chapters tell the story in full.

<ol class="timeline">
<li class="t-redux"><span class="t-year">Mar</span><ul>
<li class="ev ev--restored"><a href="../story/">Redux</a> begins. Ghidra and radare2 are fixed for the PDP-11 and VAX, and every version is decompiled.</li>
</ul></li>
<li class="t-redux"><span class="t-year">Apr</span><ul>
<li class="ev ev--rebuilt">2 April: Rogue 5.4's object file matches, with two small patches. Then the work stalls for seven weeks.</li>
</ul></li>
<li class="t-redux"><span class="t-year">Jun</span><ul>
<li class="ev ev--restored">Claude Opus 4.8, then on 12 June Claude Fable 5. The 2.8BSD toolchain and simulator are built, and the stalled problems start to give. Late in June Fable is withdrawn for a while, and the work <a href="../story/models/">waits for it</a>.</li>
</ul></li>
<li class="t-redux"><span class="t-year">Jul</span><ul>
<li class="ev ev--rebuilt">3 July: Rogue 3.4 matches byte for byte, with a rebuilt 2.8BSD toolchain.</li>
<li class="ev ev--rebuilt">5 July: Rogue 3.6 for the PDP-11, then Rogue 3.6 for the VAX and Rogue 4.22.</li>
<li class="ev ev--rebuilt">13 July: Rogue 5.3, object file and installed game. 19 July: Rogue 5.2.</li>
</ul></li>
<li class="t-redux"><span class="t-year">Aug</span><ul>
<li class="ev ev--restored">The PDP-11 and VAX tools become <a href="../story/toolchains/">pdp11-xdev and vax11-xdev</a>, toolchains and simulators for every Unix of their machines.</li>
</ul></li>
<li class="t-redux"><span class="t-year">Nov</span><ul>
<li class="ev ev--restored">Claude Fable 5.2 and Opus 5.5 get the stuck Linux ports moving; all six Berkeley versions are ported in a week. Rog-O-Matic plays again, with a runner for unattended games, and XRogue and <a href="../games/advanced-rogue-1-0/">Advanced Rogue 1.0</a> follow. PC Rogue is next.</li>
</ul></li>
</ol>

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
