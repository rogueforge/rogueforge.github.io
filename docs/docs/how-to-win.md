---
title: How to Win at Rogue
summary: Bart Wright's treatise on winning at Rogue, from a player who had won some thirty games.
---
# How to Win at Rogue

By Bart Wright  
Revised and expanded by the Archmage Yendor

This edition corrects the text against the games' source code and adds notes for other versions of Rogue, from 3.4 to 5.4 and PC Rogue 1.48.

I learned what follows on Rogue 5.2, as it ran on Unix systems around 1986. Where other versions differ, a note in parentheses says so, and the PC version has a section of its own at the end.

I assume you know the fundamentals of the game and have played several times.

## The Big Picture

My goal when I play rogue is to have the greatest number of wins per hour I spend playing the game (though I am not averse to breaking any of the rules in here to have fun).  Although I have won some 30 times (in 5.2), I average about one win per 10 hours of play -- I still need good luck.  As an example of a decision influenced by my goal, if I find a ring on the first level of the dungeon, I try it on immediately.  If it is cursed, I quit the game and start another one.  You wouldn't do this if your goal is to maximize your chances of winning any one game.  Carried to its extreme, this would also suggest that you not bother to pick up gold if it takes you out of your way, and not waste arrows on leprechauns, but I haven't gone this far myself.

Here is the basic situation.  To win rogue, you have to go down 26 levels, find the Amulet of Yendor, and then come back up.  "Stuff" (magic, armor, weapons, food) occurs with equal frequency on all levels when going down. When you start back up, there is no stuff at all (except what some monster may be carrying).  Monsters also occur on every level, but the species you encounter get decidedly more threatening as you descend; as you come back up they get less threatening.

You need to collect all the stuff you can, discarding what is not useful and keeping what is.  Some of the good stuff helps you permanently, such as enchantment of your weapon.  Most of it disappears immediately when you use it (arrows, most scrolls and potions), some disappears after a number of uses (charges of staves), and while the rings last forever, most use up your food at a faster rate when you have them on, so their use is limited by food supplies.  Food is also needed just to stay alive (I have died of starvation many times).  Call all of this good stuff that gets used up consumables.

The basic pattern of a good game of rogue is to scan every level thoroughly for stuff, building up your consumables (and of course your permanent good stuff as well), until you reach a level where (on average) the consumables you consume fighting a level's monsters that you find after you find the stairway exceed the value of the stuff you will find after finding the stairway.  I think this is usually level 17 or 18.  You then shift to a mode where you go down as fast as possible (including use of trap doors when you find them), hoping that your consumables last long enough to get you back up to where you can defeat monsters without consumables.  You may be comforted to know that if you can get back up to level 15, you are almost assured of victory.  You don't even need food at that point; possessing the Amulet of Yendor stops your food consumption altogether (though rings you are wearing still use food). (5.4: the Amulet doubles your food consumption instead. PC: it has no effect on food.)

## Basics of Combat

Magic is nice when you run into trouble, but you have to be able to dispatch most of the monsters by simple combat, because you don't get enough magic for more than a small fraction of them.  I have won several times where I couldn't reliably defeat a xorn or umber hulk, but I never won unless I could defeat a troll or invisible stalker.

Your blows against a monster are affected by your dexterity (the chance you have of hitting as opposed to missing), and your damage (how many hit points you take away with a hit).  They are also affected by the monster's "armor" level (which affects your likelihood of landing a blow), and the total number of hit points the monster started with.

The monster's blows against you are almost completely parallel. (One exception, a bug: an attacker gets +4 to hit a target that is asleep or held, and the game treats you that way from the start until the first time you are frozen, put to sleep or faint and then recover, so until then every monster hits you on 4 more rolls out of 20. 3.4 and 3.6: there is no such bonus. PC: it never goes away.)  The monster has a dexterity value and a damage value, which are pitted against your armor level and your hit points.

So dexterity, damage, armor, and hit points are the fundamental units of combat.  They are often determined by secondary factors:

Your dexterity level goes up as your experience level increases, and it goes up a little for strength values over 16.  It is also affected by rings of dexterity and the first number on your weapon.  "A +1,+2 mace" is one with one extra dexterity level and two extra damage points.

The damage you do is affected by the identity of your weapon (as well as the second number).  Your original +1,+1 mace takes from 3 to 9 hit points, for an average of 6 (one more than that, thanks to your starting strength of 16).  You may find spears, daggers, long swords, etc. in the dungeons, but the only ones that are worth wielding (as opposed to throwing) are the long sword, which edges out your mace at 3 to 12 hit points (average 7.5), and above all the two-handed sword. (3.4 and 3.6: the long sword does only 1 to 10, so there the two-handed sword really is the only one.)  This takes from 4 to 16 hit points, for an average of 10. (3.4 and 3.6: 3 to 18, average 10.5.)  Your damage is also increased significantly as your strength goes above 15: +1 at 16 and 17, +2 at 18, +3 at 19 and 20, +4 at 21, and +5 from 22 up.

Your armor class is simply what is shown on the screen, though a ring of protection has an additional, invisible effect.  A +2 ring of protection is 2 good units of armored-ness, meaning an armor class 2 units lower than the screen shows, and it also helps your saving throws against magic.

Your maximum hit points show on the screen.  They go up each time you gain a level of experience, by a random number from 1 to 10.  They go up a little when you quaff potions of healing and extra healing, assuming you were reasonably well-healed to begin with.

A very important factor is your rate of healing, which also goes up as you gain experience levels.  When you reach level 8, you recover one hit point for each three turns you do not fight, and above level 8 you recover a random number between one and (level minus 7) every three turns.  At experience level 13, this is from 1 to 6 hit points, which can be very significant in the art of running away.

The monster's dexterity level is a constant determined by the species (down to level 26; below that, each extra level adds one to every monster's level and improves its armor class by one).  The number of hit points per blow is random (for each blow) within a range that is constant for the species.  The monster's armor class is also constant for the species.  The monster's dexterity level determines the number of hit points the monster has.  Each dexterity level corresponds to an average of 4.5 hit points (random from 1 to 8).

It also seems to me (though it could be a superstition) that a better armor class for you also reduces the number of hit points a blow takes away from you, though I don't think the monsters are helped in the same way.  This does happen, because many monsters have several separate attacks (a troll has three), each of which must hit on its own, while the message that the monster hits you appears if any of them land a blow; better armor means more of those messages are a single blow.

High experience levels (say above 10) don't increase the damage you do with each blow, though it can feel that way: each level adds one to your roll to hit, so more of your blows land.

## Know Your Monsters

Here is the monster table, as it stands in Rogue 5.2.

| Monster | Levels | Carry | Mean | Skill | Damage | Armor | AvgHP | Points |
|---|---|---|---|---|---|---|---|---|
| K | 1-6 | -- | yes | 1 | 1-4 | 7 | 4.5 | 1 |
| J | 1-7 | -- | yes | 1 | 1-2 | 7 | 4.5 | 2 |
| B | 1-8 | -- | -- | 1 | 1-2 | 3 | 4.5 | 1 |
| S | 1-9 | -- | yes | 1 | 1-3 | 5 | 4.5 | 2 |
| H | 1-10 | -- | yes | 1 | 1-8 | 5 | 4.5 | 3 |
| E | 2-11 | -- | -- | 1 | -- | 9 | 4.5 | 5 |
| A | 3-12 | -- | yes | 2 | 1-6 | 3 | 9 | 9 |
| O | 4-13 | 15 | yes* | 1 | 1-8 | 6 | 4.5 | 5 |
| Z | 5-14 | -- | yes | 2 | 1-8 | 8 | 9 | 6 |
| G | 6-15 | 10 | -- | 1 | 1-6 | 5 | 4.5 | 7 |
| L | 7-16 | gold | -- | 3 | 1 | 8 | 13.5 | 10 |
| C | 8-17 | 15 | -- | 4 | 2-12 | 4 | 18 | 15 |
| R | 9-18 | -- | yes | 5 | -- | 2 | 22.5 | 20 |
| Q | 10-19 | 30 | yes | 3 | 3-8 | 2 | 13.5 | 32 |
| N | 11-20 | 100 | -- | 3 | -- | 9 | 13.5 | 37 |
| Y | 12-21 | 30 | -- | 4 | 2-12 | 6 | 18 | 50 |
| T | 13-22 | 50 | yes | 6 | 4-28 | 4 | 27 | 120 |
| W | 14-23 | -- | -- | 5 | 1-6 | 4 | 22.5 | 55 |
| F | 15-24 | -- | yes | 8 | inc | 3 | 36 | 80 |
| I | 16-25 | -- | -- | 8 | 4-16 | 3 | 36 | 120 |
| X | 17-26 | -- | yes | 7 | 7-33 | -2 | 31.5 | 190 |
| U | 18- | 40 | yes | 8 | 8-34 | 2 | 36 | 200 |
| M | 19- | 30 | -- | 7 | 3-12 | 7 | 31.5 | 100 |
| V | 20- | 20 | yes | 8 | 1-10 | 1 | 36 | 350 |
| P | 21- | 70 | -- | 15 | 4-32 | 6 | 67.5 | 4,000 |
| D | 22- | 100 | yes | 10 | 5-46 | -1 | 45 | 6,800 |

(3.4 and 3.6: experience values are fixed, and many differ: troll 55, xorn 120, umber hulk 130, mimic 140, vampire 380, purple worm 7,000, dragon 9,000. 5.3, 5.4 and PC: many letters are different monsters, so this table does not carry over.)

Key to the monster table:

Monster:  The letter that identifies the monster on the screen.

Levels:  The levels of the dungeon where the monster appears.  Note that treasure rooms are stocked with monsters from one level deeper, so there each kind shows up (and stops showing up) one level earlier than shown here, and every monster in a treasure room is mean.

Carry:  The chances that the monster is carrying some "stuff" which you can pick up if you defeat it. This only applies to monsters that are there when the level is made; itinerant monsters carry nothing. (5.3 and 5.4: only on a level deeper than any you have visited before.)

Mean: There are two kinds of monsters, those that are put on a level when you enter the level (settled) and those that are created more or less constantly as you spend time on the level (itinerant).  All itinerant monsters start chasing you as soon as they are created (floating eyes, leprechauns, nymphs, violet fungi, mimics and dragons are never itinerant).  Mean refers to whether a settled monster will "wake up" and chase you.  Monsters that are not mean never do, unless aggravated by ring or scroll.  Those that are have a good chance of doing so when certain triggering events occur: you enter the room, leave the room, or end a turn next to the monster.

*Orcs go for gold and sit on it contentedly if there is any in the room; if not they go for you.

Skill:  The monster's level. Each point of skill adds 5% to its chance of hitting you, and it also sets the monster's hit points.

Damage:  The range of possible damage the monster can inflict in a single blow.  This is modeled as a certain number of N-sided dice. If the bottom of the range is 1, it is a single die, if it is 2, then it has 2 dice, etc. But some monsters attack several times in a turn, and each attack has to hit separately; the range shown is what you take if they all land. A Centaur makes two attacks of one 6-sided die each. A dragon lined up with you within six squares can also breathe fire for 6d6 (a saving throw dodges it). Monsters with multiple dice have a greater tendency to inflict damage in the middle of their ranges, compared to single-die monsters.

Armor:  The armor level of the monster, just like your armor class.

Average hit points:  How many points the monster has, on average. This is always 4.5 times the Skill level.  In fact, it is computed as if the monster rolled an eight-sided die for each skill level, so you can compute maximum and minimum from that.  Monsters in treasure rooms roll their hit points the same way as any others. Below level 26, though, every monster gains one skill level (so more hit points), one point of armor and 10 more experience points for each level you are below 26.

Points:  How many experience points you get for slaying the monster, plus a bonus of one point for every 6 hit points it had (every 8 for skill-1 monsters), multiplied by 4 for skill 7-9 and by 20 for skill 10 and up. The bonus averages about 20 for the skill 7-8 monsters, 140 for a dragon and 220 for a purple worm. Yes, purple worms and dragons have values in the thousands.

Scanning a level.

Your goal when you enter a level (on the first 15-17 levels, anyway) is to find all the stuff you can, as quickly as possible, defeat all the monsters you meet, and get on to the next level.  There are two reasons for not dallying.  First, you have a limited supply of food, and even if you're not in danger of starving a surplus is good if you want to use rings later. Second, itinerant monsters are being created, and the longer you hang around, the more of them you have to fight.  (But if I'm about to face trolls on level 13 and am 5 experience points short of getting to the next level, I'll sometimes wait near the stairs for another monster.)

The game provides you a variety of options for moving.  When I want to go more than a single space, I typically use the "f-direction" syntax (f key followed by direction key).  This stops you whenever you find anything. When I talk about "waiting", I usually do that by searching (s).  (You can pass time without searching with the period key.  Occasionally this is desirable, for instance when you are healing after combat and don't WANT to discover any hidden passages just yet.)

There are only nine possible rooms on a level, arranged in a 3 x 3 grid.  The only passageways go from one room to an adjacent room (not on a diagonal).  In some cases a single hallway space is created as a placeholder for a room, and passages can go to that.  All passages consist of (at most) a straight segment toward the other room, a straight segment laterally, and a straight segment toward the other room again.  Occasionally when these overlap you see more interesting patterns, but if you look you can always see how it was made according to these simple rules.

So when you are searching for hidden passages leading to new rooms, you never need to search for passages leading off the screen, for more than one secret door on the side of a room, or for any passage that leads to a place you can already get to by passages you know about.

Generally you do better to seek out the corner rooms first when you have a choice about where to go.  Since the screen is wider than it is high, you generally minimize your walking distance by going up/down first instead of left/right.

You want to look for things in every square of every room (I'm assuming the room is dark), but you don't want to walk on more floor than you have to, to minimize your chances of falling into a trap.  All rooms are 2, 3, 4, or 5 squares high.  When you first enter a room, first move up and down to discover which height room you are dealing with.  In addition, you may or may not care about discovering doors.  For instance, suppose you enter a 5-high room on the top of the screen (from the right).  There are no doors on the top wall, but there may be a door on the bottom wall, so you can scan the room in two passes.  You can first walk along the second row from the top, and then along the bottom row, and you will have scanned the whole room.

When you zip across a room, you scan three rows at a time.  With a little effort, you can actually scan four rows at a time.  Suppose that you enter a 3-high room on the top of the screen, from the right.  Go to the bottom row and repeat this pattern of moves: left, left-up, left-down, (left, left-up, left-down...)  You scan four rows without taking extra steps. Of course this is a bit tedious, so I generally only do it when I am deep in the dungeon (say level 13 or deeper) and invested in my game. When you need to scan a 3-high room in the middle row of the screen (including looking for doors on top and bottom walls), you can get an efficient search pattern by going to the middle row and repeating this pattern of four steps:  up-left, down, down-left, up-left.

If there is any chance you may later have to search for a secret door along a wall, it's best to initially explore by hugging the wall, so you don't later have to walk across more floor.  You COULD follow your same step pattern when you search, but I've never had the patience for that.

When you search, you search all eight of the surrounding squares including diagonals with equal effectiveness.  So if you are looking for a secret door on a wall (but not the adjacent wall), it never pays to search in the corner.  My general pattern is to go one away from the corner, search 7 times, then move left, search twice, move left, search twice, etc. until I reach one from the other end and search 7 times.  Then I repeat the procedure going back to the right.  I know this could be further optimized, but I haven't done so.  When you have a choice of looking for a secret door on a horizontal or vertical edge, it pays to search the vertical edge first, because if the door is there you will find it with less effort.  In fact I often search horizontal edges (7-10 times) when I am near them in case I may need them later.

Often you end up going down a corridor which comes to a dead end. First, if there aren't four rows or columns between you and the edge of the screen, there can't be a room (two rows of room plus two rows of walls), so you don't need to search for it.  Second, if the corridor ends while you are moving laterally (e.g. you move down from a room, to the right, and there is no way down), there is always a room there. What's more, you can back up one square from the end of the corridor to do your searching.  You will find the door just as fast, and if there are monsters waiting to get out, you get an extra turn to look at them before they are upon you.  Critically, you can take off your armor if a rust monster appears.

When you want to be especially cautious, you can throw an arrow (or dart, or whatever) down a corridor before you walk down it.  If there is a monster there, you will be told about it (maybe it's the distinctive grunt of surprise that gives the beast away?).  Then you can react appropriately.

Another thing to be aware of is the "homing patterns" of itinerant monsters.  Once created, they essentially walk towards you in the X,Y plane, pretty much oblivious to whether there are passages leading to you, when they are at a distance.  (I don't know their full algorithm.)  Suppose the passages joining rooms on your level are like a big E.  If you explore the bottom two arms quickly and find the stairway there, but then end up spending a long time in the top arm (fighting tough monsters or whatever), then you can expect to meet several itinerant monsters just as you get partway down the shaft of the letter E, because that's when they will "drain" toward you.  So when you start heading back down the E shaft is a good time to send down an arrow, or even wait a few turns so the monsters come to you before you stumble into one.

## Doorways and Bends in the Road

When you first appear in the doorway to a (dark) room, you should consider searching for several turns before you enter.  I mentioned under monsters that "mean" monsters often wake up when you appear in the doorway.  For one thing, if there is more than one in the room, you will be able to fight just one at a time.  Also, if you are moving and you start a turn 1 space away from a monster who is coming for you, the monster gets a hit on you before you know he is there.

One reason to prefer first entering a room from a door on the top or bottom (rather than the sides) is the much greater chance that a monster will first appear diagonally from you in the doorway instead of straight ahead. With a rust monster, this typically makes the difference between losing an armor level or not.  (This is generally a minor factor; I don't take long detours to enter a room from the top or bottom, but it is another reason to explore up or down corridors before sideways corridors when all else is equal.)

I played rogue for a long time before I learned a lesson from a dragon.  I was in the doorway of a room fighting something like a purple worm, and the dragon was visible diagonally one square away within the room.  Said dragon fired a bolt of fire at me from that position. (In 5.2 it couldn't actually hurt me there: a bolt bounces off a door square even when you are standing on it, so a doorway is proof against bolts, your own rebounds included. 5.3 and 5.4: fixed.)  This led me to the insight that you too can send bolts on diagonals, and more importantly you can send arrows and other projectile weapons.  This can be a real help.  Note that arrows and crossbow bolts are still quite effective when thrown, even without the bow or crossbow to fire them: they do their full 2d3 and 2d5, just without the launcher's bonuses. (3.4, 3.6, 5.3, 5.4 and PC: not so; thrown by hand an arrow does 1d1 and a bolt 1d2.)

Here is a classic case.  You stand in the doorway for a turn when a rust monster appears.  You immediately take off your armor. (That takes just one turn, and the armor is off before the rust monster swings, so you lose a point only if it got a hit in before you noticed it.)  A troll becomes visible diagonally one square away.  You could defeat the rust monster, and then face the troll without any armor on.  But you're better off wielding your bow, ignoring the rust monster, and fire arrows at the troll until you kill it.  Then wield your main weapon again and dispatch the rust monster, then put your armor on.

Many other cases are also worth it.  If you face a jackal straight ahead and a centaur on the diagonal, you might take hits from the jackal while you soften up the centaur with arrows.  If you face a gnome and you view a rust monster on the diagonal, you might want to take off your armor to fight the gnome, figuring you can defeat the gnome comfortably without armor.  Even if you don't want to fire arrows, seeing the next monster you have to face can help you plan your strategy (can I defeat this duo, or will I need magic?)

The same principle applies to bends in corridors.  If a monster lunges out of a room at you as soon as you discover the hidden door, it's often worth backing up a few squares to a bend to see if there is another monster behind.

## The Art of Running Away

It's great when you can dispatch a monster without moving.  But all too often, you find yourself losing the battle.  Even if you could use magic, your supply is limited.  But if you run away, you will gradually heal, while monsters don't (3.4 and 3.6: trolls and vampires do heal a little, with a one-in-three chance of regaining a hit point each time one attacks you; 5.2 still marks them as regenerators, but nothing reads the mark).

There is always the danger that you will run into another monster as you run.  For this reason, it's not a bad idea to start running away while you still have enough hit points to survive one vicious hit from another monster who might surprise you.  I often try to keep 30 hit points (once trolls have appeared).  I fight until my hit points drop to 30, then run away until they have recovered to 50 or so.  Your healing gets much better right around experience level 8.  Once you get to experience level 13 or so, you can even heal enough while running away to defeat purple worms.

When you run away down a dead-end street, you don't have very far to run.  Running away works best when you can go in a circle.  Circles are of various kinds.  A circuit may go through a number of rooms, or sometimes strictly within a set of corridors.  The less obvious case is a non-mean monster stationed in the middle of a room (not adjacent to any wall).  You can use a series of diagonal moves around this monster to avoid the one who is chasing you while you heal.  Often the one chasing you will reverse directions, so you have to be alert. As long as you don't hit it, the non-mean monster will blithely sleep through the battle raging about it.

At levels where you can expect to meet monsters you can't easily defeat, it's a good idea to be on the lookout for circles.  For instance, if you have explored the center, west, and south rooms, and you see corridors leading from both the west and south rooms to the southwest, you may want to explore that room first, to find secret doors or defeat monsters in it so it is available as a circle.  (There may be only a passageway instead of a room, but you are guaranteed that the passages connect.)  Of course, the shorter the circle, the less chance you have of meeting an itinerant monster as you go around it.

Walking into a teleport trap does not count as running in circles, but it can be very handy when you are being chased by a bad monster.  Remember where your teleport traps are.

At other times you may simply want to leave the level, foregoing any magic you haven't yet discovered.  If you have found trap doors or the standard stairway, you can run away and down to the next level. Monsters never follow you down the stairs or through the trap. Scrolls of magic mapping can be used when you want to run away, to find the stairway.  They work best when you have a choice as to where to go (for instance, in the middle room).

Managing Strength:

A high strength can be a major asset in winning.  The story is that strength from 7-15 does not either hurt or help you.  Values above 15 help by about 1 damage point (with an occasional dexterity point thrown in) per level, and values below 7 hurt both by a damage and a dexterity point per level.

A potion of poison reduces your strength, a potion of gain strength increases it one point, and restore strength restores it to the highest value it has ever been.  Poison dart traps occur on all levels and can rob you of strength, but the greatest threat to your strength is ants.  They appear on levels 3-12.

My general strategy is to try to save all potions I have until I am finished with level 12.  By then my strength is almost always below 16, but still above 6.  I almost never use an identify scroll on a potion, so I have a mystery at level 12.  You would love to encounter your potions in the order poison, restore strength, and gain strength. To maximize your chances, it helps to know that poison potions are less common than restore strength, which are in turn less common than gain strength.  So if you have more than one of some potions, it pays to quaff the ones you have least of first.

I have added one twist to this strategy.  As long as my strength is at 16, I tend to quaff a new, unknown potion shortly after I find it, hoping it will be gain strength.  The main reason is that you are likely to run out of room in your pack before you reach level 12 (and the extra strength can help you with the first 12 levels).

If my strength goes below 7 and there are other good parts to my game, I will try all my potions immediately; it's hard to survive long with strength of 5 or below.

Managing armor:

If I encounter armor that promises to be good (chain mail, band mail, splint mail, or plate mail) on the first few levels, I am likely to simply try it on (and then immediately try to take it off).  It will often be cursed.  If nothing else good has happened to you, you might want to quit and start over.  When you are more invested in your game, you often want to spend an identify scroll to make sure the armor is OK before you try it on. But there are two scrolls which will remove the curse, both "remove curse" and "enchant armor".  So if you have a half dozen scrolls of unknown type, it's not a bad idea to try on the armor and if it is cursed then hope that one of your scrolls will help you get it off.

The only danger to armor is rust monsters, which are present on levels 9-18.  I generally wear armor and take it off when I encounter a rust monster.  If the rust monster got a hit in before you reacted, you will have lost a level of armor strength; taking the armor off takes only one turn, and the armor is off before the monster swings again. (3.4: it takes two turns, and the first is spent with the armor still on.)  Once the rust monster is defeated, I put armor back on.  If I have a choice of armors, I tend to wear less good armor (class 7-5) until at least level 12.  It would be nice if you could save your best armor (class 4 and up) until level 19, but it's often hard to survive if you do.  I often find myself taking my chances with my best armor at level 13 (when trolls first show up).

A ring of maintain armor can be very good.  I rarely wear it all the time because of its drain on food, but whenever you see a rust monster, you can put it on, avoiding the usual drain of an armor point.  (And if space in your pack is tight, you can throw away the ring when you get to level 19!) A staff of cancellation will also cancel the rust-inducing properties of rust monsters.

Strange (and unrealistic) as it may seem, with very good armor (say of class 1 or better) and good fighting strength, I sometimes walk around with no armor on at all.  When I see a bad monster, I then put on my good armor. This requires me to take one hit from the monster without armor and another with armor on before I land my first blow, but the armor is usually good enough to let me still win.  If you are wearing less good armor, this isn't a practical strategy since you would have to take four hits (three of them without much protection) while you change armor.  My strategy protects my good armor from rust monsters most of the time.  This strategy really suggests itself when you don't have any spare armor better than class 9, which happens all too often.  Class 10 (no armor on) is not much worse than class 9.

## Managing Rings

The ring of slow digestion is a very nice ring.  You leave it on constantly because it reduces your food consumption.  The ring of adornment is said to have no effect on food consumption.

The other rings, except aggravate monster and teleportation, cause you to consume food at a greater rate.  Regeneration is the hungriest ring: it triples your food use. Stealth, protection, add strength, maintain strength and maintain armor each double it; dexterity, increase damage and searching add a third; see invisible adds a fifth. (3.6: only regeneration, maintain strength and searching cost extra food.)  Usually this added food consumption is enough so that you will run out of food if you keep the ring on constantly.  One good strategy is to save up your food and then put on the ring for the "dash" from level 20 to 26.  Wearing a ring together with a ring of slow digestion also works, up to a point: slow digestion halves your normal food use, which more than pays for dexterity, increase damage, searching or see invisible, but with stealth or protection on the other hand you still eat half again as fast as normal, and with regeneration two and a half times as fast.  You can also get a lot out of rings by only wearing them at certain times.

When you meet a difficult monster, you might take a hit while you put on your ring of regeneration, assuming you have some space to back up.  This makes your running away strategy much more effective.  (The regeneration ring also heals you during combat, which ordinary healing will not. But every point the ring restores resets your rest count, so ordinary healing stops while it works. From experience level 12 up, ordinary healing while you run is as fast or faster, so at those levels the ring only pays while you are actually trading blows.)  This could also apply to any of the "fighting" rings (dexterity, increase damage, protection, or add strength).

Putting on a ring of maintain armor immediately when a rust monster appears adjacent to you is very effective in keeping your armor intact.  It doesn't protect you from an "ambush" by a rust monster, however.  Maintain strength will similarly work when you run into an ant.  And obviously you can put on your ring of searching only when you want to find something.

The ring of stealth is the best one, and you can get its full effect without wearing it all the time.  The stealth ring does nothing against itinerant monsters, since they always chase you, nor does it do anything against non-mean, settled monsters, who won't chase you in any event (orcs are the exception: ring or no ring, they set off after the room's gold, or after you if there is none).  But it does keep mean, settled monsters from waking up and chasing you.  The only times they may wake up are (a) when you go into or out of the room they are in, and (b) when you end the turn next to them.  So you never have to wear your stealth ring in a corridor, or when going back through a room you have already explored (assuming you didn't tiptoe around any mean monsters there the first time).  Taking the ring off at every opportunity gets tedious, but you can get much of the effect if you keep the ring on when you are going forward and exploring, and taking it off when you need to backtrack.  Remember to put it on again before you go down the stairway!

## Identifying Things

You find lots of unknown magic in the dungeon, as well as weapons and armor that may be cursed.  You never have enough identify scrolls to identify everything.  For the most part, you have to find out about things by trying them out.  This means that you rarely get much benefit from the first scroll or potion of a type that you find.  The good news is that the longer you survive, the more likely you are to find second copies of things you then know how to use.

When you try out a ring or armor and find it is cursed, you are stuck with it until you find the appropriate scroll(s), which may be a long time.  The same goes for weapons you wield; however, the only weapon I ever wield instead of my mace is a two-handed sword, and even when it is cursed it is likely to be better than my mace.

a.  Potions

There is still considerable judgment involved in when you try things out. As mentioned above under Managing Strength, I like to save my potions until I am done with level 12, when ants disappear.  This is convenient because trolls increase the danger of the game considerably at level 13.  I will also sometimes wait until I have just attained a new experience level, so I can get the most benefit out of a potion of raise level.

The bad potions are poison, confusion, paralysis, and blindness (5.3 and 5.4: no paralysis, but hallucination instead), and since you are stuck quaffing beverages at random, you have to be prepared to deal with them.  Blindness can be a real nuisance, but you can usually survive it, especially if encountered before level 13.  You simply walk over every square of every room, and test every square of the sides to see if you can find a passageway.  It may be slow, but you can explore a level while waiting to regain your vision.  You can't search for secret passages, however.  When you meet monsters, you (amazingly) are still as good at fighting them as ever.  When one attacks you in a room, you aren't always clear where it is.  My solution is to back away a few squares until I am sure where the monster is, and then fight.  (This same strategy also applies when fighting invisible stalkers when your sight is intact.) Potions of healing, extra healing, or see invisible cure blindness.

b.  Scrolls

When I can, I save my scrolls until I am done with level 7, sometimes longer.  The increase in danger from the centaurs of level 8 is the reason for picking 7.  Waiting gives me longer to perhaps find better armor (for the enchant armor scroll), a two-handed sword (for the enchant weapon scroll), or a ring or staff I really want to identify (for an identify scroll).  If, as often happens, I have promising armor I haven't tried on yet and six or more unknown scrolls, I will try on the armor (or armors). If one is cursed, I have a very good chance of finding either enchant armor or remove curse among the untried scrolls.

Until I have found the aggravate monsters scroll, I tend not to read new scrolls until I am done with a level; it can be hard to survive the sudden onslaught of monsters without healing time between them.

c.  Scare Monster

If you read this scroll, you hear maniacal laughter.  This scroll works wonders when you drop it.  Once you pick it up again, it turns to dust. But you can sometimes identify it before you pick it up.  Simply arrange for a monster's normal path to lead it over the scroll; if it is scare monster, the monster will step around the scroll; the scroll has its effect before you drop it.  For instance, if the monster is chasing you from the east, be east of the scroll, then step northwest, then southwest.  For a scare scroll the monster will move to your northeast; otherwise it will stand on the scroll to your east.  I used to get carried away leaving scrolls untouched in a room and going to other rooms in search of monsters to lead back over the scrolls, but this has problems: you can fall through a trap door, you can meet a monster coming the other way on your way back to the room, and you can use up a lot of food.  However, I still do this when I see a monster and a scroll in the same room.  I will even take two hits from a manageable monster as I step around it to lead it over the scroll.

Ordinarily you can't lead monsters over scrolls in a corner, but you can still diagnose the scroll if your pack is full.  With a full pack, you stand on the scroll without picking it up, search a turn, and see if the monster hits you.  You can step off it and back on repeatedly; you can lead tough monsters back to it and dispatch them with impunity.  This is a good reason to keep a full pack when possible. (5.3 and 5.4: there the scroll turns to dust even with a full pack, but the m prefix lets you step onto it without picking it up; on the PC the g prefix does the same.)

The same reasoning works (and applies more often) after you drop a scare scroll.  If you had a full pack and there is some other item nearby that you can pick up to replace the scare scroll, you will again have a full pack and can re-use your scare scroll on that level.  When you can do this on a level with purple worms and dragons, you can achieve fabulous experience levels (I think I've gone as high as 16, maybe 17).  The dragons can still hit you with bolts of fire, however.

d.  Staves (aka staffs)

You can try out a staff on a monster and usually know right away what kind of staff it is.  (If it says "you hit the monster", then it is a staff of striking, or else the useless magic missile staff, which self-identifies in this situation.)  But if it is a serious monster and you "haste" it (so it moves twice for every move you make), you may not survive.  Similarly, if you polymorph your friendly jackal into a dragon on level 5, you are unlikely to survive.  So my general rule is to wait until I have 40 or 50 hit points before trying out staves, and only to try them out when I am done exploring a level and am standing on the stairway.  I sometimes have to wait around or go back to some adjoining rooms to find a monster for a guinea pig.  That way you can make a quick escape, even from violet fungi who hold you or umber hulks who confuse you.

e.  Identify scrolls

The top priority use of an identify scroll is to find the number of charges on a staff of teleport away. (5.3 and 5.4: identify comes in five kinds, for potions, scrolls, weapons, armor, and rings, wands and staves, and each works only on its own kind.)  This is because of its immediacy; you want to be able to use it with 1 hit point left, which is likely to be fatal if the last charge is gone.  The number of charges on other good staves, such as polymorph or slow monster, is also important, but since you use them with a reserve of hit points, you usually can use some other immediate magic to survive when your last charge runs out.

Rings are another priority item to identify.  But note that if you have a known scroll of remove curse, you should first try on your unknown ring (ideally two of them, plus some unknown armor) to see if it is cursed.  You don't care what a cursed ring is.  (I have tried using a de-cursed ring of teleportation as a means of defense while running away, but the results in practice aren't very good.) If the ring is not cursed, you can often find out what it is without identifying it.  Add strength rings cause a visible change in your current strength on the status line.  Regeneration gives you back one hit point each turn.  Searching helps you find doorways, which you can test by moving back and forth where there is known to be a secret door.  Sustain strength and maintain armor can be tested by seeking combat with ants and rust monsters, respectively, but this is often not practical because of the damage they do in the usual case where you don't have that ring.  Slow digestion can be determined by putting it on when you first get hungry and noting how long it takes to get weak, but I've rarely done this.

Armor is the next priority item for identify scrolls.  I rarely identify leather armor, studdied leather armor or ring mail, because they aren't worth much anyway except in the rare case where they happen to be enchanted to start with.

I probably use 50% of my identify scrolls on rings, 40% on armor, and 10% on staves.  Don't be afraid to hang onto identify scrolls for use later; you're likely to find something worthwhile.

When I am in dangerous territory (say level 22) and I find a new staff, I'm likely to identify it immediately, since I don't have time to try it out carefully.  The same may go for scrolls, if many have already been identified but a few very good ones are still unknown (scare monster, hold monster, teleportation).

The Best Magic:  Goodness vs Immediacy

One handy rule is to stop and think a while when you first run into a difficult monster.  There is no time pressure in this game.  I've lost many games saying "surely I'll get him this time" after a streak of bad luck with the sword.  If after sober reflection you doubt you are going to win, do you want to use some magic now while you have hit points, rather than using more potent magic later?  This section gives some hints about what magic to use when.

"Goodness" and "immediacy" are two different dimensions of magic.  For instance, slow monster staff is very good, but to use it you need to take one more hit.  "Teleport away" may be less good because the monster chases you again and you have to deal with it later, but it is great that it is immediate: it works with 1 hit point left.  Magic that stops a monster permanently (such as hold monster) has an advantage over magic that limits it for a while (such as the confuse monster scroll).

Here is a list of the best magic and what it can do for you:

Magic With Immediate Effect:

**Very good:**

Teleport away staff: one of the best there is, because you can wait to use it to see if you can beat the monster through conventional means, and then it removes the monster (though it starts running toward you at once).  It is a very good thing to identify because you want to know when that last charge is used up.  Limits: if you are in a room, the monster can get teleported to another square adjacent to you.  This has happened to me, but it is infrequent enough that I just take my chances.

Scroll of hold monster: This holds every monster within two squares of you, permanently, until you attack it (or zap it, or read aggravate monsters).  It has virtually no limitations and will get you out of just about any pickle.  Of course if another monster comes along from more than two squares away, you have to fight it.  But be aware of where the monster(s) are when you use it.  If you hold the monster in the middle of a room, it will then constitute a circle that you can run around in escaping from another monster.  But if you hold the monster in a corridor or blocking a door which you need to use, remember you'll have to fight that monster again after you heal, which may often require more magic.

Scroll of scare monster: This was discussed earlier.  This is terrific because it protects you permanently, until you step off of it.  Two limitations: you can't use it when you're standing on something: weapon, magic, etc., or most importantly, a doorway.  Second, dragons will still shoot bolts of fire at you.  If your pack is full when you drop the scare monster and you can find something else to refill your pack nearby, you can step back onto the scare scroll and re-use it several times on that level. This is a good reason for keeping a full pack, even if some of it is cursed or junk.  (Another reason if that if a nymph gets you, there is less chance she'll take what you really value.)

Potion of extra healing:  This is usually good enough that you gain ground on even the worst monsters while taking a hit from them.  But you have to go on fighting, so it's not the first weapon of choice if you don't think you're about to polish the monster off.

**Good:**

Potion of healing: This is better to use in the upper levels, while facing things like centaurs, than in the depths, because you usually can't gain ground with it against trolls, xorns, umber hulks, purple worms, or dragons.  Sometimes it's useful as a hedge against a new potion turning out to be blindness, because it cures blindness (as does extra healing and see invisible).

Staff of fire, cold, lightning: All three of these work the same, except that fire does nothing to a dragon ("the flame bounces off the dragon").  If you hit the monster, it's usually pretty effective, but if you miss, the bolt can bounce and hit you.  (I've known a dragon's bolt of fire to miss me and kill the umber hulk I was fighting...)  So if you are in desparate straits, it can have immediate effect; but if you are trying to play it safe, you either avoid it or use it when you can take a hit from both the monster and the bolt and still have some option left. It's better against monsters like centaurs and trolls than xorns or purple worms.  Purple worms often dodge the bolt: every monster gets a saving throw that improves with its level, so a purple worm dodges more than half the time, a dragon 45% of the time, and a troll or xorn about a third of the time.

Staff of drain life: Takes half your remaining hit points away, and that many from the monsters in your room or your stretch of corridor (divided among them if there is more than one, even ones across the room that you aren't fighting). You have to use it early in combat, while you still have hit points. This is good against umber hulks who have confused you, if you have lots of hit points.  And it has an advantage against monsters with good armor, because you circumvent the armor (e.g. xorns and dragons).

**So-so:**

Staff of cancellation: These can actually be great if used against rust monsters to protect good armor.  But other uses aren't worth much.  The staff will stop an ant from stinging, a leprechaun or nymph from stealing (though they still carry their gold/magic), vampires from taking your hit points permanently, wraiths from grabbing experience levels, violet fungi from holding you, umber hulks from confusing you, and dragons from shooting fire. It also stops a floating eye's gaze, and shows you an invisible stalker or a disguised mimic.  The umber hulk use sounds promising, but the problem is that usually by the time you know there's an umber hulk there, you're already confused.

Striking: The nice thing is that you always hit, so they can be good against heavily armored monsters like xorns and dragons that you are on the verge of polishing off.  But often you do less damage than you would with your own weapon, if you are strong enough to have survived into the depths. Also note that each time you use it on a monster, it uses TWO charges (in case you have identified the staff and know how many charges are left). (5.3 and 5.4: there is no staff of striking.)

Magic With One Turn Delay:

**Very good:**

Slow monster staff:  You take one hit, then the monster is slowed permanently.  As long as you have space to back up (and just about any room three squares high has enough space to maneuver around the corner and end up going back the other way) you can kill anything by backing up when the monster is active and hitting when the monster is inactive.  There is a limitation against dragons:  if you are backing up and the dragon has a direct line of sight on you (which includes in straight corridors), he can still blast you with fire.  But if you have space in a room to back up diagonally (so that your new position and his old position aren't on a straight line), you avoid this problem.  This can also be effective against a bunch of monsters, giving you time to gain ground on them, especially in corridors.  But be aware that when they reach a room, the ones behind will go around the slow one.

**Good:**

Staff of polymorph: This can be a wonderful piece of magic, because it permanently changes a monster to something else, which you immediately take one hit from.  Because it just randomly selects another monster, though, you're much better off using this in the depths than higher up.  Use it on a dragon or purple worm, and your chances are pretty good of getting a softer monster.  Use it on a centaur, and you may well end up with something worse.  And remember that the new monster might be an ant, floating eye, or rust monster, that you were counting on not seeing any more -- but that is usually an acceptable risk.

Potion of haste self: This is limited because you take a hit immediately, and it wears off pretty quickly.  But it can function like a slow monster charge if you can polish off the monster in four or five swings of your weapon.  (A combination of slow monster and haste self can be very nice, especially if you are in a confined space and can't run away; you land 4 blows to every 1 from the monster.)  If you quaff another potion of haste self while you are already hastened, you faint from exhaustion.

Magic With More Than One Turn Delay:

**Good:**

Scroll of monster confusion:  Here you first have to take a hit while you read the scroll, and then you get no benefit until you actually hit the monster.  Once you do, the monster is confused: it blunders about at random four moves in five (a bat does so only half the time), but it wears off, after about 25 turns on average, though sometimes after only two or three.  The fact that you need a hit makes it better to use against less-well-armored monsters.

Scroll of magic mapping:  This can also be used when not in combat, but in a combat situation it can often show you how to run all the way to the stairway so you can drop through (monsters never follow you down the stairs).  I have often used it with success against Xs and Ps.  Of course you have to hope you don't meet any other monsters along the way.  Best if used early on a level where you have choices about where to go.

Interesting Monsters:

(5.3, 5.4 and PC: most of these monsters are replaced by look-alikes with the same tricks: the rattlesnake has the giant ant's sting, the aquator is the rust monster, the ice monster the floating eye (in 5.3 and 5.4 it can freeze you to death), the venus flytrap the violet fungi, the phantom the invisible stalker, the xeroc the mimic, the medusa the umber hulk, the jabberwock the purple worm, and the black unicorn (the ur-vile on the PC) the xorn.)

Ants are hard to hit and steal your strength points sometimes.  I often spend arrows on them, especially if my strength is at its peak value, or is down around 7 or 8.

Floating eyes are best left alone, once you are committed to your game, for they can transfix you permanently until you die of starvation, if nothing else.  But on the first few levels, when you are taking risks, they are often an easy way to get experience points.

When violet fungi first score a hit, they hold you.  From then on, they take hit points every turn whether they hit you or not, and the amount goes up by one each time they do hit (1, 2, 3, 4, ...).  You can't fight any other monster while you are being held.  But you can beat violet fungi one on one if you've survived that far in the dungeon.

Invisible stalkers are usually not that serious a problem (so the potion and ring of see invisible are not worth much).  Because they are slightly confused, you can often run away.  One good place to run is down a straight corridor and shower them with arrows until they catch up to you.  And in a corridor, you either hit them or chase them.

Leprechauns always carry gold, but if they hit you, they steal your gold and disappear.  If you're trying to win rather than accumulate a high score, all they are worth is their experience points (and they might be standing on some piece of magic or the stairway).  If you do fight them, bow and arrow is a good idea.

Mimics pose as other objects or the stairway.  They are not usually a problem if you keep in mind that any object you see at level 19 and beyond might be a mimic (don't pick up that scroll with 2 hit points left).  It is frustrating when one poses as the Amulet on level 26.

Nymphs are to stuff as leprechauns are to gold.  But they are definitely worth dispatching for what they carry.  Bow and arrow from a distance away is ideal.  When I confront one in a small room, one strategy is to move down a corridor a ways and drop all your best magic (not scare scrolls!), then attack the nymph.  Then if she steals you haven't lost much.  She will never steal the weapon you wield, the armor you are wearing or the rings on your hands, and she only takes magic items.

Vampires sometimes take away from your maximum hit points as well as your current hit points.  They're not exactly welcome, but compared to everything else at level 20, they (and mimics) are a comparative pleasure to meet.

Wraiths sometimes cause you to lose an experience level.  The good news is that if they do so, you get the level back as soon as you kill something, the wraith or anything else.  (If they take two from you, you still get only one back.)  What you always lose is whatever experience points you were accumulating toward the next level. It's interesting to watch what happens to your maximum hit points.  In the typical case where you get back the experience level, your hit points first go down by a random number from 1 to 10, then back up by a different random number.  Sometimes this is bad, but sometimes I have gone from 55 to 54 and back to 64, in which case I thank the departed wraith for his intervention.

The Worst Monsters:

The hobgoblin is the worst monster you have in the game initially. The centaur (level 8) is the next substantial increment in pure fighting ability, followed by the troll (level 13).  But there isn't much special to say about these monsters.  The ones that follow are generally too tough to be called "interesting".

Xorn: These are the best armored monsters in the game, and they have a big bite (like trolls, umber hulks and purple worms).  Slow monster is good (the armor doesn't help them against the staff).  Monster confusion is often frustrating because it can be a long time before you score your first hit and actually confuse the monster.

Umber hulk: The worst monsters of all.  They sometimes (about half the time: you get a saving throw, which improves as you go up experience levels or wear a ring of protection) confuse you the instant you see them, then they take big bites.  Umber hulks are always what I eliminate if I get a genocide scroll.  But note that if they don't confuse you the first time you see them, they never will (exception: if you move next to one and it doesn't "wake up", it can confuse you if it later wakes up.)  In particular, if you teleport away from them somehow and then you encounter them later, they won't confuse you a second time.  If you're not confused, they fight like xorns with less good armor.  But if you are confused, here are your options.  First, if you're in a hallway, you can just swing away, because the game is gracious (unrealistic?) enough to figure that if you hit the wall, you didn't mean to, so when something actually happens, you either back up or hit the umber hulk.  If you're not in a doorway but close to one, you can sometimes get there in time.  I think I have observed that arrows (thrown weapons generally) have a better chance of reaching the umber hulk than blows with a weapon, and that staff charges have an even better chance.  But even they can miss.  This is a good use for a staff of striking (though maybe not your best option for escaping).  Similarly bolts of fire, cold, and lightning are worth trying when you start out with lots of hit points.  The drain life staff is often very good -- provided you have a lot of hit points, and it helps to have good armor; I've often found that two drain life charges will do the trick, especially if the umber hulk misses me after the first one.  Healing or extra healing potions are rarely good enough by themselves.  Slow monster is also rarely good enough by itself, since you can't control your movements to hit with impunity.  But slow monster can be a good choice if you have other "lesser magic" to team it up with.  Teleport away and teleportation are good choices, but even they will often not separate you from the umber hulk by enough so you are unconfused (about 30 turns, anywhere from 18 to 40) before your friend reappears.  Polymorph is a very good choice, because you will quite often get a manageable monster from whom you can take many turns worth of hits until you land a lucky blow to dispatch it.  But use the polymorph early, to allow enough hit points for a "bad polymorph" (care for a dragon?  how about a xorn?) plus what you need to fight a centaur or yeti.  Finally, hold monster or scare monster will usually save you from this encounter, and it's often better to use them right away than use up lesser magic and then discover you need them anyway. With scare monster, remember to mark time by searching until you are unconfused or you'll step right off the scroll!

Purple worm:  These are poorly armored, but with 50% more hit points than anyone else (dragons are next).  They also hardly ever miss, so don't count on your fine armor to save you.  The classic solution is the slow monster staff.  Bolts of fire, cold, and lightning rarely work; the purple worm seems to catch the bolt most of the time.  Monster confusion can help too. What you need to beat them in straight combat is great damage potential and a lot of hit points.  I have rarely had that capability, but have often been able to handle them routinely if I have 20 or 30 squares to retreat over while healing.  They give loads of experience points.

Dragon: With bolts of fire as an option along with the biggest bites of any monster (up to 46 hp), dragons are deadly.  And they are well-armored. Slow monster is great if you are in a room and can back up diagonally in a zigzag pattern.  Running away from them rarely works, though it can if you have enough twists and turns and a few healing potions.  And they can shoot fire at you even when you are standing on a scare monster scroll (but do so with the same frequency they would otherwise -- they don't send a bolt every time).  Monster confusion is often a good bet if you use it right away.  Polymorph is an excellent choice.  Otherwise the teleports are OK, once you have landed some blows; you can heal before you meet the dragon again.  Hold monster is the only thing that always works.  It's often worth considering using magic to kill a dragon instead of polymorphing or escaping since they are worth so many experience points.

Gang of monsters: What do you do when you find a treasure room deep in the dungeon, or worse yet, drop into the middle of one when you go down a staircase?  To a lesser degree, these suggestions apply to two or three monsters that find you in a room.  If you are standing on the doorway, I wouldn't go in; you'd rather fight them one at a time.  Scare monster is the best choice (beware of dragons, as usual), but if you are standing in a doorway and fighting it out, holding the scare scroll in reserve to use if things get bad, it's often best to back up one square into the corridor immediately, in case a monster coming down the corridor sandwiches you where you can't drop your scroll (that is very frustrating).  Teleportation is good (and in this case, is better than teleport away).  Hold monster is good though if you use it in this case, it's often better to wait for the monsters to form a seamless ring around you (if you can wait); otherwise some monsters from more than two squares away will flow through the cracks and attack you.  Haste self can be good if you can use it to get to a doorway, and is in this case better than slow monster.

## The Big Picture Again

Though it takes experience, one thing you want to keep track of is how far above or below average you are at any given time.  If things are going badly, why not try on those rings or that armor, and if they are cursed, give up.  If they are going well, you both want to take fewer risks and attend more closely to your game.  Occasionally you are in such a good position that you should use magic instead of fighting a monster that you could almost certainly beat.  Here are the main factors I take into account in judging my situation:

How is your basic fighting capability?  A two-handed sword is a major good thing.  Strength at 18 or above is quite good.  A good set of armor (class 4) is worth something, and armor of class 1 is worth a lot.  Having a mace that has been enchanted three or four times is almost as good as a plain two-handed sword.  Also, how are your maximum hit points coming?  This you can compute.  You started with 12 at experience level 1, so if you subtract 12 from your current total and 1 from your experience level, and divide, you get the average number of extra hit points you have got per level.  So if I have 54 hit points at level 7, I have an average of (54-12)/(7-1) or 7.  The "average average" is 5.5.  7 is pretty good, 4 is pretty bad.

How much immediately-effective magic do you have?  Teleport away staffs, scrolls of teleportation, scare monster scrolls, hold monster scrolls, drain life staves, and potions of extra healing come to mind.

How much magic with latency do you have?  Polymorph staves, slow monster staves, monster confusion scrolls come to mind.

And how much other magic do you have (genocide on umber hulks, where there is a genocide scroll, and ring of stealth the first ones to consider).

It's hard to win without both a pretty good fighting character and at least some immediately-effective magic.  Sometimes you cannot defeat a monster without magic when they first appear, but with the gain of an experience level or two you find you can.

## On the PC

I have a little experience of the PC version of Rogue, from A.I. Design and Epyx (the details here are as in PC Rogue 1.48). These are the differences that matter.

Some of the monsters have different names:

| PC | Unix |
|---|---|
| aquator | rust monster |
| emu | jackal |
| venus flytrap | violet fungi |
| griffin | (new: flies; nothing like it on Unix) |
| ice monster | floating eye |
| jabberwock | purple worm |
| kestral | kobold |
| medusa | umber hulk |
| phantom | invisible stalker |
| quagga | quasit |
| rattlesnake | giant ant |
| slime | snake (the slime divides when you miss it) |
| ur-vile | xorn |
| xeroc | mimic |

Better armor has a higher number, not a lower. Subtract the Unix armor class from 11 to get the PC number: the starting ring mail, 6 on Unix, shows as 5. (5.3 and 5.4 also count upward, but from 10.)

You can throw a potion at a monster, and it always takes effect if it reaches the monster: a potion of confusion confuses it, for instance. (I could never do this on Unix.)

If you are confused and fighting in a hallway, your confused bumps into the wall count as real turns. This is a big difference from 5.2 and 5.3, which let them pass free. (3.6, 4.22 and 5.4 count them too.)

The Amulet of Yendor does nothing for food consumption, so you need food for the trip up. (From 3.6 to 5.3 carrying it stops ordinary digestion; in 5.4 it doubles it.)

Below level 10 there are sometimes mazes of hallways in place of rooms, which can contain magic, monsters, or the staircase. Monsters have a hard time keeping up with you there, because they head straight for you instead of following the passages, which can be a big advantage. (5.3 and 5.4 have mazes too.)

Ice monsters don't hold you permanently the way floating eyes do: they freeze you with frost bolts from a distance, about 7 turns at a time.

"Haste self" lasts longer: 10 to 13 turns, against 4 to 7 on Unix.

Any teleport leaves you confused briefly, and a fall through a trap door injures you somewhat.

The monsters have different levels where they occur. In general, from centaurs through trolls, the monster appears one level earlier.

There is no genocide scroll; "vorpalize weapon" takes its place. (5.3 and 5.4 have no genocide scroll either.)

The magic detection potion not only detects magic, but tells you whether it is good ($ sign) or bad (+ sign).

--------

Thanks to Torsten Nielsen for helpful comments on an earlier draft.

—Bart Wright

“How to Win at Rogue” circulated by e-mail and on the Usenet group [rec.games.roguelike.rogue](https://groups.google.com/g/rec.games.roguelike.rogue/c/NH7ztjeRFN4), where Mark McConnell reposted it in 1995.

Copyright © 1995 Bart Wright.
