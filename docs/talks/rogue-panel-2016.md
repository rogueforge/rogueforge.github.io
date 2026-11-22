---
title: Rogue panel: Glenn Wichman, Michael Toy and Ken Arnold
summary: Glenn Wichman, Michael Toy and Ken Arnold on stage together at the 2016 Roguelike Celebration, transcribed.
hide_summary: true
---
# Rogue panel: Glenn Wichman, Michael Toy and Ken Arnold

<div class="paper-source paper-source--conference">
<div class="paper-source__kind">Panel</div>
<div class="paper-source__date"><span>September</span> 2016</div>
<div class="paper-source__venue">Roguelike Celebration</div>
<div class="paper-source__detail">San Francisco · video, 30:49</div>
<div class="paper-source__id"><a href="https://www.youtube.com/watch?v=4IkrZkUV01I">youtube.com/watch?v=4IkrZkUV01I</a></div>
</div>

The three creators of Rogue together on stage, by their own account the
first time in about thirty years that they had all been in the same room.
The first half is a moderated Q&A; the second takes questions from the
audience. They talk about meeting at UC Santa Cruz, how Ken Arnold's curses
library made Rogue possible, the players in the stat lab, Rogue's spread
through Bell Labs and BSD, Rog-O-Matic, and why "permadeath" is the wrong
name for what they meant.

See also the [2021 interview with Glenn Wichman](wichman-interview-2021.md).

> **About this transcript.** Made from YouTube's automatic captions and lightly edited for
> readability: punctuation added, false starts, repetitions and filler words removed, and
> obvious mishearings corrected (names, technical terms, *roguelike*, *permadeath*,
> *Rog-O-Matic*). The wording is otherwise as spoken, slips included; words in [brackets] were
> supplied, and *[unclear]* marks words the captions lost. The captions do not say who is
> speaking: the moderator, David Craddock, asks the first questions, then the audience; a dash
> marks a change of speaker within a paragraph. Chapter titles are YouTube's; each timestamp
> links to that point in the video.

## The origins of Rogue

[**0:08**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=8s) Well, I'll jump right into this. Glenn asked me to moderate the first half of this, which is a Q&A, and since I had bugged all of these guys to talk to me, I didn't see how I could really turn them down. So we'll jump right in. What I want to do is, again, my thing, which is set foundations: I'll ask them about their parts and what they think about roguelike DNA and culture, and then we'll take some questions. Michael, before you began writing Rogue, you played a lot of adventure games, namely Colossal Cave, and I wonder if you could tell me how those text adventures led to you creating a game that was very unlike those adventure games — puzzle-driven and so forth.

[**0:49**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=49s) Well, the first time I played Adventure, it was like the universe had changed, right? Suddenly stories are talking to you, and you can actually be in the story. [I] was like, "This is the greatest thing ever. I'm going to write me one of these," right? And then you write an adventure game, and you go, "Oh, this is really boring to play," because there's a troll there, and if I have a bottle of poison, he won't attack me.

[**1:13**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=73s) So it's intense. Okay, that was a blast, but as an author, if I'm going to write games that I play, that can't be the path. So how do I write a game that I can have that sense of wonder, but also be the author, right? — Sure. — Did I answer the question? Yes, I did. — Glenn, how did you and Mike meet, and what was your experience creating and designing games beforehand? What sort of games did you make?

## Meeting and early development

[**1:36**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=96s) So we were both at UC Santa Cruz; we were both freshmen in '78. There were computer labs — it was a small room with three terminals that had wires going to a computer that was off somewhere — and I was trying to teach myself BASIC, and so I was creating a text adventure game. And suddenly, looming behind me, was this large man saying, "What are you doing?" And I said,

[**2:09**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=129s) "Well, have you ever played Adventure?" And yes, he explained to me that he had completely beaten Adventure, which I never had. And so I said, "Well, I'm trying to make a game here." So that was how we met, and he just started looking at the game that I was making, and we started trading ideas, and he started telling me how to program, because I really didn't know; I was just teaching myself.

[**2:37**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=157s) So that was how we met. — And now you are — you've been in the games industry since then? — Yeah, I took a 20-year break from the games industry, but I'm in the games industry now, and I became a professional game developer through that experience, ultimately. — Excellent. So before we jump into Ken, I wanted to ask Mike and Glenn: I wonder if you could tell me how discovering Ken's curses library helped you kickstart Rogue. How important was that in the development of Rogue? — You start.

## The impact of Curses

[**3:14**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=194s) Yeah, well, there would not be a Rogue without curses. So we're in a computer lab, we're using a PDP-11/70, and our terminal is an ADM-3A, which has an addressable cursor; it's 24 by 80. We had Ataris and Apples, but the thing that we had access to was a dumb ASCII terminal.

[**3:39**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=219s) So we're trying to get as close to the graphic — quote — richness of an Apple II's colors as we could on the computers that we had access to. And [it] was this weird dichotomy, because the computers with color graphics were slow, and then the computers that were fast had no graphics. And so curses let us think graphically and visually, and come close to presenting a kind of interactive experience.

[**4:11**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=251s) Yeah, I think initially the first things we did with curses was games like Snake. So there was a while when we were just doing very simple things with it, before — I think, yeah — we asked each other, "Could we do an adventure game, a graphical adventure game, with this?" So that was the big epiphany that started it all.

[**4:36**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=276s) Okay, so Ken, could you talk about what led you to make curses? Because I think the idea of being able to position your cursor on the screen today is kind of a given. — Yeah, I find it hard to describe to people what it enables, because there's no world without that capability. Plenty of people don't use curses, but it was really quite simple.

## Engineering the Curses library

[**5:02**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=302s) There were these cursor-addressable terminals, and people around me — we were hacking on things for entertainment, and we wrote various programs, some of which were just visually interesting. There was one that I wrote that had a constant list of who was in, on the 11/70 we had, which had about 70 terminals on it, so you could see who was around and look for your friends. And then we brought in a second type of cursor-addressable terminal that had a whole different set of sequences, and I didn't want to do this a third time and a fourth time and a fifth time, port it to each one of these things. — Sure. — And at that point, luckily, Bill Joy had already written vi and had the underlying database of capabilities

[**5:40**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=340s) For me to draw on. And I said, "I'm not writing this twice; I'm going to do this once." And so I wanted a regular thing, so that everything could work that way — everything could be cursor-addressable without needing to be rewritten for all these terminals. So I said, "What's the right abstraction?" And I just figured out some way to do this. — That's awesome.

[**5:56**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=356s) So curses is the very first graphic API — cross-platform graphic API? — Yeah, I guess that's true, if you can call that graphic. — Yeah. — To the extent that the character matrix is graphics, yes. Bill Joy had done this for vi, but only vi could use it, basically, and I was having none of that. — Well, and what I found interesting, Ken, is when we spoke, you said that you'd heard of Rogue because a lot of people came up to you and said, "Oh, you're the guy who wrote curses for Rogue." They seem to be tied.

[**6:27**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=387s) Yeah, people believe that curses was written for Rogue, because it's almost everyone's first experience with it. Whereas before, curses had been used in ten programs sitting around Berkeley — who else had seen it? So it's not at all surprising, but it wasn't the origin. When Michael transferred up to Berkeley and left Glenn behind, I came to him because he'd been using curses, and I said, "You're doing this cool thing with my package." I just wanted to talk to him about it. — So, Michael, this might be

## Community and player behavior

[**7:06**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=426s) A long shot, but you said that of course you wrote Rogue because you wanted to be surprised by a game that you had written. I wondered if you had any memories of surprising things that happened to you down in the Dungeons of Doom 30 years ago. — Yeah, 30 years ago, I remember it in detail. No, I'm sorry, I can't help you there. — Anyone else? [unclear] you guys playing this game, because that was one of the fun things. These games are hard to test, because you very rarely can create the same set of circumstances.

[**7:37**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=457s) Well, yeah, rather than give an anecdote, I will say that one of the things that we had — I had no idea what a great thing that we had — was a community of game testers available to us all the time. Or college students trying to pass their class.

[**7:53**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=473s) So we would add some new feature to the game, and immediately all of our friends in what was called the stat lab — which was — we [were] definitely studying statistics. — Yeah, absolutely. — It was very — yeah, we were. — Yes: what are the odds of getting killed by a troll?

[**8:16**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=496s) So I do definitely have memories of 10 or 15 people [in] the stat lab. Again, when we started writing it, it was three terminals, but the following year it grew and was in a bigger room, and there were like 20 terminals around, and there would be 10 people, and they would all be playing Rogue. And then you'd hear somebody scream, and you'd turn around, and they'd have been startled because a T appeared on the screen.

[**8:39**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=519s) So that was something that really hit me: just how this very simple, representational game — the T really didn't look any scarier than a B, but you played it for a while, and you didn't see a T on the screen; you saw a troll.

[**9:02**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=542s) So that was pretty amazing to see. — If I may: you asked about surprises in gameplay. About half of the reason that I got really engaged in the development was being surprised by the users' reaction to things. Both clever things they figured out how to do — we introduced starvation because people figured out how to take advantage of hanging: putting your shoe on the space bar and going and having lunch, and coming back, and you had fainted, but who cared? And so we had to add starvation, right? That had not occurred to us. But also this kind of thing: the people's psychological reaction to it, the kinds of ways that people would personify the algorithms. They'd come and say, "Oh, some games are more like this; you must have this algorithm back there that says, 'Oh, it's going to be a scroll-heavy game.'" No,

[**9:56**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=596s) Not even slightly. But that's the human perception of it, and I learned a lot about how human beings perceive the world and build the world around them, and how unreal, in some sense, what we build around [us] is — what we see in the room right now, what we think we're seeing, is also a construct. I was much more often surprised by that than by the gameplay, where I just died a lot. — Sure.

[**10:21**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=621s) Yeah, I just want to echo that. So when we sat down and said, "We're going to make this thing," we had this grand vision for games: every monster would have his own way of living; maybe they'd build their own dungeons. And so it's like, "Okay, well, let's get some rooms up on the screen, and we'll put some letters in, we'll give them stats, and we'll connect the rooms, and then we can really get started." Only, by the time we did that, it was done. All the things that we were imagining, people were creating in their minds, and it was completely unnecessary, right? You just had to get out of people's way, right? And then they would inhabit the world. Instead of, "We need to create this space or they won't know what they're doing" — it's like, no, they're doing it without us creating it for them. It was really awesome; that was one of the amazing things.

[**11:02**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=662s) Excellent. So we can —

## Design choices and challenges

[**11:10**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=670s) All three of you can answer this; we'll just pass the mics on. But I wondered: as you all worked on the game, did you have a particular aspect of it that you really gravitated to or wanted to hone — procedural generation, or optimization, anything in particular that you liked working on?

[**11:24**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=684s) Well, when I first started getting involved, I wanted to talk to Michael about ways he was using curses that I thought could be done more effectively. I played over a 300-baud dial-up — 300 baud means 30 characters a second; sorry, I have to translate that — and addressing a cursor from one place to another by itself takes four.

[**11:46**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=706s) So when you talk about 30 characters a second, this is not a high-speed interaction modality. And so — it used to be, you hit inventory, and it cleared the screen into the inventory, and then it would redraw the screen. And I made it so it would go to the upper right-hand corner — upper right-hand, 'cause you can clear to end of line, and that's just two characters — and put in the inventory in a little window there, and then just repaint that small part of the screen.

[**12:10**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=730s) So I started out by just making — how do I make it smoother? How do I make it fewer keystrokes? I don't have to hit space as often when I read a potion — "read a potion", boy, that was good — and things like that. So originally a lot of it was smoothness of play, and then after that I was more [into] quirky things. I don't know how many people here have heard of Rog-O-Matic?

[**12:27**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=747s) Yeah? Is any of the authors here? Oh, damn. Never met any of them. But there're these people — I can't remember the school. — MIT. — Right, okay, you guys fight that out later. — CMU. — And they wrote an AI to play Rogue. They called it "Experiments of artificial intelligence in a user-hostile environment", something like that. And so I made it my rule that every release of Rogue would break Rog-O-Matic.

[**12:57**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=777s) So they'd have to go back and do something different with it. It's just that subtle thing — hallucination, for example. I just liked little things that made it more unpredictable and quirky without changing the gameplay. — I think one of the things that I liked best — and again, the code that we're talking about here, I didn't really write any of. When Michael went to Berkeley and he and Ken started working on the game — if there had been such a thing as forking a code base, then I was working on my own fork of the code base. Only that just meant that I was sort of orphaned out there in Santa Cruz. But I did start working on the code then. But again, the code that all of you saw, that went with the Berkeley Software Distribution, I didn't write any of that. But the things that I liked working on, I think, were how the monsters would

[**14:00**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=840s) Pursue you. Like, okay, you leave the room, then the monster needs to stop following you and figure out where the door is instead, because he's got to get to the door and then get to you. And then, again, specialized things that monsters can do, which I did later on when I did the Atari ST version: I added centaurs having the ability that after they hit you, they curse your weapon.

[**14:28**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=868s) So the Atari ST is the only version where that happens. But stuff like that, I think, I liked working on. — I don't have a good answer for this question. It was a blast to do. The procedural generation of Rogue — I was a dumb kid; I didn't know anything about computer science, and so I'm really embarrassed about how poor the procedural generation of Rogue is. It's a tic-tac-toe board with a room randomly placed in each square, because the idea of picking random rooms and then connecting them and making sure the graph is completely connected — I hadn't taken that class [in] computer science yet, and had no idea that such a thing was possible. — I think you described your early experiments as just loading paint into a gun and spraying the wall to see how it came out.

[**15:20**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=920s) So I think we've about wrapped up our 15 minutes.

## Audience Q&A: Genre popularity

[**15:28**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=928s) Thank you guys for answering my questions, and let's open the floor. Right there, right in front. So one of us is gonna walk around with the mic — it'll be me or my wonderful assistant [unclear], dressed as a tourist — and she's going to go hand the microphone to you to ask questions. Okay.

[**15:44**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=944s) While that's going on, I just wanted to say thanks for having us up here. It's an honor to be here. You guys are awesome, right? We made Rogue, but you guys all made roguelikes, so thank you for letting us be here. — This is more for Glenn, since you're back in the games industry, but any of you: clearly this is a genre that has legs, and it's been around for a long time, but also, why isn't it bigger? Why isn't it more popular? I mean, we still see new roguelikes — we've got Binding of Isaac, and you've got things like Dwarf Fortress, and now RimWorld, where there's a lot of emergent behavior, and I think it's probably the same kinds of things that attract people — but it's coming out of indie developers. Why is it that major publishers don't want to touch it? — They're fools. No, that's my joke answer. I think it's big.

[**16:44**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1004s) I think it's plenty big. And I think that the bits and pieces of roguelike — the checkbox list of "this is what makes something a roguelike" — you're going to see some of those in every game. The game I work on now is Words with Friends, and I had somebody joke that it's a roguelike, because it uses ASCII characters, and it's randomly generated, and has permadeath.

[**17:18**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1038s) So I think — but I feel like it's a very — even the hardcore roguelikes is a very vibrant community. I think that because it's not twitchy, it is a little bit more of a niche. It's more for people who want to think hard and want something hard. I can't play roguelikes; they're all way too hard. I created a pretty simple — or we created a pretty simple game, mostly because of the limitations. I think Michael would have made it much more complicated. — No, we ran out of instruction space on the P[DP-11].

[**17:50**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1070s) Yeah, we did. We made it as complicated a game as we could make with the technology we had. — But that was where I liked it; that was fine. I don't like them more complicated than that. — Well, the other thing that's weird is that in America, if it's not the biggest thing ever, it's crap, right? And that's just not true, right? You can make something that has quality that's inherent, that's beautiful, that doesn't appeal to everybody, and that doesn't make it not crap, right? It's just — it's a good thing. Roguelikes are a great thing. We tried to sell Rogue. There was a time where you could buy Rogue in a box in a computer store, and everybody had a chance to make it the biggest thing in the world, and it's just not interesting to a mass market.

[**18:30**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1110s) So we can just say that ship has sailed, and there's been a number of people who have made that attempt — even the Diablo people. It's like, yeah, whatever, 5% of our people like playing it that way. Okay, well, yay for those 5% in this room. Thank you all. — Hey, it's cool to see you guys. When I was like 10, my dad would babysit me by taking me into Tektronix and dropping me in front of a dumb terminal on some mainframe, and they had Hunt the Wumpus and Rogue and a few other games, and I was great for hours.

[**19:05**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1145s) So I was curious — given that experience, there wasn't some internet that I was using at that point; I don't remember, it's like early '80s, right? So I was curious: what was your sense of your user base, your community? Was it just — the game was out there and you talked to a few people you knew at college? Or did you actually have a sense of who was out there playing the game somehow? Or was it actually kind of a surprise?

[**19:37**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1177s) So we wrote this, Glenn and I, instead of attending class at UC Santa Cruz. And one day we discovered that somehow a binary of Rogue had made it to Bell Labs, where the Unix developers were, and they had renamed it Under Bell Labs, which was, I guess, an homage to Beneath Apple Manor. And so a bunch of people at Bell Labs played this game called UBL, which was basically the binary of Rogue. And it's like, people outside the stat lab are playing Rogue? How did that happen? It was a shock that anybody would want to do that. And then it just became a thing, like, wow.

[**20:19**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1219s) Yeah. So by the time it came to Berkeley — [it] was like node 10 in the ARPANET — it did start to get around. And certainly by the end, I think we were very aware: we make a change, and it busts people's save files, 'cause [of] the way we did saves. We knew we had players. But it also changed the way — at least, certainly, I thought of it. Suddenly, to a certain extent, there was a shared score file. And I didn't care if you cheat, because it's entertaining to you and you have a fun time — cheat codes, that kind of stuff, it's cool. But if you're competing against other people, right, that is a whole another thing entirely, and it's unfair.

[**21:01**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1261s) So that made us try to keep it as clean as we could, which was not bad, considering neither of us really understood security, if I could speak for you there. But I remember once — so we had save files, and they were secured in

## Legacy and community impact

[**21:19**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1279s) Certain ways, one of which was by understanding a bit of how they were stored in the file system. And speaking of Bell Labs, I once heard that Ken Thompson was cheating by saving the save file and putting it on a mounted disk, and then he would replay it, and then he would clone the disk and replay it again — the same game, again, over and over again — because he could defeat us, because he was Ken Thompson.

[**21:42**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1302s) So I threw up my hands at that one. But yeah, user community: by the time we were done with it, we absolutely knew that there were a lot of people out there. — Yeah, well, we knew it was being played in Italy, at Olivetti, I think it was. It was a strange thing, because what happened was — and these guys know that part of the story better than me — it became part of the 4.2 Berkeley Software Distribution, right? Which meant that if you got Unix, if you got the operating system, you got our game. If you can get that kind of distribution — you're on the operating system — if you have that opportunity for your game, I would say take it. We were the Minesweeper of Unix. — Exactly.

[**22:30**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1350s) So we knew it was all over the world, and we knew, kind of anecdotally, that it was being played all over the world, and we said that it was the most popular game on college campuses in the early '80s. I don't know how you would substantiate that, but I don't think that there are any other competitors who would challenge it. So it was a strange thing, because it was being played everywhere, but nobody was making money, and there weren't sales charts or these kinds of statistics, DAU measurements, or any of the kinds of things that you take for granted today. — DAU, daily active users. — Wow. — Sorry, industry term.

[**23:17**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1397s) So we had a lot of DAU, but we didn't know how to measure it. And again, by today's standards — the whole industry was so much smaller than it is now that it's hard to compare. But we knew it was very popular, and I think we all felt very gratified. And I think we thought it would be, because we knew we had something pretty cool when we built it. — I think I knew that; I thought people would love it. So yeah, I definitely thought that once it was in a box, it would be a thing that would be in everyone's living room. — Mm-hm.

[**23:51**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1431s) So it was a little bit disappointing [when it] turned out to be in this narrow thing. For this to be cool, you have to [have] played so many games that the things that make Rogue unique to you are kind of shocking, right? [unclear] — My favorite story is: I met Dennis Ritchie, who's one of the people who created the C programming language and Unix, and he's like a god of everything that we're doing, and [I'm] like, "Oh my gosh, the Dennis Ritchie." And he says, "You're the Michael Toy?" Like, okay, I can die

[**24:25**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1465s) Now, because Dennis Ritchie has called me the Michael Toy. That's maybe the best moment related to Rogue in my whole life, that one thing. — Hey, fellas, thanks for coming out; thanks for your cool game. This

## Modern perspectives and favorites

[**24:42**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1482s) [is] for any of you, whoever wants to answer first: if you still follow roguelikes today, or if you see where the genre has gone, is there anything that any of you wish one of us would do? Like, why hasn't this happened yet? You think about where things have gone — does anything come to mind?

[**24:49**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1489s) Thank you. — No, I'm totally amazed all the time. Every time I pick [one] up, [I] go, "Wow, I wish I could have thought of that, or done that." — Yeah, well, I'll echo that. No, I think that what people have done with roguelikes so far surpasses anything that I ever thought of; I think you're all doing way cooler stuff than I was imagining. A couple of things that I would have done if I kept working on things: I wanted to have neural networks, and monsters that got smarter as you fought them. Somebody may be doing these things; I just don't know. I really don't follow it as closely as all of you do, so it's a little embarrassing, sorry. And then I think — what is it, No Man's Sky? That's the new thing — having entire worlds is the other thing.

[**25:49**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1549s) So that is being done, so I can't say you'd do it, 'cause someone's doing it. — So Rogue, for us, was: here's the rules for video games, and those games aren't satisfying, so we're going to break the rules and do something a little bit different. And so, where you continue to push the horizon, going, "I'm bored with what exists, and I'm going to change the rules" — people are already doing that. And so I've really enjoyed all the people [who] said, "Oh,

[**26:16**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1576s) Yeah, roguelike, that's kind of a good idea, but what about a roguelike on a ship in space?" Like, oh, wow, that's a great idea. So you guys are all my heroes, for all the ways that you've done it. — I think one more question. One more question, somebody. — Not counting your own, what is your favorite roguelike? — This is just a question of doom, because I don't want to hurt anybody's feelings. — I'm just going to — if I wasn't married to you — in the early Mac days there was a roguelike called Mission Thunderbolt that I played to the end, and of all the roguelikes, that was probably my favorite that wasn't Rogue. — I'm going to say *Ananas* [as the captions have it], because my friend wrote it. But yeah, I really don't play a lot of roguelikes.

[**27:30**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1650s) So honestly, I'm not a good judge of them. I like more casual [laughter] games. It's a way of not answering your question, because it would get me in trouble. — My son has a Rogue tattoo on his chest, so. — And Glenn, can you talk about permadeath? Because I think you really put permadeath in a good context, and I want to hear that said in this space. — You mean about my post yesterday?

## Defining consequence persistence

[**28:01**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1681s) Yeah. So I posted on Facebook yesterday that we need a different name from permadeath. There's this idea that when people talk about permadeath, they talk about us three being mean. It's like, "Oh, they wanted to make it extra hard, so they threw in permadeath, and only people with lots of testosterone play games with permadeath."

[**28:24**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1704s) Yeah. And the thing is — I didn't like that. This isn't what we came up with, right? Permadeath is an example of consequence persistence, and so this is the name that we need, right? The way that it came out is that with Rogue, we've got mystery items, and we've got procedural generation. From that, what you've got to do: if I find an item, do I use it or not? Do I read this scroll? Do I drink this potion? I don't know; it might be good, it might be bad. If I can save the game, and then drink the potion, and then — oh, it's bad — then I restore the game and I don't drink the potion, that entire game mechanic just completely goes away.

[**29:05**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1745s) So that was the whole reason why — once you have made a decision, or once you have taken an action, once a consequence has happened, there's no way to go back and undo it. And permadeath is not the right name for that. So that's my homework to all of you: [to] come up with a better name.

[**29:20**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1760s) Yeah, we're trying to make it more immersive by making things matter, but not to make it more painful. Make it more fun — it was really meant to make it more fun. Like, "This thing matters; I'm going to think about this," right? The good stuff is just as permanent as the bad stuff. — That's it. Huge round of applause, everyone.

[**29:47**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1787s) So, if I can beg an indulgence: a few years ago somebody sent me a version of the Rogue source code which has essentially vanished from the world. They stole it off of a backup system at UC San Francisco when I worked there, and it's up on SourceForge — oh, that's awesome — under the project Rogue. And it is just post-5.3, and it doesn't quite work, because they stole it in the middle of development. And if anybody wants to pick that up and debug it, we would have the real Rogue source code running. It's not something I've had time to get back to, but find me. — And I just want to quickly say that this is the first time in 30 years that we have all been in the same room.

[**30:28**](https://www.youtube.com/watch?v=4IkrZkUV01I&t=1828s) So you guys are witnessing something pretty cool. — Yes. Thank you all so much.
