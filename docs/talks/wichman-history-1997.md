---
title: A Brief History of Rogue, by Glenn Wichman
summary: Glenn Wichman's 1997 account of how Rogue was made, from his website, now offline.
hide_summary: true
---
# A Brief History of Rogue, by Glenn Wichman

<div class="paper-source paper-source--conference">
<div class="paper-source__kind">Essay</div>
<div class="paper-source__date">1997</div>
<div class="paper-source__venue">A Brief History of "Rogue"</div>
<div class="paper-source__detail">Glenn R. Wichman · wichman.org (offline; Internet Archive copy)</div>
<div class="paper-source__id"><a href="https://web.archive.org/web/20110927071632/http://www.wichman.org/roguehistory.html">web.archive.org: wichman.org/roguehistory.html</a></div>
</div>

Wichman's own account of how Rogue was made, written in 1997 for his website: curses arriving
at Santa Cruz, the game he and Michael Toy built on it (and his naming of it), the move to
Berkeley and Ken Arnold, BSD, A.I. Design with Jon Lane, the Mac, Atari ST and Amiga versions for
Epyx, and where "the Rogue Band" had gone by the late 1990s. The page linked to a Rogue Stories
page of readers' stories, which follows it here.

See also his [1984 Usenet post](wichman-usenet-1984.md) on the same subject.

> **About this text.** Glenn Wichman's essay from his own site, wichman.org, which is no longer
> online. The text is from the Internet Archive's copy of September 2011 ([archived page](https://web.archive.org/web/20110927071632/http://www.wichman.org/roguehistory.html)),
> the last before the site changed; it is unchanged, with its 1990s links as they were (most are
> now dead). © 1997 Glenn R. Wichman. Reproduced here with attribution so it is not lost. The
> [first archived copy](https://web.archive.org/web/19980625212119/http://www.wichman.org:80/roguehistory.html), of June 1998, differs only in the closing news: then Michael Toy
> "has been at Netscape" rather than "recently retired from Netscape", and there is no link to
> Ephraim Cohen's Java Rogue or to the Rogue Stories page.

## A Brief History of "Rogue"

*by Glenn R. Wichman — copyright © 1997 Glenn R. Wichman*

* The classic computer game "Rogue" was developed over a a period of a few years by a number of people. I was one of those people, and this is my version of the story. This happened quite a while ago, and my memory is imperfect, but I'll do my best to give the facts clearly and correctly. There are some details I don't know or may have confused. The others might tell the story differently.*

*I'm not going to describe the game itself here. There are plenty of other places where that information is available.*

For those of you who weren't involved with computers back in 1980, a little background is going to be necessary. Let me set the scene. The main home computers at this time were the Atari 400/800, the Commodore 64, and the Apple II (No Macintosh, and hardly any IBM PC's at the time). At computer labs in universities, most students used "dumb terminals" connected to some kind of mainframe or minicomputer. These terminals had no graphics capabilities. Programs would just output text, which would scroll off the screen and disappear.

A popular game on college computers at the time was a text-only role playing game called "Adventure". The computer would print out a textual description of your surroundings, and you would respond by typing in a command telling what your character should do, e.g. "go west" or "pick up bird".

Around this time at U.C.Berkeley, a student named Ken Arnold (I'm sure there were others involved as well) put together a library of routines which allowed programs to do "cursor addressing", which means the programs could put a character at a specific location on the computer screen. There were still no real "graphics", but now you could use letters, numbers, and symbols to simulate pictures. The library of software routines was called "curses".

As this package began to make the rounds to other universities, it was picked up by a couple of students in Santa Cruz, California, [Michael Toy](http://www.toyland.org/) & myself, Glenn Wichman. We both enjoyed playing "Adventure" (Michael had long ago mastered the program; I kept getting killed but enjoyed it anyway).

Being a creative pair, we immediately set about seeing what kind of fun we could have with the new curses library. After fooling around with a couple simple games, we considered whether we could use this package to do a "graphical" adventure game. Once we decided it could be done, things moved forward pretty quickly. I was still a novice "C" programmer, so Michael did most of the actual programming of the original version (I pretty much learned "C" by looking over his shoulder as he wrote). The ideas in the game came from both of us. The name "Rogue" was my idea.

One of the things we wanted to do was create a game we could enjoy playing ourselves. Most of the existing adventure-type games had "canned" adventures -- they were exactly the same every time you played, and of course the programmers had to invent all of the puzzles, and therefore would always know how to beat the game. We decided that with Rogue, the program itself should "build the dungeon", giving you a new adventure every time you played, and making it possible for even the creators to be surprised by the game.

We had a playable game, without all the features yet (e.g., no armor), when Michael transferred to U.C. Berkeley, where he met up with Ken Arnold. For a while, we each moved forward with our own versions of the game, him in Berkeley and me in Santa Cruz. This proved to be too difficult to keep up logistically, so I just let Michael & Ken take over Rogue development completely. To this day, there are a lot of folks who think of it as Michael & Ken's game.

Rogue's move to Berkeley was fortuitous. U.C. Berkeley was the home of a particularly popular version of UNIX called BSD (Berkeley Standard Distribution). Version 4.2 of BSD UNIX included Rogue -- suddenly, the game was available on university computers all over the world. At the time, there was no other game like it. Over the next 3 years, Rogue became the undisputed most popular game on college campuses.

Soon, Michael & I each left school for the professional world. I was working at a Silicon Valley start-up, and Michael got a job working for Olivetti in Italy, where he met Jon Lane, who would become the fourth member of the Rogue Band.

After returning from Italy, Michael & Jon started their own company called A.I.Design. One of their first projects was to "port" Rogue from UNIX to the IBM PC. For awhile, they packaged & sold this game on their own. I was not really involved during this period.

Michael Toy was one of the very first people to buy a Macintosh computer. Soon, a Mac version of Rogue was underway. I got back involved in the project -- I did the graphic design for Mac Rogue in exchange for a used Macintosh computer. Meanwhile, Michael & Jon tired of trying to market Rogue on their own, so they got together with an established computer game company called "Epyx", who took over the marketing & packaging of the game. At this point, I came to work for A.I.Design.

Once Epyx was involved, we decided to do versions of the game for the Amiga and the Atari ST. Michael wrote the Amiga version, and I wrote the Atari ST version. Unfortunately, although Rogue had been wildly popular on college mainframes, commercial success eluded us. Epyx went bankrupt, Atari ST's and Amiga's faded away, and the computer gaming world became a much more sophisticated place, where a little game like Rogue no longer fit in. Still, although the versions of Rogue that we wrote are almost impossible to find anymore, Rogue and its decendants live on, and shareware versions of Roguelike games are available for just about every computer platform.

Just like watching those old, black & white, silent movies can teach us about how Cinema got to where it is today, looking at old games like Adventure and Rogue can help us understand how computer gaming evolved. Rogue is generally credited with being the first "graphical" adventure game, and it probably was at least one of the first (Wizardry could probably also make the claim). And its graphics have since been far surpassed by everything from Myst to Doom. But I think Rogue's biggest contribution, and one that still stands out to this day, is that the computer itself generated the adventure in Rogue. Every time you played, you got a new adventure. That's really what made it so popular for all those years in the early eighties.

As for the Rogue Band, we are all still in the computer industry, though none of us is doing professional game programming. Ken Arnold, last I knew, was at [JavaSoft](http://www.javasoft.com/). Michael Toy recently retired from [Netscape](http://www.netscape.com/), where he worked since it began. Jon Lane continues to run his own small company, [The Code Dogs](http://www.codedogs.com/). And myself? After 5 years at [Intuit](http://www.intuit.com/), I am at an intranet start-up called [UpShot](http://www.upshot.com/). Back when I had spare time, I worked on a couple of shareware games for the Mac. If you're a Mac person, [check 'em out](http://www.wichman.org/shareware.html).

Thanks for listening to my story. If you haven't played Rogue -- give it a try. You'll be surprised how enjoyable it is even after all these years. You can play Ephraim Cohen's Java version of Rogue [right now, on-line](http://www.hexatron.com/rogue/)! I would love to hear your comments, recollections, and stories about Rogue. See the [Rogue Stories](http://www.wichman.org/roguestories.html) page for details.

**Further Information:** I get a number of requests that I am unfortunately unable to fulfill. Following are some of the things that I **cannot help you** with:

- Binary copies of any particular version of Rogue
- Source to any particular version of Rogue
- Rogue hints, cheats, or strategies
- Technical support
- Information on Rogue's internal algorithms

If you are looking for more information, your best sources are [Edwin's Rogue pages](http://www.casema.net/%7Eloche/rogue/index.html), along with the [Rogue Home Page](http://www.win.tue.nl/games/roguelike/rogue/), and the Rogue News Group (news:rec.games.roguelike.rogue).

## Rogue Stories

*The Rogue Stories page on wichman.org, as archived in June 1998 ([archived page](https://web.archive.org/web/19980625221401/http://www.wichman.org:80/roguestories.html)); it held one
story, by a reader, Christine Colby, and an invitation to add more.*

> The one especially memorable Rogue-related story I have is about how we went on vacation and came back to discover that we had been robbed. We figured they weren't professionals, because they didn't take the TV or, luckily, the computer. We didn't know for sure who the culprit was, although thanks to some neighbors and the person watching our cat, we had a few ideas. A short while later, maybe even the day after we came home, my brother sat down to play some Rogue. He didn't have a very good game, and made it to the high score list right away. Well, upon examination of the list, he discovered that someone had gotten on the top 10 high score list while we were GONE! And that moron, for all his apparent Rogue-playing skill, was too dumb not to type his own name in at the beginning of the game!! Needless to say, thanks to this new evidence, we soon got all of our things back.
>
> — Christine Colby, Madison, Wisconsin
