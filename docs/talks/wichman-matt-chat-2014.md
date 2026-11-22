---
title: Matt Chat: Glenn Wichman
summary: Glenn Wichman, co-creator of Rogue, interviewed by Matt Barton for Matt Chat in 2014, transcribed.
hide_summary: true
---
# Matt Chat: Glenn Wichman

<div class="paper-source paper-source--conference">
<div class="paper-source__kind">Interview</div>
<div class="paper-source__date"><span>January</span> 2014</div>
<div class="paper-source__venue">Matt Chat 225 and 226</div>
<div class="paper-source__detail">Matt Barton · two videos, 28:30 and 31:44</div>
<div class="paper-source__id"><a href="https://www.youtube.com/watch?v=t5tJQ3cqRmc">youtube.com/watch?v=t5tJQ3cqRmc</a><br>
<a href="https://www.youtube.com/watch?v=MjjRfz2_dCs">youtube.com/watch?v=MjjRfz2_dCs</a></div>
</div>

Glenn Wichman talks to Matt Barton for his show Matt Chat, in two episodes. The first covers
his start in games, meeting Michael Toy in the Santa Cruz stat lab, how Rogue passed from Toy and
Wichman to Toy and Ken Arnold at Berkeley and then to Toy and Jon Lane at A.I. Design, the
tic-tac-toe dungeon and the "Mars bug". The second covers Rogue on BSD Unix, the Epyx deal and
what Wichman was paid, the Macintosh and Atari ST versions, roguelikes and Diablo, and his later
work: Mavis Beacon Teaches Typing at Software Toolworks and the Macintosh shareware games
Mombasa and Toxic Ravine.

See also the [2016 panel with Michael Toy and Ken Arnold](rogue-panel-2016.md) and the
[2021 interview with Glenn Wichman](wichman-interview-2021.md).

> **About this transcript.** Made from YouTube's automatic captions and lightly edited for
> readability: punctuation added, false starts, repetitions and filler words removed, and obvious
> mishearings corrected (names and titles, *Wichman*, *Epyx*, *Jon Lane*, *Olivetti*, *Gygax and
> Arneson*, *Mavis Beacon Teaches Typing*, *Steve Wozniak*). The wording is otherwise as spoken,
> slips included; words in [brackets] were supplied. The captions do not say who is speaking:
> Matt Barton introduces each episode, asks the questions and ends with his ale of the week, and
> Glenn Wichman answers; a new paragraph, or a dash, marks where the speaker changes. Chapter
> titles are YouTube's; each timestamp links to that point in its video.

## Part one: Introduction to Rogue

*Matt Chat 225, published 26 January 2014.*

[**0:17**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=17s) Hi guys, welcome back. This is Matt Chat episode 225, featuring the first of a brand new series of interviews with one of the creators of Rogue, Mr. Glenn Wichman. Now, Rogue, as you probably know, is one of the most historically important of all computer role-playing games. It introduced the procedurally generated dungeons, so that no two games are ever the same. It's really great stuff, and it really holds up well today. There's still many, many people who still play Rogue and any of the thousands of roguelikes and spin-offs out there.

[**0:41**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=41s) It's really great stuff. Anyway, we've got a lot to cover here, so without further ado, here is Mr. Glenn Wichman. All right, folks, I am here with the great Glenn Wichman. He is the co-creator of a game you've probably heard of if you know anything about computer role-playing games, namely Rogue.

## Background and inspiration

[**1:00**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=60s) He's a game designer and engineer, and now he's working at Zynga. How are you today, Glenn? — I'm doing just fine, thanks. — I always like to start by talking about the background. What brought you to computers?

[**1:14**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=74s) How did you learn how to program? What got you into game design? Maybe you can just set the stage as far back as you can remember. — Well, as far back as I can remember, which is like when I was seven, I wanted to either be a board game designer or a cartoonist when I grew up.

[**1:36**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=96s) So my intent was to design games, board games. And then when I got to college and first ran into computers, I started playing computer games — Adventure, and the very simple text-based games that they had on the Unix systems at college. And I went, "Wow, the computer can do all the boring parts for you." Then I think, "I'd like to design computer games," and so then, "I guess I'd better learn how to program these things."

[**2:21**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=141s) So that was the impetus into it: it was just a way to make my games easier to create and play. — You said you played a lot of Adventure. For folks who don't know, of course, that's the text adventure game. I think it's Will Crowther. Who was the other guy on that? — Yeah. Don… Don something.

[**2:40**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=160s) So what fascinated you about that game? — Well, like many geeks growing up in the 70s, I was a D&D player, and [a] reader of Tolkien and C.S. Lewis, and going to Renaissance fairs and stuff like that. So just the… — Oh, so you were the full package, then.

[**3:14**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=194s) Well, there were certainly people who were much more dedicated than me. I didn't make my own costumes or anything like that, but I enjoyed that medieval fantasy, and the interactive fiction. It was a fun thing to do, to sit down and imagine yourself in these scenarios — rather than just reading what other players are doing, imagine yourself in this scenario and think of what you would do. Which is, again, a lot of what Dungeons & Dragons was about.

[**3:52**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=232s) So [it] was the same thing, but you didn't have to get a bunch of people together. You could just sit down in front of the computer and do it. — Coming back to Adventure, it seems like I read an interview where you said you never actually beat the game. Is that still true? — I can't remember if I beat Adventure. I never beat Rogue; that was the thing that I remember saying in an interview. I can't remember if I ever beat Adventure.

[**4:26**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=266s) I may very well have, but that's one where you can just keep pounding away at it until you figure everything out. So I imagine sooner or later I got it. But I was never as good at playing games as I was at creating them. — Yeah.

## Early game development

[**4:46**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=286s) It seems like one of the problems for games like Adventure is, of course, once you do beat it, there's little reason to go back and play it over again, right? — Yeah. Which was kind of the whole point behind Michael and me creating Rogue: to create a game that we could enjoy playing.

[**5:11**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=311s) So you weren't playing any of the games at the arcades at the time? — No… Pong, or I guess Pac-Man, that sort of thing. Asteroids, which I never got very good at. And Centipede, and Galaxian, all of those sorts of games. I was pumping quarters into machines when I had the chance, when I could find some quarters. — Were you interested? Did you want to make games like that, or were you more drawn to the computer side of the… — Yeah, I wanted to make any kinds of games.

[**5:46**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=346s) At the time, again, what I had available to me — people didn't have their own computers in those days. In high school I didn't even know anyone who owned a computer, and then in college I met a couple of people who had built their own. But for the most part, the computers I had access to were Unix machines, minicomputers off in a room somewhere, and all I had was a dumb terminal. So I didn't have any graphics capabilities or color.

[**6:19**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=379s) I had ASCII characters and a screen, and that was it. But yeah, I liked the idea of trying to do graphical games, and did what I could with what I had, and got more into that later when I had an Atari 400. But that was several years later.

[**6:49**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=409s) Well, the Atari — was that your first computer? — The Atari 400, first personal computer. I was living in a house with a bunch of guys, and there was an Atari 400 there. I can't remember who actually owned it, but it was there for me. And so, yes, I played with that some, and did some Q*bert-like games and stuff like that. None of that was commercial. That was just stuff I did for my own entertainment in my spare time.

## Creating the team

[**7:28**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=448s) Let's talk about when you got to college and you met Michael. What was this meeting like? — Oh, well, I was in what [was] called the stat lab, which was where the computer terminals were. And I was trying to teach myself BASIC, and I was writing a really poorly programmed text adventure game. And he walked in and looked over my shoulder and saw what I was doing and said, "What is that?" And I asked him if he'd heard of Adventure, and he talked about how he had beaten it long ago.

[**8:14**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=494s) And so then we sat down and started talking about games and how to program them. So then, I don't know, we ended up just working on a lot of stuff together, becoming really good friends. — So what about Ken Arnold and Jon Lane? — Okay.

[**8:41**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=521s) Well, so yeah, that came later. So this is where the history of Rogue was Michael and me, and then Michael and Ken, and then Michael and Jon. So Michael's the constant, and the four of us never really worked together as a foursome. It was Michael and each of us. So Michael and I were at UC Santa Cruz. Ken Arnold was at Berkeley, and he was the one who developed this library of routines in C called curses. — Why do they call it curses, by the way?

[**9:20**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=560s) Because it allowed you to do cursor addressing, to place the cursor at a specific point on the screen. So normally, whatever letter came up next that was sent to the terminal would just come out at the bottom left-hand corner of the screen and work its way across. So most terminals had the capability to send it a special escape code to put a character at any point on the display, but all terminals — and there were a bunch of different brands — they each had their own capabilities.

[**9:52**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=592s) So Ken was the one who just put together a library that had a database of "if this is your brand of terminal, this is the escape code that you need to send," and made it so that the programmer didn't have to special-case each of those things. So he had written that library, and we got ahold of it, and that was where we realized we had the technology to do much cooler games on these terminals than text adventures: that we could actually use the letters as graphics.

[**10:37**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=637s) So we got started doing Rogue, and then Michael and Ken started corresponding by email, and then Michael ended up transferring from Santa Cruz to Berkeley. So at that point the center of gravity of Rogue development moved to Berkeley. And there was not, like, GitHub or anything like it in those days, at least not that we had access to. Rogue wasn't under any sort of source control system where I could check in and check out files.

[**11:08**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=668s) So once he left, I was working on it in Santa Cruz; he and Ken were working on it in Berkeley, but we were working on separate versions at that point. So that was where Ken came into the picture, and Ken rewrote a lot of [the] interface and came up with a lot of different ideas. Jon — Michael met Jon in Italy. So both Michael and I left college and got jobs with tech companies, without bothering to graduate, which was fairly common in those days.

[**11:50**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=710s) And Michael ended up working for Olivetti, went to Italy; that's where he met Jon Lane. And Jon was the one who came up with the idea of making a commercial version of Rogue for the IBM PC. And so that was where Jon got involved. And because the code base that Michael and I had written — we wrote [it] at the University of California, with their equipment — we didn't really have the rights to that. And so Jon basically rewrote the game from scratch, changed the monsters so that we weren't infringing on any of Gygax and Arneson's intellectual property, and basically made it into something that we could sell commercially.

## Open source philosophy

[**12:49**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=769s) So when you and Michael were first working on this, nobody had any ideas about selling this thing eventually, or making a profit out of it? I mean, why did you make it? — We made it because we'd played all of the adventure games that were out there and we wanted to play more. And we had this idea of doing one that was graphical, and again, doing one where the computer would come up with the adventure.

[**13:14**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=794s) Because we'd created a bunch of text adventure games, and I had written a program in Pascal that allowed you to create your own adventures, and so all of my friends, even the non-programmers, were creating different text adventures. — [Do you] remember the name of that?

[**13:38**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=818s) Oh, I don't remember it. It was called Dome World, because that was the first game that I had created with it. And again, that was never released commercially. That was just passed around amongst college buddies. Anyway, again, we wanted to do this thing where the computer would come up with the adventure for us. And yeah, I can't remember if, when we were doing all of this, we thought, "Okay, someday we'll do this commercially." There wasn't a commercial market for Unix games.

[**14:20**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=860s) Nobody had Unix computers. And so, yeah, I don't think, at least, I was thinking that far forward. — [I've] been reading that book Hackers again, that one from Steven Levy. — Yeah, I don't think I read it, but I'm familiar with the book. — One of the things he goes on about in here — and I think you see the same thing with Richard Stallman, the Free Software Foundation, that kind of thing — they paint this picture of that time as everybody's just sharing code.

[**14:51**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=891s) They're free; everything, all the software, is free, and that was actually a more fertile environment for innovation than, I guess, the later commercialization of it all. Would you agree with that? — I keep going back and forth on that. I've been thinking a lot about it, and the question of how you get something that's economically sustainable if there's no money coming in from somewhere, I think, is an interesting question. But I think the amount of open-source software that's out there that people just use nowadays — there's a lot of really good, useful things.

[**15:44**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=944s) And it does seem to manage to be sustainable. So I think for tools and other things that all of us software creators are sharing with each other, it makes sense. I think for end-facing consumer products, it still makes sense to have a commercial model where you bring in revenue somehow. And I think what is the best way to bring in revenue for a game is still a big, wide-open question.

## Procedural generation

[**16:21**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=981s) So tell me about how you came up with this procedural generation concept. It's pretty high-concept stuff, it seems to me. — Yeah, I don't think it was — I think it was really, again, just based on: we wanted a game that we could play. We were tired of — if I created the game, then you could play it, but then if I wanted to play one, I'd have to wait for you to write one.

[**16:43**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1003s) So it was really as straightforward as that. And once we latched on to that idea, then figuring out the details of how you make that work, I think, involved a lot of creativity and a lot of problem solving, and a lot of running into things that nobody that we knew of had run into before.

[**17:20**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1040s) So it was a lot of fun, and we really felt like we were creating something pretty new and exciting. — Can you give me an example of one of those moments when you realized that you're on your own new frontier?

[**17:42**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1062s) Well, I think just when we sat down and we had an idea in our mind of what we wanted level generation to look like. And again, we were 19 years old. Michael had more experience than me in programming; he'd been doing it in high school. I was really just learning. But we're looking at this problem of, okay, we've got this screen, 80 by 24 characters, and we want a level map, a dungeon level like we have in Dungeons & Dragons. And I think initially in our minds we had something much more wide open in terms of what we'd like the computer to be able to do.

[**18:30**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1110s) We ended up with something that was really extremely simple. It was just a tic-tac-toe board. Every level in the original Rogue has nine slots for rooms, laid out in a 3×3 grid. But a room could actually be minimized to just one piece of corridor, or a room could be missing, right? And so we ended up with a very simple algorithm, not because we thought it was a good idea, but just because everything we tried that was more complicated, we ended up not having enough smarts to implement.

[**19:06**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1146s) But we did come up with something that I think gave the illusion of being much more deep than it really was, and gave enough variation that there was unpredictability, and there was a sense of exploring, and that you could find something on a level that you weren't expecting. — It seems like one of the hard challenges, to me, just thinking about the game, would be to make sure that all the dungeons had all the rooms connected with exits, and you could actually get to the lower levels and so on.

[**19:40**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1180s) How hard was that to actually program? — We got in so much trouble with our friends. One of the great things that we had was a room full of people who were eager to play whatever we came up with next, which is all the people who hung out at the stat lab.

[**20:08**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1208s) So we did have a bug where every now and then you would drop down a level and you'd be in a room that didn't connect to anything. And it ended up being called the Mars bug. I don't remember exactly why, but it was infamous: we'd hear screams coming from somebody who'd gotten down to level 20 and had a really great character, and everything was looking good, and then they ran into the Mars bug and they were just doomed.

[**20:43**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1243s) So we didn't do it perfectly. We finally got that one solved, but it was not straightforward.

## Adrenaline and immersion

[**20:58**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1258s) So what's your favorite gameplay story of Rogue? Something unpredictable that you talked about. — It was very interesting to feel the surge of adrenaline that you would get when you saw a T appear on the screen, right? Because it was a troll, and that was, as you got down levels, the first really threatening monster, if you were doing well. It's like, "Okay, I don't know if I'm going to beat this guy." And then I would sit back and I'd go, "I'm looking at a letter T on a CRT screen," right?

[**21:31**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1291s) But my adrenaline is going. So that was fascinating to me: how much you could really get into the game even when it's completely abstract like that. And to watch people hitting the keys harder, hoping that would help them beat the monster! These were computer scientists. They knew that hitting the keys harder was not going to make any real difference, but they did it anyway, because you were into the game at that point.

[**22:11**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1331s) Yeah, that story really, to me, brings home the point that you really don't need these advanced graphics. All these new consoles always talk about how great the graphics are going to be and so on, but, like you say, you got the letter T and get just as great of an adrenaline rush from that.

[**22:20**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1340s) Why do you think that is? — I don't know why it is. If we had the tools and the capabilities to do something with really great graphics, we would have. It certainly wasn't anything on our part where we thought, "Oh, we don't need these fancy graphics." They just weren't an option. But I think it is interesting. In a lot of ways I think it's like reading a book. If you read a Stephen King novel, right, it's not the same thing as seeing a Stephen King movie, but you still can have — your imagination fills in all of the blanks.

[**23:10**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1390s) Which in some ways I think is better, because each person can fill in the blanks in their own way.

## Wrap up and Patreon

[**23:30**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1410s) And that's all for this week's episode. I hope you guys enjoyed that. I should be back next week with part two of my interview with Mr. Glenn Wichman. Lot of great stuff coming up; we've barely scratched the surface of this thing. So stay tuned. A lot of great stuff; you're definitely going to enjoy it. As always, I want to thank you very much if you have supported me in my efforts to keep this show on the YouTubes, as it were. If you'd like to support Matt Chat, don't feel like you have to give me a lot of money.

[**23:55**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1435s) A dollar per episode is fine, whatever you can afford and you feel comfortable with. When you're ready to support the show, just go to mattchat.us. Look for the handy-dandy "support the show" link. You can set up a subscription, one-time payment, whatever works. Guys, I really, really appreciate it. Some of you guys have been suggesting that I look into this site called Patreon, or Patreon. I have been looking at that. It's very interesting. I'll definitely, hopefully, have a chance to roll out my own Patreon site soon, but in the meantime, there's always PayPal.

## Ale of the week

[**24:26**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1466s) Now, what about that ale of the week? Well, what else am I going to choose but a Rogue ale? Rogue's one of the best brewers out there. They've got lots of varieties, so [I] thought it'd be fun during this interview series to stick with their various brews from Rogue.

[**24:50**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1490s) Let's see what it says. They tell you what the ingredients are: Carawheat, Crystal and Perle hops, free-range coastal water and Pac-Man yeast. Well, if they're kidding about Pac-Man yeast, that's kind of cool. I didn't know there was such a thing. Guess there's a lot of retro gamers that are into brews. What else do we have here? "Citrusy, pale orange in color, citrus grapefruit aroma." 15° Plato, whatever that means. 76A again, whatever that means. 59 IBU.

[**25:25**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1525s) I don't actually see the percentage of alcohol in here, [which] is what I usually look at, so [I] really have no idea how that translates. But hopefully this will be okay. Now, also, I want to let you know that we now have a complete spreadsheet of all of the ales I've tried on the show, as well as the ratings and where they're brewed and so on. And that's mostly thanks to a viewer named James Dunn, who helped me. Some other folks helped out, but this guy really came forward and pretty much did the whole thing himself.

[**25:49**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1549s) So anyways, if you find that useful, say thank you to James Dunn for that. I definitely thank him. Anyway, let's get this Brutal open and see what it's all about. All right, so I've got some of this Brutal IPA here in the rather excellent drinking horn. I've been smelling this, and I'm really trying to give this a good snort, but I just don't really smell a lot coming off of this. It's a little bit of a lemony scent to it, but not a really strong aroma to it at all.

[**26:20**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1580s) Maybe a little bit of a citrus-peachy thing. Anyway, let's give it a taste. What is that? So you get a little bit of coffee, a little bit of nuttiness, kind of what you'd expect from an IPA. It's not very bitter, actually. It's a little bit bitter at first, but then it quickly goes away. You get a fairly nice aftertaste to it. I got to say, though, I'm very surprised that they would call it Brutal, 'cause it's really not much flavor to it. It's actually very light, maybe more on the refreshing side than the sucker-punch side.

[**27:03**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1623s) Anyway, let me give it another taste. Yeah, just not a lot of flavor here. It's very light and, you know, watery even. Again, really surprised. Usually Rogues are very full of flavor; they're very full-bodied ales. This one is very tame. One more taste.

[**27:21**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1641s) Yeah, it's just not doing that much for me. It's not bad, but there's just so many better IPAs out there, and I'm a little concerned that they would call this Brutal when it's in fact quite kind of wussy.

[**27:42**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1662s) Anyway, I'm going to go one out of five drinking horns on this. Again, not a bad choice, but there's just so many better IPAs out there, and life is short, so what can we say?

## Closing remarks

[**27:54**](https://www.youtube.com/watch?v=t5tJQ3cqRmc&t=1674s) Okay, let's wrap this up with a quotation. So for the quotation this week, I was looking for quotes about rogues. There's actually a lot more than I expected to find. I really like this one from author Henry Fielding, though. Goes something like this: "A rich man without charity is a rogue, and perhaps it would be no difficult matter to prove that he is also a fool." See you guys next week. — Tell him about the Twinkie. — What about the Twinkie?

## Part two: Rogue success and fame

*Matt Chat 226, published 2 February 2014.*

[**0:16**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=16s) Hi guys, welcome back. This is Matt Chat episode 226, featuring part two of my interview with Mr. Glenn Wichman, the co-creator of Rogue, one of the most important computer games of all time. [In] this part of the interview we talk more about Rogue, including the commercial release by Epyx. Then we get [into] his later projects, including a couple of shareware games for the Macintosh that I think you'll find very interesting.

[**0:31**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=31s) Anyway, we've got a lot to cover here, so without further ado, here is Mr. Glenn Wichman. So after you got the game finished, you're sort of the big man on campus? Were all these people coming up to you and saying, "Oh, wow, look, this [is] the guy that did Rogue," or "one of those Rogue guys"? I mean, did you have a measure of fame from this? — Yeah, the fame part was interesting, because it came and went and then came again.

## The resurgence of Rogue

[**1:03**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=63s) But I remember going into a software store, once we had the commercial version, and seeing it on the shelves, and going, "Oh, there's my game." And then one of the people who worked at the store came up: "Wow, that's your game? So why didn't you show up in a limo?" So yeah, there was a measure of fame on campus, I mean among the people who were there writing games. Michael and I had what everybody, I think, agreed was the coolest game at that point.

[**1:50**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=110s) So that was fun. And then, as time went on, all of that faded, and there came a point where I didn't even have it on my résumé anymore, because nobody had heard of it, so there wasn't any reason to have it on there. And then, starting maybe just a few years back, all of a sudden everybody had heard of it again. [It] took me a while to figure that out, and I think I've at least got a theory as to what happened there. But it's been fun to have a little bit of a resurgence of that, after lo these many years.

## Rogue on BSD Unix

[**2:40**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=160s) Okay, then let's hear the theory. — So my theory is that when I was in college, there were no game design courses; that just didn't exist as a discipline. And now I'm realizing that there are all of these colleges that are teaching computer game design and history of computer games. And so people who are my age have heard of me because they played Rogue in college, and people who are in their 20s, they learned about it in college. But there's this gap in between, of people who have never heard of Rogue, but they've heard of Mavis Beacon Teaches Typing.

[**3:28**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=208s) So I get to be famous for that one, for them. — Oh, seriously? I mean, not to knock the typing thing, but really, people know you more for that than for Rogue? — Well, people of [a certain] age, yeah. — How did it end up being distributed with BSD Unix?

[**3:45**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=225s) Well, that was because of Ken Arnold and Michael being at Berkeley. That department got to decide what went on BSD Unix, and they put Rogue on. And it ended up being a program that exercised most of the facilities that you needed to make sure that your installation was correct.

[**4:18**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=258s) So the thing is, you would install BSD Unix, and then if you could play Rogue, you knew that your installation had been good. So I guess that was the excuse for why it was there. — Yeah, that's always just seemed so awesome to me, to have a game so good that they actually include it with the operating system.

## The Epyx commercial deal

[**4:36**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=276s) So how did this deal with Epyx come about? — Well, we knew people who worked at Epyx. There was a guy named Scott Nelson, who was one of the guys who hung out at the stat lab, and he worked for Epyx, and he got us introduced to people there.

[**5:01**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=301s) So that was Michael and Jon who made that deal. I wasn't really involved in it, so I don't know the details. Initially, Michael and Jon created a company called A.I. Design, which stood for Anything Interesting Design, and so we initially had a boxed version of that we were trying to sell ourselves. — Do you still have any of those boxed copies? — No, I don't, but I bet Michael does. — Those have to be some pretty serious collector's items.

[**5:40**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=340s) Yeah. I'll ask Michael about it. I've got one of the Epyx boxes still, but I don't have any of the original A.I. Design ones. So yeah, at some point they were producing it in Jon's garage and shrink-wrapping it themselves and shipping it off to stores, and then decided that was not scalable. And so we made the deal with Epyx. At that point we had the PC version, and that was the only version that we had, and Epyx paid for us to do versions for Macintosh initially, and then later Atari ST and Amiga and CoCo. But strangely, those versions didn't really sell that well. — Right, the ones for personal computers.

[**6:32**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=392s) I was wondering what your thoughts are on that. Just bad marketing, or what? — Yeah, it's an interesting question. There was a point — and I think you mentioned this in your book, and I think Richard Garriott shot down the idea that it was piracy, because obviously there were games created at the same time that did do well commercially. But ultimately Epyx, the whole company, ended up failing. And so I think piracy was a big problem in the industry. I think that Rogue was massively popular on Unix computers. It became fairly famous in that very academic circle of people who played games on college computers, but I guess — it seemed natural to us that it was just going to therefore be a massive seller commercially. We thought we'd make a ton of money off of it. — But how much money did you actually make off of it personally?

## Financials and competition

[**7:59**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=479s) I made $15,000, and that was the advance on royalties for doing the Atari ST port. So that was the only thing that I was ever paid money for. Oh, and plus I got a Macintosh. So Michael and Jon paid me — when we did the Mac version, that was the first one that we did that actually had tile graphics instead of characters.

[**8:33**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=513s) So I created all of the tile graphics for the Mac version, and my payment for that was I got to keep the Mac that they let me use to create the tiles. — Probably more significant than people may realize, because those Macintoshes back then were, I guess, about the equivalent of five or six thousand dollars today, right?

[**8:51**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=531s) Yeah. It was used, and it was a skinny Mac, 128K of memory, but that was actually probably my first computer that I personally owned and didn't have to share with anybody.

[**9:16**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=556s) So it was a big deal. — One of the things I remember reading about this Epyx release was that, at the same time that came out, there had already been shareware, public-domain versions of Rogue they had to compete with. Is there any truth to that? — I don't know whether there were. On the PC there probably were. There were certainly games like it; there were already roguelikes at that point.

[**9:47**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=587s) So yeah, I think a lot of the people who wanted to play Rogue, they could just play NetHack or whatever at college, so they didn't have a need to have it on their PC.

## The roguelike phenomenon

[**10:12**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=612s) So you brought up the topic of roguelikes. When did these things first start popping up, and what were your thoughts on them? — This was a thing that, I think, by the time I became aware of it, had already been a phenomenon for quite some time.

[**10:26**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=626s) So I was out of the picture for a long time, and the first thing that I had heard about was — [I] somehow came across the Seven-Day Roguelike Challenge, and I don't remember even how I came across that. So that was only a few years ago, less than 10 years ago. And I mean, I knew about Hack and NetHack and some of these other things that were roguelikes, but I hadn't heard the term.

[**10:58**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=658s) So I think it's really cool that they ended up getting named after our game, and I think that's appropriate. I think that a lot of people have created a lot of really neat innovations, and I feel blessed to have been one of the people who got that ball rolling. — On a related note, have you done some of your own roguelikes?

[**11:38**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=698s) Well, I did the Seven-Day Roguelike Challenge once, a few years ago. I did a JavaScript roguelike called the Seven Day Quest, and it had seven environments and seven amulets, and so I did the whole thing based on this idea of seven. And that was pretty fun. — Did you win the challenge?

[**12:02**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=722s) Yeah — so yes, I succeeded. At that point they weren't judging which one was best; it was just: you either had something playable in seven days or you didn't. And I did, and I felt really good about it, because I really did start completely from scratch — no existing libraries or game engines or anything like that — and I came up with the story and all of the graphics and all of the code. And I was working full-time at the time, so [I] really did not have anything like 134 hours to do it in, but I managed to get it done.

## Modern roguelikes and Diablo

[**12:48**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=768s) So you never thought about doing one based on the Bible? — I don't know why I haven't thought about that. I've read the Bible, and there's a lot of interesting stories and adventures in there, but I have not thought about that. But that's a good idea. — Okay, so I have a question here from Maximilian Dimethyltryptamine, I believe that's how you pronounce that. He says, "I want to know if Glenn has any current favorite roguelikes that he likes to play. P.S. My current favorite is Infra Arcana."

[**13:28**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=808s) Well, yeah, I have — shoot, now I need to remember the name of it. I actually just judged a roguelike contest, and there was — so yeah, we'll go back at some point at the end and I'll tell you the name of it and where to get it. But [it] was a very fun, quick little thing that is sort of roguelike. It doesn't have a lot of exploration to it, but it's got a lot of the good visceral feel of a roguelike, and [it's] very simple to just sit down and play it for a while and win or lose. — All right.

[**14:26**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=866s) So I got a question here from Shane's, and I think this might be a joke question, but go ahead and throw it out there and you can decide for yourself. So he says, "Ask him if he's ever going to let Rogue and Gambit smooch." — It's fine with me.

[**14:45**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=885s) Okay. So Diablo — a lot of people say that's a roguelike. Now, I looked at an older interview you did back in '07; you said you never even played the game. Has that changed? And if so, do you agree that it is [a] roguelike? — I still have not played Diablo, but I am much more familiar with it because of David Craddock's Stay Awhile and Listen book, which I read, and that got me to at least watch some YouTube videos of Diablo. I don't have a PC, and Diablo 1 is, last I knew, not available for the Mac.

[**15:32**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=932s) So I haven't played it. I suppose I could go out and get Diablo I, but from everything that I've read — so yeah, I'd certainly be interested in playing Diablo, at least one and maybe two, at some point. That's still on my list of things to do. But I've at least watched some YouTube videos, some walkthroughs of it. So yes, and it's certainly, I think, well documented at this point in David Craddock's book that Rogue was at least one of the big inspirations for Diablo. And again, there's the Matt Householder connection: he was the producer of Rogue at Epyx, and then was also involved in Diablo. — I think it's true for me, and probably for a lot of the viewers here, that you're better off playing Rogue than Diablo I.

## Mavis Beacon Teaches Typing

[**16:30**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=990s) But anyway, let's move on to Mavis Beacon Teaches Typing. It's [a] surprisingly popular game, given the subject matter, I think. You can just tell me how this game came about, and then why you think it had such a great reception.

[**16:46**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1006s) Okay. So I guess — is it even fair to call it a game? I think so. I mean, it had games in it. There was the racing game inside Mavis Beacon, and I had a lot of input into the design of that game. I was the one who pushed for making it first person, with a rearview mirror, rather than an overhead view.

[**17:19**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1039s) So if you're typing faster than the pace car, then you see the pace car in your rearview mirror, and if you slow down, then you see the pace car ahead of you. So yeah, how that came about was: I kept working for A.I. Design, which then later became called Highland Software — so, Michael and Jon's company. But they were doing contract work and working on Microsoft Bookshelf and various things, and I [asked], "Are we going to do any more games?" And they said,

[**18:00**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1080s) "Well, no, games didn't work out too well for us. We're going to do these other things that are making money." And so I started looking for someplace I could do games, so I moved down to LA, started working for Software Toolworks, came to do Mavis Beacon. And again, they already had a PC version; I worked on the Apple IIGS version. But I did get to have a lot of design input in there. One of the things that I'm proud of there was the translucent hands over the keyboard. Their initial design just had this diagram where a finger would stretch out to hit the right key, and I said, "No, we should do this." And then I got my manager really mad at me, because I spent about three days taking pictures of hands and drawing hands. It's like, "We've already got an artist; you're here to write code." But by the time I was done showing them "this is how it should work," then they said,

[**19:02**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1142s) "Okay, yeah, that's a good idea." So I think that was part of what made it successful. I have no idea what makes things win and what makes things lose. I've seen all sorts of great things do poorly and poor things do great.

[**19:18**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1158s) So either I have no good judgment, or the rest of the world has no good judgment, or both.

## Macintosh shareware projects

[**19:26**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1166s) I know you've done some Mac games, Toxic Ravine, and is it Mombasa? I kind of wonder if you could tell me about those games, but also just in general what appeals to you so much about the Mac. — Well, yeah.

[**19:51**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1191s) So I just ended up being a Mac guy for a long time. [I] was never in a position to be one of those people, and so I thought the Mac was going to win. I actually really liked the Atari ST, and if that had won, I'd have loved to [have] kept working on that, even though it was cheesy in a lot of ways. I had a certain affection for it after having done the Rogue port for that. But anyway, I ended up with a Macintosh; that was just the computer that I owned. And so in the late 80s, game software was really transitioning from a thing where a person could create a game to something where you had to spend a million dollars and have dozens of people. And so I did some shareware.

[**20:56**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1256s) Well, there was shareware around, and I wanted to test out the theory that I was wishing was true, right? There was shareware, but it was mostly really amateurish stuff, and then there was commercial software that you needed a whole team of people to do. So there was a game — Mombasa was one of many shareware knockoffs of a game called Shanghai, which was based on mahjong. And so there was a Mac shareware version of it called GunShy, which I was playing and my wife was playing, and we really liked it, but I thought,

[**21:42**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1302s) "Oh, I could do much better than this." And so that was why I decided to do Mombasa, and then just see how it would work as shareware. And Toxic Ravine — there was an arcade game called Canyon Bomber that I pumped quarters into, and that was in college. At the same time that I was doing Rogue, I did my knockoff of Canyon Bomber that ran on a dumb terminal [and] used the same curses library as Rogue did. And so Toxic Ravine was — Canyon Bomber was really simple: all there was [was] rocks to blow up. And then Toxic Ravine was me taking that idea and running with it and saying,

[**22:36**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1356s) "Well, what if every rock did something different when it got hit by a bomb?" And so again, there I was, I had my Mac, and I put that together to see. I did all the sound design, graphic design, game design, programming; there was nobody else involved in Toxic Ravine aside from people playing it and giving me feedback. It was just purely my own thing, and I wanted to see what I [could do] with that. So [I] put it out there as shareware [and] probably got 50 people or so to write checks.

## Shareware distribution

[**23:24**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1404s) But one of them was Steve Wozniak, so [I] didn't cash that check. I have [a] check signed "Wozniak," and I thought, "Oh, I'm keeping this one." — I was wondering why — it seemed like he'd be making a lot more than that. But I guess it wasn't a very large Mac shareware community. — You know, I don't know.

[**23:46**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1426s) How did you do the shareware part of it, by the way? Was it you get to play so long and then you pay, or is it just…? — [It] wasn't nagware in any way. It was just purely based on the honor system. It was: if you like this game, write a check and put it in an envelope with a stamp, and here's my address — which was actually my parents' address, because I was still moving around too much in those days.

[**24:10**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1450s) So I didn't think that the letters would find me. There wasn't anything like PayPal or things like that, to make it really easy to just click a button and donate. — Well, all those people out there that played Toxic Ravine and Mombasa, now's the chance to pay up, right?

[**24:46**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1486s) So I saw… — Oh, sorry, what? — Say that address isn't any good anymore. — So that's… Well, what if they send it — they could PayPal you, right? — Yeah, sure. I'm easy to find.

## Final thoughts and beer review

[**25:05**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1505s) And that's all for this week's episode. I hope you guys enjoyed that. I should be back next week with part three of my interview with Mr. Glenn Wichman; that'll probably be the final installment with him. [I've] got a lot of great stuff to cover, including stuff for aspiring game designers.

[**25:20**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1520s) So stay tuned; a lot of great stuff. As always, I want to thank you very much if you have supported me in my efforts to keep Matt Chat on the air. You probably know by now I've set up this Patreon site. It's really a lot of fun; a lot of you guys have already jumped on the bandwagon there. If you're donating via PayPal, if you want to continue that, fine, of course I appreciate that, but you might want to check out this Patreon stuff. There's going to be some special perks for people who support me on Patreon, including a members-only podcast.

[**25:48**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1548s) So I know you guys will enjoy that. And by the way, if you [have] ideas for the podcast, or maybe you want to be on the show to chat with me, let me know. Maybe we can set something up. A lot of that stuff is still in the drawing-board phase at the moment, so [I'm] really happy to hear all of your suggestions. And again, thank you very much.

[**26:05**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1565s) Now, what about that ale of the week? Well, this week I've got a brew submitted by a fan. This is a fan named Masacus, from Colorado Springs, a lovely place. He says, "Dear Matt, enjoy the brew. As a return —" ah, there'd be a catch "— as a return, thanks. Maybe one day you can do a retrospective on Dark Sun: Shattered Hairdo." I think that probably means Dark Sun: Shattered Lands. Shattered Lando Calrissian.

[**26:48**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1608s) Anyway, I think I know what game [he] is talking about. Thanks. Well, thank you, Masacus. I've been wanting to look at Dark Sun for quite a while now, so hopefully we'll have that as the next retrospective. But anyway, more importantly, let's check out that ale you submitted.

[**27:04**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1624s) All right, this one is the — what the hell is this? Oh my God, is this a fishnet for an ale bottle? I think I can put that on. I think Elizabeth will really be turned on by that. Hey, maybe I shouldn't be showing you guys this. Thank you very much, Masacus. I don't really know where this thing has been. Okay, what do we have here? Whoa: Lagunitas Hop Stoopid ale, brewed and bottled by the Lagunitas Brewing Company from Petaluma, California. Alcohol 8% by volume. A really lovely label on this one. [One] pint, 6 fluid ounces.

[**27:51**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1671s) Well, there['s] a whole paragraph of text back here. "Give it to Mikey, he'll drink anything. Up the bomber went in toast, then to his lips, and what happened next could not have been foreseen: a Hop Stoopid, a slick, Re-Animator green fluid ooze from the bottle." I love that movie, Re-Animator.

[**28:14**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1694s) Anyway, I'm not going to read this whole thing to you. That's [a] fun story, though. Let's see what else we can find out about this. 8% alcohol by volume, 102 IBU for you. Oh, they even have the pronunciation here: Lagunitas. No, "lagunas"? Lagunitas, lagunas — I'm having enough trouble already, and [I] haven't even got the damn thing open.

[**28:37**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1717s) Anyway, let's get this open and see what it's all about. All right, so I've got some of this Hop Stoopid here in the rather sexy drinking horn. I don't know if you can see this, but [I] found a use for Masacus's little fishnet holder thing. It's quite svelte.

[**29:01**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1741s) Anyway, let's give this a sniff. Smells kind of like leather chaps and maybe some chains. No, just kidding. As I would expect, a lot of hoppiness to this. With a name like Hop Stoopid, you really would expect a really strong aroma and presence of hops. I can definitely tell that from the scent of this thing. Very nice, though, not overpowering. It's quite refreshing-smelling, actually. But anyway.

[**29:23**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1763s) Let's give it a taste. And I need to make a toast here to Masacus, obviously, but also to Mr. Brian Fargo, who has stepped forward to support the show in a really major and impressive way. So thanks to everyone, but here's a toast to Mr. Brian Fargo. Wow, that's a really vibrant one here. Got a lot of citrusy flavors to this. It's very sort of peachy, sort of peaches-citrus. The bitterness — considering how hoppy it smells, I was expecting something really bitter, but [I'm] not really getting any bitterness here. Maybe just a little, just enough; it's just the right amount of bitterness to make this flavor more complex. Let me try it again.

[**30:21**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1821s) Yeah, just a really exquisite flavor on this. All those combinations of the bitterness and the citrusy flavors, the hoppiness: it's just very perfectly blended here, a really good mix. No one flavor overpowers the other. It's just really nice. I think I could tell Masacus here has really great taste when it comes to ales. [I'm] going to have to give this one more taste.

[**30:46**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1846s) Yeah, just really good stuff here. Maybe just a little bit of lemon, a little bit of maybe a slight nutty taste, but all in all really excellent stuff. I'm going to go, of course, a full five out of five drinking horns on this Hop Stoopid. If you're lucky enough to find this one, I definitely recommend you check it out. It's really good stuff, and thank you again, Masacus.

[**31:10**](https://www.youtube.com/watch?v=MjjRfz2_dCs&t=1870s) All right, let's wrap this up with a quotation. The quotation I found this week comes from Benjamin Disraeli, and it goes something like this: "The greatest good you can do for another is not just to share your riches, but to reveal to him his own." See you guys next week. — I fart in your general direction.
