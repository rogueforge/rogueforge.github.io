---
title: Glenn Wichman talks to Gamereactor, 2020
summary: Gamereactor's 2020 interview with Glenn Wichman, co-creator of Rogue, for the game's fortieth anniversary.
hide_summary: true
---
# Glenn Wichman talks to Gamereactor, 2020

<div class="paper-source paper-source--conference">
<div class="paper-source__kind">Interview</div>
<div class="paper-source__date"><span>March</span> 2020</div>
<div class="paper-source__venue">40 Years On: The Making of Rogue with Glenn Wichman</div>
<div class="paper-source__detail">Gamereactor · Mike Holmes · written</div>
<div class="paper-source__id"><a href="https://www.gamereactor.eu/40-years-on-the-making-of-rogue-with-glenn-wichman/">gamereactor.eu/40-years-on-the-making-of-rogue-with-glenn-wichman</a></div>
</div>

Gamereactor's Mike Holmes interviewed Glenn Wichman for Rogue's fortieth anniversary, in March 2020,
when Wichman was at Zynga Toronto: meeting Michael Toy in the Santa Cruz computer lab, curses and
"the computer creates the dungeon", the eureka moments, why "perma-death" should be called
consequence persistence, the roguelikes he has played, never winning Rogue himself, his career
after Rogue, and his favourite memory of the game.

See also [Glenn Wichman talks to Slashie, 2007](wichman-roguetemple-2007.md) and the [2016 panel with Michael Toy and Ken Arnold](rogue-panel-2016.md).

> **About this text.** Gamereactor's interview, by Mike Holmes, as published on 8 March 2020
> ([original](https://www.gamereactor.eu/40-years-on-the-making-of-rogue-with-glenn-wichman/)). The text is theirs, unchanged; © 2020 Gamereactor. Reproduced here with
> attribution so it is not lost; the article's photographs and illustrations are not copied here.
> The speaker labels are set in bold.

## Interview

*We caught up with one of the creators of Rogue, the classic RPG that inspired a whole generation of game makers.*

40 years ago Michael Toy and Glenn Wichman released the first version of an ambitious game called Rogue. Later on, they'd have help from Ken Arnold and Jon Lane, but it was when Toy and Wichman met at the University of California, Santa Cruz (UCSC) in the late '70s that the first seeds were sown, not only for a game but also a whole genre.

This simple yet supremely influential role-playing adventure tasks players with descending deep into a dungeon filled with monsters in search of the Amulet of Yendor, before returning to the surface. It's turn-based, which gives you the time to consider all of your options as you try and make the right decision. Yet that's easier said than done, with procedurally generated dungeons filled with procedurally positioned monsters and random potions meaning a new experience that's never the same twice and where every step you take must be carefully considered.

Over the years Rogue has directly inspired a whole host of copycat dungeon crawlers, complete with text-based ASCII graphics. However, its influence has grown to be much more widespread than that, and the core mechanics that Toy and Wichman pioneered 40 years ago can still be felt in a number of prominent games to this day (and not just indies, even triple-A studios have experimented with the core features found in the first Rogue). Now, in 2020, phrases like "procedural generation" and "perma-death" are part of the gaming lexicon, something that simply wouldn't have been the case without Rogue and its creators.

Given the significance of the milestone that Rogue reached this year and our enjoyment of roguelikes in general, we tracked down one of the developers responsible for this innovative, genre-defining turn-based RPG. That developer is Glenn Wichman, who now works at Zynga Toronto, and below is the interview where he was kind enough to answer our questions about the part he played in creating what turned out to be a hugely important title that has truly stood the test time.

**Gamereactor: Please tell us about how you got started with Rogue and what part you played in its creation.**

**Glenn Wichman:** I enrolled at U.C. Santa Cruz, in large part because it gave the flexibility to design your own major, and I wanted to major in Game Design, which was, of course, not a thing anyone was offering majors in in 1979. Turns out I did not have the self-discipline necessary to design and pursue my own major, but that's how I ended up there. I had not conceived of designing computer games, I wanted to design tabletop games.

But at Santa Cruz I discovered the computer lab; this was my first real exposure to computers of any kind. The computer was of course in a basement somewhere on the other side of campus and I never actually saw it, we just had terminals connected to it. This was a DEC PDP-11 (later upgraded to a VAX), running Bell Labs UNIX, and it had games on it. Like, five games. Including Adventure a.k.a. Colossal Cave Adventure, and after playing it a few times I wanted to get creative and make my own text adventures. So I set about trying to figure out how to program the computer and taught myself the basics of BASIC, and was off and running.

So, of course, I created a horrible mess of tangled code, trying to bring the game to life, and while struggling with that I felt a presence behind me and looked over my shoulder to see Michael Toy watching me code.

He had built his own computer in high school, he was also a big fan of text adventure games, and had also created his own, but he actually knew how to code. We immediately started trading ideas back and forth and I ended up, mostly through "osmosis" becoming a really good coder just by watching how he approached problems.

Soon Michael & I were each creating text adventure games; he would play mine, I would play his. But it was no fun to play our own because of course when you create all the puzzles and challenges you can't help but win.

(Note that much of the time we were creating these adventures we should theoretically have been in class or doing homework.)

One day Michael showed up with a library of code routines called "curses", which had been created by Ken Arnold at UC Berkeley, based on the work of Bill Joy. This library made it easy to create "graphics" on "dumb terminals" using "cursor addressing" to put "ascii art" on the screens... skipping over lots of background information there, but I'm already going on too long. Anyway, it gave us the opportunity to make whole different sorts of games from what we had done before. But they had to be written in "C" and Michael had mastered "C" but I was still learning it. We created several simple graphical games but then Michael said, "could we create a graphical adventure game?"

We talked it over and decided it was possible, but also decided that we would have to make one where "the computer creates the dungeon", so we could be challenged by our own creation, and so we could come back and play it over and over, getting a new adventure every time we played.

**GR: Much of what made Rogue so unique came from innovation born of technical limitations, but there must also have been a bunch of "Eureka" moments when the pieces of the puzzle all came together?**

**GW:** It is funny how, in retrospect, it feels like we were struggling with technical limitations. At the time, we were working with pretty much the pinnacle of computer technology, short of supercomputers that only existed in weapons labs. So, it was certainly a design constraint that everything we did had to fit in an 80x24 grid of ascii characters, and the limits imposed by 32K of addressable memory meant that we could only keep track of about 9 rooms at any one time, so when you went down to level 3, we had to completely forget everything about level 2... But we didn't perceive it as a struggle to overcome technical limitations, we perceived it as this set of amazing capabilities that we got to play with.

The eureka moments happened as we realized just how immersive our game had become. Yes, you were looking at ascii characters, dots for floors and dashes for walls, and letters for monsters... but there was a genuine emotional response when playing the game. Your heart would skip a beat when a "T" appeared on the screen because it really felt like a troll had entered the room.

**GR: The game has had such a profound influence since you made it. When did you realise that you'd made such an important title? Was it in the '80s? In the '90s as purists continued to make traditional roguelikes? Or was it later, when the word roguelike became shorthand for procedural generation and perma-death?**

**GW:** Before the game was even completed we knew we had a game-changer. We had the good fortune to be shipped along with the BSD UNIX operating system, so the game came pre-installed on college campuses all around the world. So from the beginning, I expected it to be important, and when we created a commercial version I expected it to be a big hit and make us rich. So, we had that initial rush of knowing we had made something truly special, followed by very high expectations, followed by a crash of disappointment. By the late '80s Rogue was largely forgotten, I didn't even include it on my resumé because no one knew what I was talking about. For years Rogue was completely off my radar.

Then a couple of things happened... one was of course that an amazing worldwide community of indie developers had grown up around rogue and its immediate descendants, and were inspired to create their own games. The other was that game design began to be taught in schools, and Rogue became part of the curriculum. It was probably in the early 2000s that I first became aware of the Roguelike genre, of the concepts and controversies about "what constitutes a roguelike", about procedural generation as a concept, and about the unfortunately-named concept of "perma-death"

Let me just talk about perma-death because I think it is one of the most misunderstood things about Rogue and the games that followed. I feel like people imagine Michael and me sitting in front of the terminal and saying "How can we make this game really hard-core?" "I know, let's add something called 'perma-death' ... even worse than just plain old death! It will scare away children and casual gamers!"

I don't know when the term perma-death got coined, or how it came about (I would love to find out). But the game mechanic should really be called "consequence persistence" -- well, it should go by some much sexier term, but with that meaning. It is a necessary component of any game that has both procedural generation and mystery objects. The idea is just that once you have committed to a course of action, you are bound by the consequences of that action. It's a game mechanic we borrowed from Chess: once you take your finger off the piece, you don't get to change your mind about where to move it. So, making a move that kills you, kills you permanently (I suppose), but making a move that wins the game wins it permanently, yet they don't call the feature "perma-win". When you find a potion in Rogue, you don't know whether drinking it will result in a benefit or in harm. So you have to commit to a decision, do I drink it or not? If you are allowed to go back and re-play the game from any point, then there is no decision to be made, of course you drink the potion. If it was bad, you just go back in time and then don't drink it; the entire game falls apart at that point.

But now some games see "perma-death" as a kind of bad-ass mode that you can turn on or off. To my way of thinking, for any game that requires hand-eye coordination, throwing in "perma-death" like it's just an option you can put in any game, is just mean. Because for a game like that, what you actually accomplish may not be what you intended to accomplish, so of course you should get to re-try to perfect your technique.

**GR: Do you ever play modern roguelikes, roguelike-likes or roguelites (or whatever people like to call them), and if so, which ones do you like?**

**GW:** I have played a few, though I haven't ever sought any out. I have played Rogue Legacy and Spelunky and Don't Starve (all great games!), and I have been a judge in several roguelike competitions so I've played the submissions. There are a lot of amazing, deep, rich games out there and most of them are much too complex for my tastes. I have huge admiration for them, but I prefer simpler games. Also many of them have a fiction that is far too bloody and gory for my tastes.

**GR: When was the last time you played the game and how far did you get?**

**GW:** I don't remember when was the last time I really properly played Rogue, beyond just going through a level to show it to someone. I can tell you that I have never legitimately beaten the game, I have found the amulet a couple of times, but never made it out of the dungeon alive.

**GR: Please tell us about your career since Rogue, culminating in your work at Zynga.**

Michael, along with Jon Lane, founded a company to create a commercial version of Rogue. I worked for that company, creating the graphics for the Macintosh version and doing all the coding for the Atari ST version. When Rogue did not succeed commercially, Michael & Jon took the company in a non-gaming direction. I still wanted to make games, so I got a job at a company in LA called Software Toolworks, where I worked on a half-dozen games, the best-known being Mavis Beacon Teaches Typing (there is a generation that knows me much more as 'The Mavis Beacon Guy' than 'The Rogue Guy'). I had several game ideas that I pitched to Software Toolworks, but they didn't want to do them, so I got the bright idea to start my own company to make my own games. I'm an excellent game designer and coder, but a lousy businessman, so I soon found myself broke, right at the moment the games business was also in a big downturn...

So, for about 20 years I worked as a software developer outside the games business, working on software for personal finance, customer relationship management, e-commerce, and public health, creating a couple of shareware games in my free time. But I always was looking for an opportunity to return to the games business.

When social gaming first began to take off, I fell in love with the idea of playing cooperative games with your friends, working together to create something, instead of fighting against each other to destroy something. I interviewed at Zynga on my 50th birthday. In spite of the fact that I'd been away from games for 20 years, they gave me a shot. I had to re-learn everything I ever thought I knew, it's been an incredible ride. I'm now approaching my 60th birthday and I am doing the best work of my career, making mobile social word games like Words With Friends. And I'm still amazed at the technology that I get to play with... it hits me every now and then that the entire game of Rogue used less memory than Words With Friends' "W" icon, and the phone in my hand is 10,000 times faster and has 125,000 times the memory of that big mysterious computer off in the basement at UCSC. And yet programs still take 12 seconds to boot up. What's up with that?

**GR: Finally, looking back, what's your favourite memory of Rogue?**

**GW:** I can't pick just one... I got an email once from a young man who used to play Rogue with his dad, who had since passed away, thanking me for the memories I had helped create in his life. I've gotten several emails like that over the years. And I've had the chance to meet fans or to meet up with developers that have been inspired by what Michael and I did.

*If you've never played the original and want to try out this slice of gaming history for yourself, you can play it via your web browser over on [MyAbandonWare](https://www.myabandonware.com/game/rogue-4n/play-4n).*
