---
title: Roguelike Radio: Rogue, with Glenn Wichman
summary: Glenn Wichman on Roguelike Radio's episode about Rogue, April 2012, transcribed.
hide_summary: true
---
# Roguelike Radio: Rogue, with Glenn Wichman

<div class="paper-source paper-source--conference">
<div class="paper-source__kind">Podcast</div>
<div class="paper-source__date"><span>April</span> 2012</div>
<div class="paper-source__venue">Roguelike Radio, episode 31</div>
<div class="paper-source__detail">Ido Yehieli, John Harris, Jordan Starkweather, Keith Burgun and Michael Brough · audio, 1:04:14</div>
<div class="paper-source__id"><a href="https://www.youtube.com/watch?v=U-F3_pNq-24">youtube.com/watch?v=U-F3_pNq-24</a></div>
</div>

Glenn Wichman joins the Roguelike Radio podcast to talk about the game that named the
genre: how he and Michael Toy started Rogue at UC Santa Cruz with Ken Arnold's cursor
package, how Rogue spread with BSD, A.I. Design and the IBM PC version, the Macintosh,
Atari ST and Amiga versions for Epyx, the Dungeons & Dragons roots, the size of the pack and
the food clock, permadeath and saved games, the identification system, Rogue in Japan, where
the name came from, and his own Seven Day Roguelike, *The Seven Day Quest*. The episode first
went out on 20 April 2012 on [roguelikeradio.com](http://www.roguelikeradio.com/2012/04/episode-31-rogue-with-co-creator-glenn.html); the
video is a fan's re-upload of the audio, made in 2022.

See also the [2016 panel with Michael Toy and Ken Arnold](rogue-panel-2016.md) and the
[2021 interview with Glenn Wichman](wichman-interview-2021.md).

> **About this transcript.** Made from YouTube's automatic captions and lightly edited for
> readability: punctuation added, false starts, repetitions and filler words removed, and obvious
> mishearings corrected (names and titles, *Roguelike Radio*, *Podtoid*, *Rogue*, *Epyx*,
> *Jon Lane*, *NetHack*, *Chunsoft*, *Shiren*, *ToeJam & Earl*, *Greg Johnson*, *ne'er-do-well*).
> The wording is otherwise as spoken, slips included; words in [brackets] were supplied, and
> *[unclear]* marks words the captions lost. There are six voices, Glenn Wichman and the five
> hosts, Ido Yehieli, John Harris, Jordan Starkweather, Keith Burgun and Michael Brough, and the
> captions do not say who is speaking, so neither does this: a new paragraph, or a dash, marks
> where the speaker seems to change. The chapter titles are YouTube's; each timestamp links to
> that point in the video.

## Intro

[**0:00**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=0s) Hello, and welcome to episode 31 of Roguelike Radio. Today we'll be talking about the original Rogue. On the show we have Jordan of the Podtoid podcast from Destructoid, John Harris, Keith Burgun, Michael Brough. So, for anybody who doesn't know, Glenn was one of the three original creators of Rogue, so this is quite a milestone for us, to have you over.

## How Rogue got started

[**0:28**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=28s) Maybe you want to start by telling us a little bit about how Rogue got started, how it got developed, and how you got the idea for making it?

[**0:35**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=35s) All right. Well, so this was 1980, at the University of California, Santa Cruz. My roommate Michael Toy and I were both at college, studying different things, but both involved in computers — which, in those days, most people didn't have their own; people didn't have laptops.

[**0:59**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=59s) So we would go to the computer lab and play on terminals that were connected to mainframe computers that were off in another room. And we were into Dungeons & Dragons and role-playing games, and there were some computer games inspired by that; Adventure's the one that's, I think, most well known. And we got involved with Ken Arnold, who was at Berkeley, [and] had put together a software package that made it easier to put characters anywhere on the screen of a terminal. These terminals didn't have graphics capabilities, most of them, just text, which is how the text Adventure was done. And so we decided we could make a graphical Adventure program.

[**2:02**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=122s) So that's kind of how it began. We got this package of routines to do cursor addressing and tried to look at all of the things that we could do with it. So we did Snake as the game, and then we thought, can we make an Adventure game here? And [we] kind of dove in and spent lots of time doing that when we should have been studying.

— That's so awesome.

## Commercialization

[**2:25**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=145s) And at some point you try to take it into a more commercial direction, right?

[**2:34**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=154s) Yeah, that was actually several years down the road. I can't remember what year now. But there was a point [when] Michael transferred to Berkeley, and so then he and Ken were working on it directly together. I was a little bit less involved at that point; I started working at a company called Fortune Systems that was trying to be what Sun Microsystems ended up succeeding at being. And then, at that point, the game had been written for Unix, and it became part of the Berkeley Standard Distribution, which is how it got well known and spread around the world: it came with the operating system, which is a great way to get your game lots of exposure.

[**3:25**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=205s) So that was just a stroke of luck there, that part. And so then Michael was working in Italy for a while with Olivetti, and there's where he met Jon Lane, [and] they decided to port it to the IBM PC. Personal computers were really just starting to be a thing at that point. And so Jon did the IBM PC version, and then they decided that they could take that commercial. So they put together the company A.I. Design, which originally released Rogue in a cardboard box and shrink-wrap and on store shelves. And that was pretty much the two of them doing their own little shop.

[**4:21**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=261s) And was that still the ASCII version, or was that already with graphics?

[**4:21**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=261s) No, that was still completely ASCII. I don't think we ever did a graphic version for the IBM, except that we had a splash screen that was the four-color graphics they had in those days: magenta, cyan, black and white. But then, once you started playing the game, it was all ASCII. But we did use some of the extended characters.

[**4:51**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=291s) So you were a smiley face instead of an at sign, so it was a little bit more graphical.

[**5:00**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=300s) Yeah, that's the version that I played when I was a kid.

— Yeah, I think that's probably the one that a lot of people are going to think of when they think of Rogue.

## Versions

[**5:07**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=307s) Yeah, actually, I think the one I played was for the Atari ST. That was mine.

[**5:16**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=316s) Oh, cool. That one I wrote, that version, completely. So, a little ways further down the line, we had some friends who worked at Epyx, which was at that time a fairly successful game company, and Michael and Jon had gotten tired of trying to market Rogue on their own, and so we licensed it to Epyx, and then they hired us to do versions. I guess we had already done the Macintosh version, and that was our first version that actually had graphics in it, and I designed all of the graphics for the Mac version in return for a Mac. That was my payment: I got a used skinny Mac. And that was fun, though. We wrote it in Tahoe, because it was winter and Michael and Jon love to ski,

[**6:14**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=374s) So we all went up to a cabin in Lake Tahoe, in the mountains in California, and they skied all day and wrote code all night. So that was a fun time. So that was the Mac version, and then —

[**6:30**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=390s) So we had the PC and Mac version, then we brought that to Epyx, and then they paid us to do versions for Atari ST and Amiga. So Michael was doing the Amiga version, I was doing the ST version. We had a little bit of a rivalry going there, trying to figure out who could put the coolest new features in their own version, and each of us liked our computer better.

[**7:02**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=422s) So I was more an Atari guy; he was more an Amiga guy.

— I thought it was interesting to note that the Atari ST version that I played, which I assume has about the same interface as the Amiga and the Mac version, was actually significantly easier to play than almost all of the modern roguelikes, like NetHack and Dungeon Crawl and all those, because you could control it completely with the mouse. You didn't have to, but pretty much everything you could discover on your own. You didn't need to read through a whole big manual and have 20 different key shortcuts; or maybe you had them, but you didn't have to use them, because you were all mouse-controlled.

[**7:43**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=463s) That's awesome.

— Well, yeah, good. I'm glad you enjoyed that part of it. That was something that I added; part of my value add there was some of those UI pieces. Part of it was because that's the kind of thing that I need when playing a game. I'm not as good at reading through manuals and learning all of the commands,

[**8:06**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=486s) So I wanted to make it easy for myself.

— Well, and I think that's the way most people work. I think it's so cool, this game. It just blows my mind, because you look back, back in the 80s, there weren't books on game design; you didn't have things out here telling you, "This is how you make a game fun." But you can go and play Rogue now and it's still very playable. Obviously, since there's so many games out there that just completely copy it, and they're still super fun to play. I think it's amazing that a game like this could just crop up way back in the days and still be as playable as it is today.

[**8:36**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=516s) I would say, actually, one of the interesting things about it is that — actually, it shouldn't be that surprising, because in a way, you guys, when you were making Rogue, you didn't have this blueprint. Actually, I think that blueprint sometimes causes problems, because all the roguelikes that came after Rogue sort of had to build on top of this already existing structure, whereas with Rogue they were starting from scratch, really, a very new kind of gameplay. And so I feel like when you do that, and you start from scratch, you end up with better design results in general.

[**9:08**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=548s) Yeah, that makes sense.

— I have a kind of concrete question here right now. Glenn, you said that you were completely responsible for the Atari ST version?

— Yes.

— Including the graphics?

[**9:26**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=566s) Well, no. I did the graphics for the Mac version. The graphics for the Atari ST version —

[**9:34**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=574s) Oh, man, I wish I remembered names better, because the guy who did the graphics really deserves to be credited, and it's only that I've got a really bad memory. I can remember him, but I don't remember his name. But he did a beautiful job with all the wall pieces and monsters and creatures in the ST version. He did — the font that we used in the ST version, that I designed.

[**10:11**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=611s) So I think there were two fonts, actually: I had one for big messages, and then another really small font for when you were zoomed out, and both of those were designed as sprites. There weren't font packages on the ST at that time, so they were all just sliced bitmap graphics.

[**10:42**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=642s) Yeah, well, I'm looking at him now. He did a really good job; it's gorgeous.

— Yeah, he did such a good job that NetHack used his graphics set. It's the same; I'm staring at [it], [it] looks like NetHack right here. I'm wondering if they did that on purpose or they got permission.

[**10:57**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=657s) Well, I think once Epyx went bankrupt, all of their assets — there was nobody there to defend them, so it probably all belonged in the public domain. But given the history of how it was developed, I think that it's really hard for anybody to make a real strong claim of having the rights to any part of Rogue.

## Roguelike legacy

[**11:32**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=692s) That's another question I wanted to ask. Well, I'm a younger guy, I'm only 24, so I grew up with the Chunsoft roguelikes on the PlayStation and stuff when I was a kid. But how do you feel, like, the legacy —

[**11:40**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=700s) How do you feel about the legacy that Rogue's left with? All these — you could call them homages, or they built off the original formula, but let's be honest, there's a reason they're called roguelikes: they play almost the exact same. How do you feel about that?

[**11:55**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=715s) Well, I feel honored that the whole thing ended up being called roguelikes, and I think that's appropriate. I think that there was a lot of innovation that we brought that really was the beginning of something. I think that each descendant has added something new, and everybody who's worked on it — I think that for a lot of people it's been a real labor of love, and they've put their own unique features on top of it, or their own unique spin on things.

[**12:36**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=756s) So it's really neat, and very gratifying, to see how many people can take this, because at the basis it's a very simple set of structures and rules, and so that means that there's a whole lot you can do with it, a whole lot you can build on to it, a whole lot of directions that you can take it. So I think it's wonderful to see how many different things have been done over the years from it.

## Roguelike Radio

[**13:09**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=789s) Oh, it's interesting to note: we've had something like 30 episodes until now of Roguelike Radio, and quite often we came to the conclusion that, for almost every game that came afterwards, there's been something that they took from Rogue that actually worked much better in Rogue than in those games. A common example is the food clock, which works really well in a smaller game like Rogue, to just make you hurry up and continue diving into the dungeon, whereas with bigger games, like Dungeon Crawl or Angband or most of the newer roguelikes, it doesn't really work at all.

[**13:51**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=831s) So it's kind of interesting to see how — apparently, I've read a little bit about what you wrote on your homepage, and the Wikipedia page about Rogue, [and] it doesn't sound like there was a whole upfront design doc explaining everything that Rogue is supposed to be. It seems more like you guys were making it up as you went along, and yet it still ended up being something so tight that if you just change a couple of things, something else breaks and doesn't even work anymore.

[**14:28**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=868s) Yeah, it is true, we made it up as we went along. And we were working with a lot of limitations that a couple of years further down the line people wouldn't have, in terms of how much memory we had to run in and that kind of thing.

[**14:44**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=884s) So I think that constrained us in some ways that did keep the game simple. The other thing — I haven't heard the stories; I really need to listen to some of the other episodes of how these other games came about. In retrospect, we had a great group of play testers. These were the days when, if you wanted to be on a computer, you had to go down to the computer lab, where there would be 15 terminals or so, and you would log in and work on the mainframe. So at UC Santa Cruz and at Berkeley, we had groups of people who, as we would come up with a new feature, we'd have a whole lot of computer geeks right there testing it immediately and giving us feedback, and we could see what works.

[**15:40**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=940s) So I think some of it we really just lucked into. I think the size of your pack was determined by how many lines the terminal could display, but that just turned out to be good game balance. But I think, in addition to those things that we lucked into, we also did have a lot of good immediate feedback from people playing the game. But yeah, we didn't figure it out mathematically. We didn't sit down and say, "Okay, here's how often food is going to come about," and this — we didn't analyze that. We just balanced it by trying one thing, and then we found everybody was starving to death by the time they got to level 11, and then we nudged the numbers a bit until that stopped happening.

## Would you have made a different game?

[**16:38**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=998s) You said that the design was very much constrained by the memory constraints and so on. If you'd had more powerful technology at the time, do you think you'd have made a different game?

[**16:54**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1014s) You know, that's a really tough question. I think it was also a time when two people could make a game, right? Or even one person could be the designer and the graphic designer and the programmer, kind of do all of the pieces. If we'd had a lot more powerful technology, I think it would be harder to put together a game that's this simple. I think it can still be done; people are still coming out with nice simple games that are also compelling. But it's hard to say. The temptation to concentrate more on the graphics would have been pretty great, and I think one of the things that made the game a good game was that our focus could be on other things, with the gameplay, because graphics just weren't an option. Sound just wasn't an option.

## Graphics

[**17:59**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1079s) At the same time, I think it's really cool how you said that. Well, there's a lot of people out there that are kind of ASCII elitists, that say all roguelikes should be ASCII and stuff like that, and I just think it's kind of cool that the reason you made the game look the way it did, and the reason it was unique, is because so many role-playing games back then were all just text-based adventures, where you didn't have any graphics. I don't know, I think that's kind of funny, how people say, "Oh, you shouldn't really have graphical roguelikes," but that was kind of what you were trying to make: an RPG that was more accessible, and that you could visualize a bit more.

[**18:29**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1109s) So I think that's kind of funny.

[**18:37**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1117s) Yeah, we wished we had graphics, that's for sure. We were very excited when we got the Macintosh and went, "We can make pictures!" So I think it's great. That was also one of the things that I did very consciously with the Atari ST version: even though we put graphics in there, I allowed for ASCII mode. I can't remember if we ended up putting that in the Amiga version or not; it wasn't in the Mac version, and it wasn't originally in the plan. The Atari ST, in the lowest graphic resolution, you couldn't really get very good pictures anyway, and so in order to be able to see the whole map we still had to do it with ASCII. But I think it was also nice for people who prefer playing it that way to have that be an option, and I think it should always be an option for any roguelike to have it in ASCII.

[**19:40**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1180s) Yeah, that makes sense.

## Other roguelike games

[**19:48**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1188s) I wonder if you've played, Glenn, many other roguelike games?

— I haven't. I feel bad about that, because again, I feel like there's all these people who have built on our legacy. The thing is, I can't even beat Rogue. And I know how it works; I know it from the inside out. I still can't win. So I'm just not that great a game player,

[**20:12**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1212s) So I kind of get overwhelmed. I've seen NetHack, and other than that I haven't even really seen a whole lot of what's out there, aside from some of the Seven Day Roguelikes, which I've played, especially the year that I did one.

[**20:27**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1227s) So I have been remiss in seeing what else is out there.

## Other ambitions

[**20:37**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1237s) Do you have any other ambitions for making games again? Is that something that you want to continue to do?

[**20:46**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1246s) Yeah. Well, I'm working at Zynga now. That's right, I'm back at a game company after many years away from games. I only got into computers because I was into games. I wanted to be a board game designer when I was a kid, and then when I discovered that computers could do all the boring parts for you, then I wanted to do computer games, and so then I had to learn to program, and then I had a marketable skill. So somewhere along the line I ended up kind of drifting out of the games business, just because other opportunities came up, but I'm very happy to be back in it now. Even though right now I'm not working on games at Zynga — I'm working on the game portal, Zynga.com — it's very fun to be building a game platform. But I would love to do a social roguelike. I'd love to see Zynga do that at some point. I think that there's still a lot that can be done with the genre.

## Social crafting

[**22:03**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1323s) That idea just blew my mind, the idea of a social roguelike, especially designed by Glenn Wichman, having that behind it. What would it even be like? I find it very hard to imagine what a social roguelike would contain.

[**22:19**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1339s) Well, yeah, I don't know how much I should talk about it on the radio, since I might yet do it, if I can find a way to get it in the pipeline at Zynga. But I think that there's a lot of things in the social crafting mechanic, where you wouldn't actually get potions. You wouldn't find potions; you'd just find ingredients, and you'd have to make your own potions from the ingredients, and you'd have to trade ingredients, and some people —

[**22:52**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1372s) So you'd have to have some place where you could interact with other people playing. So that's the sort of big basic idea behind it, without giving away the store. Again, I don't know that I'll ever have a chance to create it, but I would like to.

[**23:16**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1396s) If you did, I would throw all of my money at you.

— Okay.

## Risk-taking

[**23:26**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1406s) Yeah, you know, I've been through many startups of various sorts over the course of my career here, and I'm kind of at a place in my life now where I'm happily working at a company that actually is making a profit and is a going concern.

[**23:49**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1429s) So I did a lot of risk-taking things, which were fun, and some panned out okay and some crashed and burned, but none of them made me wealthy beyond my wildest dreams. If they had, then that's probably what I would be doing: some kind of roguelike social game in my spare time, which would be all the time I had. But I have to work for a living still, and so this is a great job that I've got. I'm really enjoying it, but I'm not free to just do whatever I want.

[**24:22**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1462s) Yeah. When you got there, was that something known? Was that a factor in you getting that job, that they know that you made Rogue? Or they didn't know what Rogue was?

[**24:38**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1478s) Well, it's an interesting thing, because there are people who know, and people who have never heard of it. Some of it's generational, but some of it's not. People who are over 40, for the most part, have heard of it. [It] wasn't a factor in me being hired. It was on my resume, but I think most of the people that I interviewed with weren't familiar with it. But one guy was, and so he was very pleased. He felt like it was a coup to get me, and went around telling other people, "We got the guy who wrote Rogue!" And then people would look at him [and] go, "What?"

— What's wrong? That's awesome.

## PC Rogue

[**25:24**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1524s) So I think, among us, probably John is the most experienced Rogue player. I know you've won it many times, right?

— That's Rogue Clone, which is a rewrite of the PC version, or sort of a port of it from the Unix version. I won about four times. PC Rogue, the [Epyx] version, I have never won, and not for a lack of trying.

[**25:54**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1554s) I won it once by restoring dead characters, and even then there were some levels where I'd have to reload and try, "Okay, maybe I can get a little more food value if I go this way." I mean, "Okay, that wasn't going to the exit, and I starved to death, so let's see…" [unclear] PC Rogue really is extremely difficult. I'm kind of surprised anyone has beaten [it].

[**26:27**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1587s) What do you attribute your ability to win the game [to]? Because I've never won it.

— Oh, just sort of persistence, and figuring out a couple of little strategies, like figuring out what scrolls of scare monster are before you pick them up.

[**26:44**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1604s) So that's the only scroll you can identify without touching it. If you can do that, then you can get extra use out of it by stepping on to it before you [pick it up] the first time, and effectively use it twice. And just tricks like that.

[**26:59**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1619s) Yeah. So my theory as to why I've never beaten it, or how I would have to be different to beat it, is that I think someone who can win the game needs to be someone who never makes a move without thinking about it first. And I always get into a mode where I just hit a key, right? I'm battling a monster, and I hit a key twice without looking at the results of the first hit and deciding whether to make another one. You just go bang, and then —

[**27:31**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1651s) Oh, you're dead.

— That's how everyone dies in every roguelike.

— Yeah. So I think I just don't have the discipline to get to the point where I could stop and analyze, and I think, for someone who either that came naturally to them, or they had the discipline to do it, that's what it would take to beat the game.

[**27:54**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1674s) In the version I played — I'm not sure if this is true of all versions — there were rings that reduced your hunger counter, and if you had two of them they would stack and reduce it to zero, so the food clock wasn't a factor.

[**28:08**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1688s) And that would be the ring of slow digestion?

— Yes, slow digestion. And combining two of those with standing on a scroll of scare monster, it was possible to just wait around, generate monsters forever, and level up arbitrarily high. So in theory, if you got that combination, you could win the game quite easily. The one time I did get this combination, I died carelessly to a dragon.

[**28:36**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1716s) Yeah, I think with every roguelike, to some extent, because they're all heavily random and stuff, it's going to come down to playing enough times to not only be good, but also to get a good setup. And so, I don't know, for me, I haven't beaten my roguelike that I made, and it's because I just don't have the time. I'm constantly working on making games and all that kind of stuff. And so a lot of players who have beaten roguelikes are just playing and playing and playing and getting better, but also just waiting for that one really good run, where you got that really good weapon and didn't run into some horrible trap or monster that's very difficult to deal with, all that sort of stuff.

[**29:25**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1765s) Yeah, go ahead.

— Oh, well, I was just remembering, back in Santa Cruz, somebody wrote a program that would just launch Rogue over and over and look at the initial stats, and then quit, until there was one with good initial stats.

[**29:42**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1782s) So they would run that first, and so they didn't have to waste a lot of time.

## Gambling addiction

[**29:58**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1798s) I think, speaking of wasting time, one of the things — whenever I started playing roguelikes, I was like, "Why am I so addicted to this? I don't understand why this is so fun." And I realized it's kind of like a gambling addiction a little bit, except you're gambling your time. When you die in a roguelike, you're losing real time, real time that you spent playing the game. It's not like when you're playing some RPG where you can save your progress, and you die, you just go back a little bit. It's like, you're done, that's it. And I don't know, I feel like that risk-reward factor is just so smart. I don't know [why] too many developers don't take advantage of that, and I feel like they really should.

[**30:32**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1832s) But yeah, I can't remember why we decided on permadeath, if that was something we sat and thought about [and] decided was a good idea, or if it was just kind of arbitrary, because it's manly.

[**30:49**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1849s) Well, no, it's because — think about all the games of that time period; there was the idea that — honestly, I think permadeath is the only thing that makes sense.

[**30:57**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1857s) And, like, because if you're able to make decisions in games and then just, "Oh, that didn't work out how I wanted, so I'm just going to undo it," it takes out all the tension of the game. And if you look at all our arcade games and such, Pac-Man has, quote-unquote, permadeath. So I just think it's a natural — it makes perfect [sense]. Like you said, you didn't really think about it so much, and you didn't have a big debate, and it's because it's just kind of the obvious choice. And I think that games that don't do that are the ones that are actually the weird ones, even though they're more numerous these days.

[**31:36**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1896s) Yeah. Well, for a long time we hadn't put in saving games at all. That was a feature that came in relatively late in the development of the game. So when you can't save a game, then permadeath is de facto.

[**31:52**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1912s) So I think by the time we put saving games in, we were used to it just being that way, that when you were dead you were dead, so we kept it.

— Yeah, roguelikes wouldn't make much sense if you could save games, I think.

— Yeah.

## Inspiration for Rogue

[**32:08**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1928s) Where did the randomization come from?

[**32:15**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1935s) Well, that came from us. Before we wrote Rogue, we had each worked on games written in BASIC and Pascal that were emulating Adventure, so they were text adventures of various sorts.

[**32:31**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1951s) So we had created these games for our friends to play, but we couldn't play our own games. It wasn't fun, right, because we knew what to do in every room. And so we would look over our friends' shoulders and see if they would get what we wanted them to do in that room. So it really came down to: we wanted to create a game that we could play and enjoy as well as anybody else would enjoy it. And so we came up with a game that I can't even beat. Michael's beaten it several times. But anyway, that was the motivation.

## Dungeons & Dragons

[**33:18**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=1998s) You were talking a bit before about the game's connections with Dungeons & Dragons, [how it] was inspired by it. Could you tell us more about how it was inspired, what parts of it, which era of D&D we're talking about here?

[**33:33**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2013s) Yeah. So this was — I guess Advanced Dungeons & Dragons had just come out. When I started playing D&D, [it] would have been like 1975, and it was still the sort of thing where — I was living in Southern California at the time, and there were like three stores in the entire LA area where you could get D&D equipment, and so people would drive for miles. And they were still stapled booklets, in plastic bags. So around the time Rogue came out was the first time that there was this actual Advanced Dungeons & Dragons hardbound book with color illustrations, and it had really hit the mainstream, relatively. So initially, really, that's what we were looking at: making a Dungeons & Dragons game. We took the monsters directly out of the book, took the stats directly out of the book, and just had the computer do the same things that you would do by going through the rule book. And once we got the idea that this could actually be taken commercial, then we changed a lot of that, just so that we weren't using their intellectual property.

[**35:01**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2101s) But even before then, I think, after Rogue started to take on a life of its own, then, instead of the stats being driven by what was in the D&D books, we modified them to fit the balance of the game that we had created.

## Random dungeon generation

[**35:27**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2127s) The Dungeons & Dragons DM guide, the first edition, which I have right here — actually, it's Appendix A, I think, in the back — actually has rules for random number, or random dungeon generation. I don't know if that was an inspiration anyway.

[**35:43**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2143s) Not that I recall. It may have been, at least conceptually, an inspiration, but I don't remember, in any of the games of D&D that I played, ever using the random dungeon generation rules.

[**35:59**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2159s) So I imagine I was familiar with them; I don't really remember. But we were much more driven by the ASCII screen that we had. We had 80 characters by 24 to work with, and so our random dungeon generation was really based on how we could get a good dungeon level into that many characters.

## Character generation

[**36:30**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2190s) One thing I wanted to ask: when you mentioned D&D — I also played a lot of D&D. I think I started playing it when I was like 12 years old, and I remember the thing I spent most of the time on, at least at the beginning, was creating characters. For me, half the fun of D&D was just creating characters.

[**36:47**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2207s) So it's kind of interesting to see that this is the part that didn't make it into the game, and obviously a lot of later roguelikes added it. As a game designer, I don't think it's a good feature to have in many of these games, but I find it funny that it wasn't something that you were thinking of adding, or at least that you didn't add.

[**37:12**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2232s) Yeah, you know, I'm glad we didn't add it, because I think that it's an unnecessary complexity, and it makes it hard when you go from one game to the next. If you've got a different character with different abilities, then you can't compare your previous game to your current one and see if you're improving, and that kind of thing.

[**37:36**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2256s) So I agree. I think that generating characters is actually one of the most fun things about role-playing games, and a lot of times more fun than actually playing with the character. But again, I haven't done a lot of playing of some of the games that have lots of character classes, but I think that there is an elegance in the simplicity of Rogue. And the fact that everybody is playing the same character — everybody's Rodney, everybody's this kind of loser, scruffy rogue — is something that binds the players together, in a way that, if some people are thieves and some are paladins and that kind of thing, I think some of that camaraderie gets lost, in a sense.

## Character creation

[**38:32**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2312s) You're kind of building your character as you play the game, based on mostly what items you find, but [also] your choices in which to wear. I guess one game you are the guy in plate mail, the other game the guy in leather armor. So there kind of is the character creation.

[**38:48**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2328s) Yeah, I think there could possibly be more. I think in Rogue there's almost always an obvious choice. If you've got the choice between plate mail or chain mail, you're going to take the plate mail every time. So that would have been interesting, if there were more variety of objects that would be equally good, or that some people would prefer one over the other. I think we didn't really get there with Rogue. I think there were few enough objects that it was almost always obvious which one you're going to keep and which one you're going to drop.

## Unrandom equipment

[**39:27**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2367s) That's the case for generally unrandom equipment, like armor or weapons, but rings — there's often substantial opportunity costs, having to choose these [over] the set of other ones.

[**39:44**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2384s) That's true. Yeah, that's true. And I remember many times having 26 items in my pack and seeing a 27th that I wanted on the ground, and having to really go through and say, "Okay, what am I going to give up here?"

## The rise of Rogue

[**40:00**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2400s) Ah, I was going to say: I know earlier you said you've had a lot of different experiences, but nothing's made you rich. I just think it's really cool that something you created has had so much influence. You look at games out there today, like Skyrim or something, and as you're playing, if you've played Rogue, you can realize what parts of it were inspired by stuff like that. And the other day I was watching a cartoon, and the episode was called "The Dungeon", and it was totally inspired by Rogue, and I just think that's really awesome.

[**40:33**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2433s) I want to know, when did you start noticing that type of influence taking off, even internationally, in Japan and stuff? When did that kind of realization kick in?

[**40:50**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2450s) Actually, fairly early on. When Rogue became part of the Berkeley Standard Distribution, word started getting back to us pretty quickly. In those days there was the beginnings of the internet, but there weren't a lot of people on it, but it was worldwide, and so there were Rogue discussion groups before even roguelikes.

[**41:21**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2481s) So we had an idea of how much it had caught on. It got back to us pretty quickly that it was being played all over the world, and that people were creating their own takes on it, and that kind of thing.

[**41:37**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2497s) And at the time, I was 20, 21 years old. I figured, "Well, that's it, I'm set for life. I'm going to be rich and famous." So really, if anything, it didn't take me by surprise. I was egotistical enough to kind of take it for granted. And over the years I think I've gained a lot more of an appreciation; it is really nice to feel like something I did has made this big of a contribution to gaming.

[**42:18**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2538s) And also, the whole career that I've had, I owe to it. I was at college, but I didn't take any computer classes. I learned how to program by writing Rogue with Michael, and that was basically my resume for my first job: "Here's this thing that I created. I don't have a degree, I never took any classes, but look, I did this." That's how I got my first job. So really, I owe my whole career to it.

## Glenn and Michael

[**42:59**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2579s) It's awesome. Do you still talk to the other creators? Are you still in touch with them?

[**43:07**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2587s) With Michael I am. He did a poetry reading in Mountain View, California, about a week ago, and I went down and heard him. That's what he's doing a lot of now, is writing poetry, and he's actually also back in the games business, working at OnLive. So Michael and I were friends before we came up with Rogue, and so, yeah, we've kept in touch all these years.

## Starting from scratch

[**43:38**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2618s) Cool. You mentioned before your Seven Day Roguelike game. We just had a couple of episodes about the recent Seven Day Roguelike Challenge, which ended, I think, one month ago, and it ended with a bit more than 60 complete games.

— Wow.

— So, yeah, it's gotten pretty big. I think something like 100 people participated, and 60 of them succeeded in creating games. You want to talk a little bit about your experience during the Seven Day Roguelike, and what it's like?

[**44:08**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2648s) Yeah. I wish I could do it every year, and I'm hoping to do another one. But yeah, as soon as I found out that there was such a thing, I decided I really wanted to do it. So the idea I came up with was a Seven Day Quest.

[**44:32**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2672s) So I kind of took this idea of the Seven Day Roguelike, and I did these seven environments, where you had to get seven amulets and bring all seven of them back to a central environment. I took it seriously, in terms of — it's hard to say what it means to start from scratch, because nobody's starting from scratch; you're not entering ones and zeros into the computer. But I took it fairly seriously: I did all of the graphics, I didn't start with any particular library. It was written in JavaScript, and I started basically with just that, JavaScript and a browser. And I counted it as a success, because I did end up with a playable game.

## The bug

[**45:28**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2728s) But I didn't end up with a winnable game, because there was one bug that I missed that ended up making it so that you can't win. So if you find it out there on the internet, Seven Day Quest, and you play it — I never fixed that bug, because it seemed like it went against the spirit of the whole thing, that I had to be done in 134 hours, or whatever; I think that's right. And so I left the bug in there.

[**46:01**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2761s) So you can't beat it. But my son was just playing it the other day; he ran across it. And so it's still kind of fun to play. So I was pleased with what I was able to do, but I would love to do another one sometime. I don't think that I really can while I'm working at Zynga. I'd have to figure out how to get permission to do that, since anything I create is really Zynga's property, of course.

[**46:42**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2802s) Yeah, I'm not complaining. I think I've got a lot of good opportunities here, and I really like what I'm doing.

## Roguelikes in Japan

[**46:49**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2809s) So how about Japan? Roguelikes kind of developed along this different track [there], and as a result you can find a lot more games in Japan that you could more recognizably call roguelikes. The Mystery Dungeon series that Chunsoft makes is probably the prime example, but there are other companies that have made roguelikes there as well, most of them based more off Mystery Dungeon than the original Rogue. But a few years ago, I think with the PS2, someone actually released a game called Rogue Hearts Dungeon. I don't actually know a lot about [it], but [it's] supposed to stick pretty close to Rogue, to the extent of having large-scale dungeons that look like an extended version of the nine-room dungeon from Rogue — that sort of grid system, extended over a larger area. I think that's what I'm seeing with screenshots.

[**47:55**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2875s) Do you know anything about that?

— No, this is the first that I've heard of it. I do know that we were really big in Japan, and actually the first requests for interviews that we got, and [the first] people writing articles about Rogue, were in [the] Japanese press. And I know that there was an art museum in Tokyo that had an installation on computer games as art, and that Rogue was included in that, which was kind of especially cool, for a game that had no graphics to be in an art museum.

[**48:43**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2923s) Yeah, it is awesome.

— Because I think that there's a beauty to the Rogue screens, a stark simplicity, but they are beautiful. So anyway, I think that there was a big appreciation of Rogue in Japan, but I don't know all of the descendants that have come from it over there.

[**49:14**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2954s) Yeah, my older brother — speaking of that — I texted him earlier, said that we were interviewing you, and he wanted me to thank you, because he's all into the Pokémon Mystery Dungeon games, and they're totally inspired by Rogue, and he wanted to say thank you.

[**49:29**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2969s) Great. Well, you're welcome.

## ToeJam & Earl

[**49:29**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=2969s) The Pokémon Mystery Dungeon games have been released in the United States, along with a couple of the Shiren games as well. Beyond that, [I wonder if] Glenn is familiar with a Sega Genesis game called ToeJam & Earl, which is not, by particularly practical definitions, a roguelike, but takes an awful lot of inspiration from Rogue, and one of the creators, Greg Johnson, said that they played a lot of Rogue before they created it. I don't know if you've ever seen that before, but it's a very entertaining game; it sticks close to the spirit of Rogue in a lot of ways.

[**50:17**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3017s) No. Well, the name sounds familiar, but I haven't played the game, so I think I must have heard of it somewhere along the line. But I think that's one of the things that I love most about Rogue: the tongue-in-cheek pieces of it, and the whimsy of it. I think that was one of the things that Epyx really didn't appreciate; they really wanted to market it and push it as a very serious game, which — they know game marketing better than me, so it was probably the right choice. But in terms of what's near and dear to my heart, I liked the idea of the goofiness, and the idea of the inept hero who's kind of stumbling his way through a dungeon, and not necessarily being very heroic. He's not trying to save a fair maiden or anything like that; he's trying to get himself filthy rich.

[**51:13**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3073s) So I liked that aspect.

[**51:23**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3083s) I agree with you one hundred percent. Just wanted to say that. Anyway, go on.

— I was gonna say, there's some parallels to your own story in there, it seems like.

[**51:32**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3092s) Yeah, it's like if Charlie Brown was wearing armor and wielding a sword.

[**51:40**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3100s) That's Snoopy, breathing fire on him.

— Yeah.

## The name Rogue

[**51:51**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3111s) Lucy turning him, or confusing him with a glance.

— Yeah. I don't know if anybody asked this yet; we're supposed to ask: why did he pick the name Rogue?

[**51:58**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3118s) Yeah, that's a good question, and that's the one piece that I know was completely my contribution, was the name. If anybody ever wants to challenge that, I won't believe them. I came up with the name Rogue. I decided to call it that. But why I decided to call it that, I don't remember coming up with a specific reason; it just sounded right. At first we were just calling it "the game", or "a dungeon game", or whatever, but we needed to come up with a name for what people would type in to get it started.

[**52:42**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3162s) So I guess that was probably part of it: it needed to be one word, and it needed to be a short word, because it was a command on a command-line system, to start the game.

[**52:50**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3170s) So you couldn't call it "Dungeons of Doom", with spaces. But again, it fit with the idea of who our character was: he's a ne'er-do-well. So that was where it came from.

## The nature of Rogue

[**53:11**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3191s) Oh, in D&D terms, of the four traditional character classes, the rogue is sort of in a weird place. The fighter is all about smacking things, the wizard is all about using magic at a distance, the cleric is all about healing, whereas the rogue is kind of the versatile character. He can use some magic items, but he can't use magic himself. He can hit enemies to some degree, but he can't really rely on it. And so the rogue has to go back and forth between using the magic items he's found and fighting, and I think that's sort of the nature of the game.

[**53:59**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3239s) Yeah, that, and the fact that you're on your own. You don't have a party going down into the dungeon together, and again, that was more a technological limitation than a design choice. But the idea of, okay, this person has gone rogue, they're on their own —

[**54:22**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3262s) If only Sarah Palin would go down into it. (Laughter)

[**54:30**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3270s) Do you still play?

— Do I still play? Yes. Yeah, sometimes. There's so many games that I play right now, so many Zynga games that I play, that I don't have a lot of time for other games, but I do still enjoy it, and I play every now and then, and I still can't beat it. I haven't gotten any better.

[**54:54**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3294s) So you've made a game you've been playing for 30 years. Amazing.

[**55:04**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3304s) Yeah. Well, I think, again, there's something to simplicity. Nobody gets surprised that somebody would play chess for 30 years, or checkers, right? But so many games now feel more like a movie that you get to the end of, and then you're done with it. So I think the world can use more games that you can just keep playing over and over.

[**55:34**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3334s) Dang. So that's the real talk right there. I like that.

## Hollywood excess

[**55:34**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3334s) Oh, God, you just reminded me of this thing I saw on YouTube a couple of days ago. Some people got together and made sort of a fan trailer for a Pac-Man movie. (Laughter) It's done with all Hollywood excess, and they came up with some plot about some secret government organization that's creating some polymer thing that can clean up oil spills by eating it. It's just hilarious, but you can also see that if someone decided to make a Pac-Man movie, they would do it exactly like this.

[**56:07**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3367s) That would suck terribly.

[**56:16**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3376s) Well, if somebody decides they want to make a movie out of Rogue that sucks terribly, I'll help.

[**56:27**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3387s) Glenn, you were talking about chess a little bit before. Do you play board games at all?

— Yeah. I haven't as much lately, because I've just moved around a lot. Several years ago, when I kind of had a community of people to play board games with, mostly I would play rail games: the Empire Builder series, where you build railroads across [the map]; 18xx games, like 1830; games like that. I can't remember the name of the company that makes it, but it's a whole series of games: there's Empire Builder, [for] the United States, and then there's Eurorails and Australian Rails, and there's one based in England that I can't remember the name of. Anyway, I would play those rail games a lot, and then Settlers of Catan and those kinds of games.

[**57:22**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3442s) But again, it's been a while since I've played those, because I don't have a community to play that with right now. So now I'm doing mostly social games: Scramble, and Draw Something.

[**57:38**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3458s) So if you have access to an iPhone or iPad, there are a lot of good iOS board game adaptations; you can sometimes play them… [unclear]

## Difficulty

[**57:54**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3474s) Yeah, I should check those out.

— Could I ask a question about Rogue's difficulty? Why you decided to make the game so hard that you couldn't beat it?

[**58:02**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3482s) You know, that's a really good question. I think I didn't have a lot of excuses to make it easier, because other people were beating it. So I don't know. I can't remember us ever saying, "Okay, we want to make something that you can only beat once out of every 100 times that you try." But it seemed to work out well. The thing is that the game is fun even if you lose. There's this idea of being the total winner, which is beating the game, but there's all sorts of ways that you can feel good about your game even if you didn't become a total winner. It's like, "Oh, I got down to a level that I never got to before. I win! I killed a dragon; I've never killed a dragon before. I win!" There's lots of ways to feel victorious in the game without becoming a total winner.

[**59:04**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3544s) Yeah, I actually think that, in a way, some roguelikes don't have endings. If you look at a game like Tetris or something like that, there's no final completion spot; it's a score-based game, and so you win if you get a better score than your friend or whatever. A lot of score-based games don't have [endings]. Or Pac-Man is another example: it does have an end, in that it breaks, as a kill screen, but that wasn't a design intention; it was intended to basically function as an endless game. So I actually think it makes a lot of sense for roguelikes to either be so cripplingly hard that you never get to the last level, or for them to not even have a last level, for that reason.

[**59:52**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3592s) Yeah, I think we couldn't figure out a way to have it just keep getting harder, because you run out of monsters. We could have the monsters keep getting more vorpal, with the same names, as you went further down. But, so, yeah, I think it was a good balance to have there be a way to completely beat the game. But again, it's different from completely beating a canned game, because once you've done that, then there's no reason to ever go back and play it again. But even if you do completely [beat] Rogue, there's still reason to get back in the dungeon.

[**1:00:26**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3626s) Yeah, it makes sense.

— Let me get another question here. One of the, I guess, maybe more controversial roguelike features is the item system, which I think is possibly the most brilliant thing about Rogue — but people here, please disagree with me. That is the idea that you begin the game knowing what none of the items are, and through a process of trial and error, and identify scrolls, you have to discover the game world as you play, and every time you play you have to begin from scratch. And I don't mind the identification systems. We've basically decided earlier [that they] work better in a shorter game; NetHack is probably much too long relative to the number of unidentified items there are in it. But in Rogue, who came up with the idea of the identification system, and how did it evolve in development?

[**1:01:23**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3683s) Oh, I don't remember how we came up with it. I can't remember how much of it might have been inspired by something that's in D&D, so I just don't recall how it came about. I do know that for a long time there was no actual identification system. We had the random scroll names, but there was no way that you could ever get the correct name of it into your inventory.

[**1:01:56**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3716s) So we had people with notepads, where they would be writing down the name of the scroll and what it did, and keeping track of that separately from the game. So we did, after a while, figure out, I think, a fairly elegant way of having it start out being a mystery, but once you did figure out what it did, have it show up with the correct name in your inventory.

[**1:02:21**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3741s) I guess we're done.

— Yeah. Just a note from me: thanks again to Glenn, because it was very entertaining to listen to. It's nice to hear —

[**1:02:29**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3749s) Awesome.

— Nice to hear you're so proud of all the different mechanics that Rogue has inspired, that we all love, and it's great to hear that you love them too, after all these years. So, yeah, it's really good to hear.

[**1:02:45**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3765s) Thanks.

— Decades from now, after you've died, people are still going to be talking about Rogue.

— I love you.

[**1:02:53**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3773s) Yeah, they'll have —

— Hey, who's this? Glenn's going to die?

— Well, it's important, I think, to get a lot of this information down in some tangible form, so that history will be able to remember the game.

[**1:03:08**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3788s) Yeah, I think that would be nice. I don't know how much it all matters, whether my name gets remembered or not; it's not that important. But it is nice. For a long time I felt like I wasn't getting my fair share of the credit, because there was a big chunk of time, before I came back and did the Atari ST version, where people thought of it as Michael and Jon's game, and I felt a little bit forgotten. But at this point I think people are remembering me.

[**1:03:52**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3832s) So it's very nice to be remembered. All right, well, thank you very much for having me on. It was nice to meet all of you, and fun to talk about the old game.

[**1:04:01**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3841s) Yeah, it was awesome. Thank you.

— Thanks a lot.

— Thank you so much for speaking with us.

[**1:04:09**](https://www.youtube.com/watch?v=U-F3_pNq-24&t=3849s) Well, thanks for listening, everyone, and join us next time.
