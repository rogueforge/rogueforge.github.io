---
title: Glenn Wichman talks to Spillhistorie, 2024
summary: Spillhistorie.no's 2024 article on the story of Rogue, built on an interview with Glenn Wichman.
hide_summary: true
---
# Glenn Wichman talks to Spillhistorie, 2024

<div class="paper-source paper-source--conference">
<div class="paper-source__kind">Interview</div>
<div class="paper-source__date"><span>July</span> 2024</div>
<div class="paper-source__venue">The story of Rogue</div>
<div class="paper-source__detail">Spillhistorie.no · Joachim Froholt · written</div>
<div class="paper-source__id"><a href="https://spillhistorie.no/the-story-of-rogue/">spillhistorie.no/the-story-of-rogue</a></div>
</div>

Joachim Froholt of the Norwegian site Spillhistorie.no tells the story of Rogue in July 2024, built
around his conversation with Glenn Wichman: Santa Cruz in 1978, terminals and curses, Dungeons &
Dragons as the main inspiration, Rogue's spread with BSD UNIX, A.I. Design and the commercial
versions (including who drew the Atari ST graphics), why it did not sell, sequels that never
happened, Minecraft as his favourite roguelike, and how to win.

See also [Glenn Wichman talks to Slashie, 2007](wichman-roguetemple-2007.md) and the [2016 panel with Michael Toy and Ken Arnold](rogue-panel-2016.md).

> **About this text.** Spillhistorie.no's interview, by Joachim Froholt, as published on 14 July 2024
> ([original](https://spillhistorie.no/the-story-of-rogue/)). The text is theirs, unchanged; © 2024 Spillhistorie.no. Reproduced here with
> attribution so it is not lost; the article's photographs and illustrations are not copied here.
> Wichman's answers are the paragraphs that begin with a dash.

## The story of Rogue

*We’ve talked with Glenn Wichman, one of Rogue’s original creators, about the game that created an entire genre.*

Rogue is one of the most influential games of all time. Even if you haven’t played it, you’ve definitely played several games that have Rogue’s DNA in them. It became so popular when it was released for UNIX-based systems in 1980 that it created its own genre, which we still know as ‘roguelike games’. Even in the decades when these games were niche experiences, the genre was important. The action role-playing game Diablo built directly on the roguelike genre, which means that all the games that followed in Diablo’s footsteps also have their roots here.

But today, it has exploded in popularity, and you can hardly venture onto Steam without stumbling across at least a handful of games with the genre label ‘roguelike’ or the somewhat more undefined ‘roguelite’. Modern games like Hades, Dwarf Fortress, Minecraft, Rimworld, Dead Cells, Vampire Survivors and Slay the Spire are all greatly inspired by this genre. And like Diablo, many of these games have become sources of inspiration for other developers, who have taken their concepts further to create even new branches in Rogue’s large family tree.

Of course, Rogue is not the only root in this tree; there were other early games that shared many of Rogue’s characteristics, including [Beneath Apple Manor](https://spillhistorie.no/interview-with-don-worth-about-beneath-apple-manor/) on the Apple II and a number of role-playing games on the PLATO computer system. But it is fair to call it the most important and influental foundation of the genre.

## RPG Lite

Rogue itself is a simplified role-playing game, where you play an adventurer who must get to the bottom of an intricate cave system in search of a magical amulet, and bring it back up without dying on the way. The game is turn-based, and the original version uses ASCII characters to depict the surroundings as well as the monsters, items and treasures found there. In the early years of the roguelike genre, both of these elements were characteristic of roguelike games, but later other aspects have become more important.

These include procedurally generated challenges and/or environments, a rich and dynamic selection of tools for the player to use, and perhaps the most controversial: some form of permanent consequences of your actions, combined with limitations on reloading previous games. In short, you have to live (or die) with your choices.

## Back to the seventies

We’ve been fortunate enough to be able to chat with Glenn Wichman, who created the original concept or Rogue together with Michael Toy while they were both freshmen at the University of Santa Cruz in California. The story of Rogue starts in 1978, as Wichman explains:

– We were both freshmen at UC Santa Cruz in 1978, that’s where we met. I wanted to be a game designer, by which I meant board games and card games. When I got to college, I learned about using the computer and discovered the game Adventure (also known as Colossal Cave), and I decided I wanted to make games like that, so I taught myself BASIC and began to work on a text-based adventure game. One day while struggling with getting it to work, a tall stranger came up and asked me what I was working on, and that turned out to be Michael Toy. He knew much more about computers and programming than I did, and had also made several games, so he helped me debug my game.

He continues:

– From then on he played my games and I played his. I would make text adventure games for Michael to play, and he would make text adventure games for me to play. But of course it’s never any fun to play your own text adventure game because you already know the answers to all of the puzzles since you were the one creating them.

It’s important to remember that the computers Wichman and Toy were working on were quite different from today’s computers, or even classic home computers like the Commodore 64. The university had one DEC VAX minicomputer, which all the users were connected to at the same time:

– One thing that was interesting is that I never even saw the computer that I was using; it was underground somewhere a kilometer away. We all worked on terminals, which just consisted of a screen and a keyboard, and we all shared time on a single mini computer that served the entire university, Wichman tells us.

## Text based systems

Traditionally, people connected to such machines using printer terminals. They would type their commands on the keyboard, and the responses from the computer were then printed out on long paper rolls, line by line. By 1978, the terminals had been upgraded to use screens, but the underlying system was still largely the same. Wichman explains:

– Even though the terminals had a screen like a TV screen, they were based on the earlier technology of paper printers, so you did not treat the screen as an integrated output device, you treated it as if it were a printer, you would just send text to the output and it would appear at the bottom of the screen and everything else would scroll up; once it scrolled off the top of the screen it was gone forever. Even editing text files worked this way, where you would enter a command to see a line and then another command to change that line and then another command to save the change.

This solution worked quite well for text adventure games and many other text-based games, as these were often in practice a dialogue between the player and the game. The player typed their commands, the game responded, and this continued until the player was killed by a troll. But the key to Rogue’s success was that it was a *graphical* game. It was limited to text characters, sure, but it used the screen the way a console or computer did. The image was updated each turn – characters moved, more of the labyrinth was revealed, and so on.

What made this possible was essentially a solution to make text editing easier on these systems:

– Most terminals allowed for things like moving the cursor to a specific location by sending non-printing «control characters» to the terminal (usually beginning with the «escape» character). But there were different brands of terminals and each had its own set of rules so someone could write an editor that allowed you to display a file on screen and move the cursor around and change things visually, but that editor would only work on one specific brand of terminal.

So where text editing originally functioned more like working with a classic typewriter, it now became a bit more like what we know today. But these solutions had one big problem: There were a variety of different terminals from a variety of different manufacturers, and the routines that allowed cursor movement were unique to each of them. A program as described would only work on one specific terminal brand. Fortunately, this was also on the way to being solved:

– While Michael and I were creating text adventure games at U.C. Santa Cruz, 120 kilometers away at U.C. Berkeley, Bill Joy had created an editor called «vi» which worked as a visual editor on any terminal, because it included a database of how each terminal did cursor addressing and abstracted the problem of having to have a different program for every different terminal.

This is where Ken Arnold, the third developer of the original Rogue, enters the picture for the first time:

– A student at Berkeley named Ken Arnold took that code from vi, refined and improved it, and created a library of routines that could be used by any C program to treat terminals as an addressable graphical space (the library was called «curses»).

He continues:

– Michael got ahold of this library and we both started using it make simple graphical games, and then Michael asked me if I thought it would be possible to use this to make a graphical Adventure game. I didn’t think it would be possible but as we began to talk about it more we realized that not only could we make an adventure game with this, but we could make one where the computer itself created the environment you were exploring, we could create a game that could surprise even its creators, and that was the beginning of Rogue.

## Inspired by Dungeons & Dragons

Like many students across the USA, both Wichman and Toy had become familiar with the role-playing game Dungeons & Dragons, which, despite much opposition from certain parts of society, took the seventies by storm. Unsurprisingly, Dungeons & Dragons was a very important source of inspiration for Rogue:

– Our main inspiration was absolutely Dungeons and Dragons. Very early (pre-commercial) versions had monster stats copied directly from D&D, though of course as we refined it we came up with more original stuff. Colossal Cave Adventure and other similar text-based RPGs were also an inspiration. But really it was mostly just D&D.

The development of Rogue did not happen in a vacuum. Wichman and Toy had a network of friends who would test their games, and they also got involved with Rogue as the game was developed. Because of this, the duo soon understood that they were working on something quite special:

– We knew that our game was more fun, imaginative, and engaging than anything else running on the college computers. We saw our friends scream and pound the keyboard when killed by a troll, or stand up and dance when they found the amulet. And we had those same reactions ourselves, playing our own game.

Still, they didn’t really have any ideas of exactly how big Rogue would become:

– I think we (Michael and I) knew we had something special from the start. But also we didn’t have an idea of what «big» was at that time. We were creating a game to play with our friends and didn’t really think beyond the 20 or so people we knew who would play it with us. The game we initially wrote on the DEC VAX computer was too large and complicated to run on a home computer, and only a few thousand people owned home computers. When we wrote the game in 1980, we did not know how much the world would change by 1984.

It didn’t take long before early versions of Rogue became well known far beyond the small group of friends Wichman and Toy had involved. In fact, it spread like wildfire, and one of those who got hooked on the game was the original creator of curses, Ken Arnold at Berkeley University. His system actually became so closely associated with Rogue that many thought it had been created for the game in the first place. So it might not come as a huge surprise that when Michael Toy moved to Berkeley, Arnold quickly got involved.

– Michael and I worked on it for months and then Michael moved to U.C. Berkeley and then I was out of the picture for a while, but Ken Arnold joined in and the game was completed by the two of them, Wichman tells us.

## Distributed via UNIX

Once Rogue was completed, it really took off. This wasn’t *just* because of the game itself, though, because Rogue wound up being a sort of UNIX equivalent of the Klondike Solitaire game that would end up on millions of Windows machines many years later:

– Rogue became widely known when it was included as part of the Berkeley UNIX standard distribution… this became a very common operating system for computers on college campuses around the world. The fact that we were included with that is just happenstance. But Rogue had a couple of things going for it, most of the games included with the distribution were mild diversions, and none of them were graphical in nature — they really couldn’t be since graphic terminals were rare and expensive. Rogue was among the very first games to treat a text-based terminal as a graphic canvas by using ASCII «art», which made the game much more visually interesting (even though by the standards of just a few years later, it is very primitive).

But Rogue had more than that one advantage over other UNIX games:

– Rogue was also a very well balanced game. It was notoriously hard to beat, but you did not have to beat it to enjoy it. It was easy to learn and understand. The world was rich enough to surprise you, but it was not overwhelming… a single explorer, no classes or races or other complexities to set up your character, you could just start playing. 26 monster types total, large enough to keep the game fresh and interesting but small enough that you could keep it all in your head without having to refer to a monster manual.

Rogue became more than just a popular game, though. As we’ve mentioned earlier, it also became an important source of inspiration for other early game developers. This probably wasn’t by accident, according to Wichman:

– The initial audience for that game were, mostly, people studying computer science. Game design as an academic discipline didn’t exist yet, but for coders who wanted to make games, this was often the first game they encountered in an environment where they could take that inspiration and then make their own game.

## Commercial versions

As the eighties progressed, games from other developers took over. Games like Hack from 1982 and Moria from 1983 expanded on the concept in different ways, and had the advantage of being open source software so others could build on their foundations. But the story of Rogue doesn’t end here. As Wichman mentioned, development progressed enormously in the late seventies and early eighties, and it didn’t take long before home computers became powerful enough to run Rogue. Like many other games with mainframe roots, Rogue would jump to the commercial market.

This happened through a developer named A.I. Design. After his time at Berkeley, Michael Toy ended up at Olivetti, who were working on a machine based on IBM’s new PC standard. There he met Jon Lane, who was both a fan of the game and convinced that it could be a success in the home market. They started A.I. Design, and Lane began working on a PC version. This was discovered by the major publisher Epyx, one of the most respected names in the games industry back in the eighties, and they became involved as a publisher.

The first home version retained the original game’s ASCII-based ‘graphics.’ But later versions took advantage of the fact that home computers had far more advanced graphical capabilities than the original hardware, and this is where Wichman became involved again. He was a capable pixel artist and agreed to create graphics for a version for the Apple Macintosh. He then took primary responsibility for a version for the Atari ST, while Toy had primary responsibility for an Amiga version.

## Differences between the versions

What is somewhat interesting here are the differences between the versions. Wichman’s Atari ST version has much more detailed graphics — created by Epyx’s Michael Kosaka—and environments that scroll as you move around in them. The Amiga version, on the other hand, uses the same size for the individual characters as the original and has the entire levels on the screen at the same time.

– We both started with the «C» code that Jon Lane and Michael had written for the IBM PC and MacIntosh versions. And, we were sitting just about 2 meters apart, Michael with his Amiga and me with my ST, as we created them. Part of the reason for them being different is just that the Amiga and ST were different machines with different strengths and we were each making a game optimized for the computer we were using. It was a very different approach from the way you would approach things today, where you would certainly abstract out the platform and try to make a game that looked and felt as close to identical as possible.

But there was also something else:

– Part of it was also a friendly competition. In particular, I felt that I had something to prove. Even though I was heavily involved in the game design for our first (UNIX) version, Michael (and later Ken Arnold) wrote all the code. And being a «game designer» wasn’t really recognized. Later, when the IBM PC version was written, I was not involved at all. For the Macintosh version, I contributed as an artist but not as a coder. So, when I got the opportunity to create «my own» Rogue for the Atari ST, I worked very hard to put my own stamp on it.,

The game was also released on various 8-bit micro computers, such as the Commodore 64, but Wichman doesn’t remember a lot about these versions. He does mention one neat little detail, though:

– My memories about 8-bit versions are pretty vague. We had started to work on a version for the Radio Shack CoCo, but C compiler technology at the time was not really ready to create efficient code for 6502 or similar 8-bit processors. Ultimately that project was handed off to assembly experts who «hand-compiled» the C-code. It’s an odd thing in retrospect, that in those days humans did a better job of compiling than computers did. It is of course quite the opposite now.

## Not a commercial success

Wichman never tried any of the 8-bit versions of Rogue. The version for Commodore 64 and a number of other platforms more popular in Europe were also done by UK publisher Mastertronic under licence from Epyx, and the original creators were not involved in their creation. Regardless, the game was never a major hit on the home platforms:

– Rogue was not, by any means, a commercial success. I don’t have any of the sales figures, I don’t think there was a significant difference based on platform, relative to the installed base of that platform. I was paid $15,000 for the Atari ST work; that is the only money I have ever made from Rogue. I think it was over all a loss for Epyx.

Wichman has a theory on why:

– Even though Rogue was way ahead of its time in 1980, by the time we did the commercial version in 1984, the expectations of what a computer game should do had changed drastically, and we really never sat down and said, «What does Rogue need to be in order compete in today’s marketplace»? We just knew there was a lot of demand for people who had played Rogue on their college computers, and wanted to keep playing now that they were out of college and had a home computer. But that wasn’t enough of an audience to make the game profitable.

He also wasn’t a fan of the marketing, which he didn’t feel matched his own vision for the game:

– Cover images are designed by marketers to get people to buy games. I didn’t like any of the marketing materials that the later commercial games used.

If I had my way, Rogue’s look and feel would be much more like Spelunky. To me it was always a light-hearted and funny game.

Despite Rogue never becoming a commercial success, Wichman often toyed with the idea of a sequel. But he also had other game ideas, and a potential Rogue 2 would be a challenging prospect:

– I thought often about sequels and had several ideas in mind. But I also had lots of other game ideas as well. The ambitions I had for a follow-up to Rogue were much larger than I could accomplish on my own, but the rest of the «team» were not interested in making more games, none of the other 3 developers ever worked on another game. I did my best to stay in the game industry, but that involved working on the games I was hired to make. I wrote a couple of simple shareware games in my spare time, but I found that I was just as happy and fulfilled to work on whatever game I was hired to work on.

## Wichman loves the community

At the same time, he admits that he didn’t really keep up with what happened to Rogue over the years, nor did he follow the Roguelike genre. He tells Spillhistorie.no that he was vaguely aware of something called Hack and Nethack, but never played those games. It wasn’t actually until about fifteen years ago that he rediscovered the genre and became involved in the community around Roguelike game development. However, he greatly appreciates the community:

– I really loved the community and the people who were dedicated to the genre and I have been very impressed with all of the amazing games that they have built.

When asked if he’s got any favourites in the genre, his answer might come as a surprise to some:

– Even though nobody really counts it as a «Roguelike», my favorite Roguelike is Minecraft. I think if I had just kept working on Rogue constantly over the years, what I would have ended up with would look very much like Minecraft. Maybe Minecraft, Diablo, and No Man’s Sky are all remakes of Rogue, if you want to look at it that way.

On the other hand, he does believe a more faithful remake of Rogue would work well on modern platforms:

– I think you could make a successful game that kept to Rogue’s level of simplicity/complexity — 26 levels, 26 monsters, one Rogue named Rodney, one Wizard named Yendor, one amulet to search for… I think that would be a good game. I would play that game.

However, such a game is unlikely to come from the original creators. Wichman points out that he is not a lawyer, but describes the issue of the game’s rights as murky, and says that none of the three original developers of Rogue have received any revenue from the various versions of the game that have appeared for sale on new platforms. This includes the Steam version of Rogue, which was released by Pixel Games UK (current proprietors of the Epyx licenses) a couple of years ago.

– That doesn’t bother me though. I’m just happy to see people still like to play the game almost 45 years after we created it, Wichman says.

## «Roguelike»

But what about the aforementioned roguelike term? We’re not quite sure when it first started being used, but it became «official» around 1993, via Usenet newsgroups. This was an arena for discussion, and there was a significant overlap between people who liked these games and people with access to Usenet in the first place. Because of the way Usenet is structured, a category name for the genre was needed. After a significant amount of discussion, the term roguelike was chosen.

This meant that anyone wishing to discuss Nethack, for instance, would go to rec.games.roguelike.nethack (which means that Nethack is filed under recreation, more specifically a game, that is in the roguelike genre). Since the genre wasn’t really mainstream at this point, and not widely discussed in magazines or advertisements, Usenet would be the main place to learn about these games and the name stuck. So it’s somewhat of a coincidence, but Wichman is still happy that the term became popular:

– I just feel incredibly lucky that it happened to catch on. I mean, I think it is fair, I think we really did pioneer an entire new genre of game (though someone else would have done it if we hadn’t). But most genres don’t get named after the first major example of the genre, and if the name had not been «Roguelike», I don’t know if Rogue would be remembered nearly as well as it has been.

If you’re interested in trying Rogue for yourself, Wichman has a few tips. He points out that he never managed to complete the game himself, despite having unique insight into the mechanics of the game. But there is one thing in particular that those who’ve achieved that particular feat has in common:

– The people who do beat rogue never ever hit a key twice in a row without waiting to see the consequences of the previous move, reevaluate, and calculate. You need a good strategy of course but you need to treat it as a turn-based puzzle game to survive. I always got lost in the feeling of being in that world and I never had the patience to stop and think after every move.

And finally a word of wisdom:

– Hitting the keys harder will not do more damage.

*We’d like to thank Glenn Wichmann for taking the time to answer our questions.*

*Author: Joachim Froholt*
