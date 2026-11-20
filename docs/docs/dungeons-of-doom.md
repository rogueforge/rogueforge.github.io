---
title: A Guide to the Dungeons of Doom
summary: Michael Toy and Ken Arnold's original manual for Rogue.
hide_summary: true
---
# A Guide to the Dungeons of Doom

By Michael C. Toy and Kenneth C. R. C. Arnold  
Revised and expanded by the Archmage Yendor

This edition combines the manuals for Rogue 3.4, 3.6, 4.22, 5.2, 5.3 and 5.4 and PC Rogue 1.48, with notes where they differ.

## Introduction

You have just finished your years as a student at the local fighter's guild. After much practice and sweat you have finally completed your training and are ready to embark upon a perilous adventure. As a test of your skills, the local guildmasters have sent you into the Dungeons of Doom. Your task is to return with the Amulet of Yendor. Your reward for the completion of this task will be a full membership in the local guild. In addition, you are allowed to keep all the loot you bring back from the dungeons.

In preparation for your journey, you are given an enchanted mace, a bow, and a quiver of arrows (3.4: an enchanted sword) taken from a dragon's hoard in the far off Dark Mountains. You are also outfitted with elf-crafted armor and given enough food to reach the dungeons. You say goodbye to family and friends for what may be the last time and head up the road.

You set out on your way to the dungeons and after several days of uneventful travel, you see the ancient ruins that mark the entrance to the Dungeons of Doom. It is late at night, so you make camp at the entrance and spend the night sleeping under the open skies. In the morning you gather your weapons, put on your armor, eat what is almost your last food, and enter the dungeons.

## What is going on here?

You have just begun a game of rogue. Your goal is to grab as much treasure as you can, find the Amulet of Yendor, and get out of the Dungeons of Doom alive. On the screen, a map of where you have been and what you have seen on the current dungeon level is kept. As you explore more of the level, it appears on the screen in front of you.

Rogue differs from most computer fantasy games in that it is screen oriented. Commands are all one or two keystrokes<sup class="fnref" id="fnref1"><a href="#fn1" aria-label="Note 1">1</a></sup> and the results of your commands are displayed graphically on the screen rather than being explained in words.<sup class="fnref" id="fnref2"><a href="#fn2" aria-label="Note 2">2</a></sup>

Another major difference between rogue and other computer fantasy games is that once you have solved all the puzzles in a standard fantasy game, it has lost most of its excitement and it ceases to be fun. Rogue, on the other hand, generates a new dungeon every time you play it and even the author finds it an entertaining and exciting game.

## What do all those things on the screen mean?

In order to understand what is going on in rogue you have to first get some grasp of what rogue is doing with the screen. The rogue screen is intended to replace the “You can see ...” descriptions of standard fantasy games. Figure 1 is a sample of what a rogue screen might look like.

```
------------
|..........+
|..@....]..|
|....B.....|
|..........|
-----+------

Level: 1  Gold: 0      Hp: 12(12)  Str: 16(16)  Arm: 4  Exp: 1/0
Figure 1
```

The bottom line of Figure 1 is shown differently in other editions:

```
3.4:        Level: 1  Gold: 0      Hp: 12(12)  Str: 16  Ac: 6  Exp: 1/0
3.6, 4.22:  Level: 1  Gold: 0      Hp: 12(12)  Str: 16  Ac: 6  Exp: 1/0
5.2:        Level: 1  Gold: 0      Hp: 12(12)  Str: 16(16)  Ac: 6  Exp: 1/0
5.3, 5.4:   Level: 1  Gold: 0      Hp: 12(12)  Str: 16(16)  Arm: 4  Exp: 1/0
PC:         Level:1     Hits:12(12)   Str:16(16)    Gold:0     Armor:5
```

### The bottom line

At the bottom line of the screen are a few pieces of cryptic information describing your current status. Here is an explanation of what these things mean:

- **Level**: This number indicates how deep you have gone in the dungeon. It starts at one and goes up as you go deeper into the dungeon.<sup class="fnref" id="fnref3"><a href="#fn3" aria-label="Note 3">3</a></sup>

- **Gold**: The number of gold pieces you have managed to find and keep with you so far.

- **Hp**: Your current and maximum health points. Health points indicate how much damage you can take before you die. The more you get hit in a fight, the lower they get. You can regain health points by resting. The number in parentheses is the maximum number your health points can reach. (3.4 to 5.2: *hit points*. PC: shown as **Hits**, for hit points.)

- **Str**: Your current strength and maximum ever strength. This can be any integer less than or equal to 31, or greater than or equal to three. The higher the number, the stronger you are. The number in the parentheses is the maximum strength you have attained so far this game. (3.4 and 3.6: only your current strength is shown, and it can be at most eighteen, after which it gains a percentage, as in 18/50. 4.22: only your current strength is shown.)

- **Arm**: Your current armor protection. This number indicates how effective your armor is in stopping blows from unfriendly creatures. The higher this number is, the more effective the armor. (3.4 to 5.2: shown as **Ac**, your current armor class, and the *lower* this number is, the more effective the armor. PC: shown as **Armor**, one higher than **Arm**.)

- **Exp**: These two numbers give your current experience level and experience points. As you do things, you gain experience points. At certain experience point totals, you gain an experience level. The more experienced you are, the better you are able to fight and to withstand magical attacks.

When it is time to eat, *Hungry*, *Weak*, or *Faint* appears at the end of the line. (3.4: not shown. 3.6 and 4.22: *Fainting*.)

(PC: the line shows Level, Hits, Str, Gold and Armor, in that order. In place of **Exp** comes your rank in the guild, *Guild Novice* from experience level 2, rising as your experience grows. The hunger warning appears on the line below.)

### The top line

The top line of the screen is reserved for printing messages that describe things that are impossible to represent visually. If you see a “--More--” on the top line (PC: a highlighted “More” after the message), this means that rogue wants to print another message on the screen, but it wants to make certain that you have read the one that is there first. To read the next message, just type a space.

### The rest of the screen

The rest of the screen is the map of the level as you have explored it so far. Each symbol on the screen represents something. Here is a list of what the various symbols mean (PC: apart from the monster letters, the IBM PC's own graphics characters are used instead, such as ☺ for you and ═ ║ for walls; type `/` to list them):

- `@`: This symbol represents you, the adventurer.

- `-|`: These symbols represent the walls of rooms.

- `+`: A door to/from a room.

- `.`: The floor of a room.

- `#`: The floor of a passage between rooms.

- `*`: A pile or pot of gold.

- `)`: A weapon of some sort.

- `]`: A piece of armor.

- `!`: A flask containing a magic potion.

- `?`: A piece of paper, usually a magic scroll.

- `=`: A ring with magic properties (not in 3.4)

- `/`: A magical staff or wand (not in 3.4)

- `^`: A trap, watch out for these.

- `%`: A staircase to other levels (3.4 and 3.6: the passage leading down to the next level)

- `:`: A piece of food.

- `,`: The Amulet of Yendor.

- `A-Z`: The uppercase letters represent the various inhabitants of the Dungeons of Doom. Watch out, they can be nasty and vicious.

## Commands

Commands are given to rogue by typing one or two characters. Most commands can be preceded by a count to repeat them (e.g. typing `10s` will do ten searches). Commands for which counts make no sense have the count ignored. To cancel a count or a prefix, type &lt;ESCAPE&gt;. The list of commands is rather long, but it can be read at any time during the game with the `?` command. Here it is for reference, with a short explanation of each command.

(3.4 has no `z`, `^`, `P`, `c` or `D` command, and 3.6 no `^` or `D`; neither has the commands marked below as 5.3 and later.)

- `?`: The help command. Asks for a character to give help on. If you type a `*`, it will list all the commands, otherwise it will explain what the character you typed does. (PC: `?` simply lists all the commands.)

- `/`: This is the “What is that on the screen?” command. A `/` followed by any character that you see on the level, will tell you what that character is. For instance, typing `/@` will tell you that the `@` symbol represents you, the player. (PC: `/` lists every symbol and what it stands for.)

- `h, H, ^H`: Move left. You move one space to the left. If you use upper case `h`, you will continue to move left until you run into something. This works for all movement commands (e.g. `L` means run in direction `l`) If you use the “control” `h`, you will continue moving in the specified direction until you pass something interesting or run into a wall. You should experiment with this, since it is a very useful command, but very difficult to describe. This also works for all movement commands. (3.4 to 5.2, and PC: these editions describe no “control” run; the `f` prefix does this instead, see below. On the PC the backspace key also moves you left.)

- `j`: Move down.

- `k`: Move up.

- `l`: Move right.

- `y`: Move diagonally up and left.

- `u`: Move diagonally up and right.

- `b`: Move diagonally down and left.

- `n`: Move diagonally down and right.

- `t`: Throw an object. This is a prefix command. When followed with a direction it throws an object in the specified direction. (e.g. type `th` to throw something to the left.) (PC: `t` or `+`.)

- `f`: Fight until someone dies. When followed with a direction this will force you to fight the creature in that direction until either you or it bites the big one. (`f` stops if you get near death; `F` fights on regardless.) (3.4 to 5.2, and PC: `f` is instead the find prefix. When followed by a direction, you continue moving in that direction until you pass something interesting or run into a wall.)

- `m`: Move onto something without picking it up. This will move you one space in the direction you specify and, if there is an object there you can pick up, it won't do it. (5.3 and later; PC: `g`.)

- `z`: Zap prefix. Point a staff or wand in a given direction and fire it. Even non-directional staves must be pointed in some direction to be used. (3.6: `z` zaps in a random direction; `p` and a direction aims it. PC: `z` or `-`.)

- `^`: Identify trap command. If a trap is on your map and you can't remember what type it is, you can get rogue to remind you by getting next to it and typing `^` followed by the direction that would move you on top of it.

- `s`: Search for traps and secret doors. Examine each space immediately adjacent to you for the existence of a trap or secret door. There is a large chance that even if there is something there, you won't find it, so you might have to search a while before you find something.

- `>`: Climb down a staircase to the next level. Not surprisingly, this can only be done if you are standing on staircase.

- `<`: Climb up a staircase to the level above. This can't be done without the Amulet of Yendor in your possession.

- `.`: Rest. This is the “do nothing” command. This is good for waiting and healing. (3.4 and 3.6: space.)

- `,`: Pick up something. This picks up whatever you are currently standing on, if you are standing on anything at all. (5.4 only.)

- `i`: Inventory. List what you are carrying in your pack.

- `I`: Selective inventory. Tells you what a single item in your pack is. (Not in PC.)

- `q`: Quaff one of the potions you are carrying.

- `r`: Read one of the scrolls in your pack.

- `e`: Eat food from your pack.

- `w`: Wield a weapon. Take a weapon out of your pack and carry it for use in combat, replacing the one you are currently using (if any).

- `W`: Wear armor. You can only wear one suit of armor at a time. This takes extra time.

- `T`: Take armor off. You can't remove armor that is cursed. This takes extra time.

- `P`: Put on a ring. You can wear only two rings at a time (one on each hand). If you aren't wearing any rings, this command will ask you which hand you want to wear it on, otherwise, it will place it on the unused hand. The program assumes that you wield your sword in your right hand.

- `R`: Remove a ring. If you are only wearing one ring, this command takes it off. If you are wearing two, it will ask you which one you wish to remove, (3.4: `R` repeats the last message instead.)

- `d`: Drop an object. Take something out of your pack and leave it lying on the floor. Only one object can occupy each space. You cannot drop a cursed object at all if you are wielding or wearing it.

- `c`: Call an object something. If you have a type of object in your pack which you wish to remember something about, you can use the call command to give a name to that type of object. This is usually used when you figure out what a potion, scroll, ring, or staff is after you pick it up, or (5.3 and later) when you want to remember which of those swords in your pack you were wielding.

- `D`: Print out which things you've discovered something about. This command will ask you what type of thing you are interested in. If you type the character for a given type of object (*e.g.* `!` for potion) it will tell you which kinds of that type of object you've discovered (*i.e.*, figured out what they are). This command works for potions, scrolls, rings, and staves and wands. (PC: it doesn't ask, but lists all the kinds of potions, scrolls, rings, and staves and wands you have discovered.)

- `o`: Examine and set options. This command is further explained in the section on options. (PC: `o` only says there are no options.)

- `^R`: Redraws the screen. Useful if spurious messages or transmission errors have messed up the display. (3.4 to 5.2: `^L`. Not in PC.)

- `^P`: Print last message. Useful when a message disappears before you can read it. This only repeats the last message that was not a mistyped command so that you don't loose anything by accidentally typing the wrong character instead of ^P. (3.4: `R`. 3.6, 4.22, 5.2 and PC: `^R`.)

- **&lt;ESCAPE&gt;**: Cancel a command, prefix, or count.

- `!`: Escape to a shell for some commands. (PC: a fake DOS prompt; type `rogue` to return.)

- `Q`: Quit. Leave the game.

- `S`: Save the current game in a file. It will ask you whether you wish to use the default save file. *Caveat*: Rogue won't let you start up a copy of a saved game, and it removes the save file as soon as you start up a restored game. This is to prevent people from saving a game just before a dangerous position and then restarting it if they die. To restore a saved game, give the file name as an argument to rogue. As in

```
% rogue save_file
```

To restart from the default save file (see below), run

```
% rogue -r
```

- `v`: Prints the program version number.

- `)`: Print the weapon you are currently wielding (5.3 and 5.4 only)

- `]`: Print the armor you are currently wearing (5.3 and 5.4 only)

- `=`: Print the rings you are currently wearing (5.3 and 5.4 only)

- `@`: Reprint the status line on the message line (5.3 and 5.4 only)

### Extra commands on the PC

PC Rogue also has these commands:

- `a`: Again. Repeat the last command. (5.4 also has this.)

- `F`: Define the macro. Type the keys you want the macro to stand for, followed by a &lt;RETURN&gt;.

- `^F`: Do the macro: rogue acts as if you had typed its keys yourself.

- `^T`: Switch between terse and long messages.

## Rooms

Rooms in the dungeons are either lit or dark. If you walk into a lit room, the entire room will be drawn on the screen as soon as you enter. If you walk into a dark room, it will only be displayed as you explore it. Upon leaving a room, all monsters inside the room are erased from the screen. (3.4 and 3.6: this happens only on leaving a dark room.) In the darkness you can only see one space in all directions around you. A corridor is always dark. (5.3, 5.4 and PC: deeper in the dungeon, some rooms give way to mazes of twisting passages.)

## Fighting

If you see a monster and you wish to fight it, just attempt to run into it. Many times a monster you find will mind its own business unless you attack it. It is often the case that discretion is the better part of valor.

## Objects you can find

When you find something in the dungeon, it is common to want to pick the object up. This is accomplished in rogue by walking over the object (unless you use the `m` prefix, see above; PC: `g`). If you are carrying too many things, the program will tell you and it won't pick up the object, otherwise it will add it to your pack and tell you what you just picked up.

Many of the commands that operate on objects must prompt you to find out which object you want to use. (PC: usually rogue shows you the items in your pack that will do, and you type the letter of the one you want; see the **menu** option.) If you change your mind and don't want to do that command after all, just type an &lt;ESCAPE&gt; and the command will be aborted.

Some objects, like armor and weapons, are easily differentiated. Others, like scrolls and potions, are given labels which vary according to type. During a game, any two of the same kind of object with the same label are the same type. However, the labels will vary from game to game.

When you use one of these labeled objects, if its effect is obvious, rogue will remember what it is for you. If it's effect isn't extremely obvious you will be asked what you want to scribble on it so you will recognize it later, or you can use the `call` command (see above). (3.4 to 5.2: you are asked only if the **askme** option is set; see below. The 3.4 and 3.6 editions don't mention `call`.)

### Weapons

Some weapons, like arrows, come in bunches, but most come one at a time. In order to use a weapon, you must wield it. To fire an arrow out of a bow, you must first wield the bow, then throw the arrow. You can only wield one weapon at a time, but you can't change weapons if the one you are currently wielding is cursed. The commands to use weapons are `w` (wield) and `t` (throw).

### Armor

There are various sorts of armor lying around in the dungeon. Some of it is enchanted, some is cursed, and some is just normal. Different armor types have different armor protection. The higher the armor protection, the more protection the armor affords against the blows of monsters. Here is a list of the various armor types and their normal armor protection:

| Type | Protection (5.3 and later) | Armor class (3.4 to 5.2) |
|---|---|---|
| None | 0 | 10 |
| Leather armor | 2 | 8 |
| Studded leather / Ring mail | 3 | 7 |
| Scale mail | 4 | 6 |
| Chain mail | 5 | 5 |
| Banded mail / Splint mail | 6 | 4 |
| Plate mail | 7 | 3 |

(3.4 to 5.2: these editions give armor *class*, which runs the other way: the lower the armor class, the more protection the armor affords, so enchanted armor has a lower class than normal and cursed armor a higher one. The 3.4 and 3.6 tables have no “None” row. PC: the protection shown is one more than in this table, *e.g.* 3 for leather armor.)

If a piece of armor is enchanted, its armor protection will be higher than normal. If a suit of armor is cursed, its armor protection will be lower, and you will not be able to remove it. However, not all armor with a protection that is lower than normal is cursed.

The commands to use armor are `W` (wear) and `T` (take off).

### Scrolls

Scrolls come with titles in an unknown tongue.<sup class="fnref" id="fnref4"><a href="#fn4" aria-label="Note 4">4</a></sup> After you read a scroll, it disappears from your pack. The command to use a scroll is `r` (read).

### Potions

Potions are labeled by the color of the liquid inside the flask. They disappear after being quaffed. The command to use a potion is `q` (quaff).

### Staves and Wands

(Not in 3.4.) Staves and wands do the same kinds of things. Staves are identified by a type of wood; wands by a type of metal or bone. They are generally things you want to do to something over a long distance, so you must point them at what you wish to affect to use them. Some staves are not affected by the direction they are pointed, though. Staves come with multiple magic charges, the number being random, and when they are used up, the staff is just a piece of wood or metal.

The command to use a wand or staff is `z` (zap)

### Rings

(Not in 3.4.) Rings are very useful items, since they are relatively permanent magic, unlike the usually fleeting effects of potions, scrolls, and staves. Of course, the bad rings are also more powerful. Most rings also cause you to use up food more rapidly, the rate varying with the type of ring. Rings are differentiated by their stone settings. The commands to use rings are `P` (put on) and `R` (remove).

### Food

(This subsection first appears in the 5.3 edition. In 3.4 and 3.6 you faint from hunger but never starve to death.)

Food is necessary to keep you going. If you go too long without eating you will faint, and eventually die of starvation. The command to use food is `e` (eat).

## Options

Due to variations in personal tastes and conceptions of the way rogue should do things, there are a set of options you can set that cause rogue to behave in various different ways.

### Setting the options

There are two ways to set the options. The first is with the `o` command of rogue; the second is with the `ROGUEOPTS` environment variable.<sup class="fnref" id="fnref5"><a href="#fn5" aria-label="Note 5">5</a></sup> (PC: neither. Options are read from a file when rogue starts; see below.)

#### Using the `o` command

When you type `o` in rogue, it clears the screen and displays the current settings for all the options. It then places the cursor by the value of the first option and waits for you to type. You can type a &lt;RETURN&gt; which means to go to the next option, a `-` which means to go to the previous option, an &lt;ESCAPE&gt; which means to return to the game, or you can give the option a value. For boolean options this merely involves typing `t` for true or `f` for false. For string options, type the new value followed by a &lt;RETURN&gt;.

#### The rogue.opt file (PC only)

PC Rogue has no `o` command (it just says “i don't have any options, oh my!”) and no ROGUEOPTS. Instead it reads the file `rogue.opt` in the current directory when it starts. The file has one option on each line, written as the name of the option, an equals sign, and its value. A `#` begins a comment. For instance,

```
# rogue options
name = Blue Meanie
fruit = mango
```

#### Using the ROGUEOPTS variable

The ROGUEOPTS variable is a string containing a comma separated list of initial values for the various options. Boolean variables can be turned on by listing their name or turned off by putting a `no` in front of the name. Thus to set up an environment variable so that **jump** is on, **terse** is off, and the **name** is set to “Blue Meanie”, use the command<sup class="fnref" id="fnref6"><a href="#fn6" aria-label="Note 6">6</a></sup>

```
% setenv ROGUEOPTS "jump,noterse,name=Blue Meanie"
```

### Option list

Here is a list of the options and an explanation of what each one is for. The default value for each is enclosed in square brackets. For character string options, input over fifty characters will be ignored. (3.4 and 3.6: the name should be less than eighty characters long. 4.22: less than eighty.)

(PC: the options are **name** [*Rodney*], **fruit** [*Slime Mold*], **savefile** [*rogue.sav*], **scorefile** [*rogue.scr*], **menu** and **macro**, plus **drive** and **screen** (`bw` for black and white). The others are not options: rogue always acts as if **flush** and **passgo** were set.)

- **terse** [*noterse*]: Useful for those who are tired of the sometimes lengthy messages of rogue. This is a useful option for playing on slow terminals, so this option defaults to *terse* if you are on a slow (1200 baud or under) terminal. (PC: the `^T` command switches between terse and long messages during a game.)

- **jump** [*nojump*]: If this option is set, running moves will not be displayed until you reach the end of the move. This saves considerable cpu and display time. This option defaults to *jump* if you are using a slow terminal.

- **flush** [*noflush*]: All typeahead is thrown away after each round of battle. This is useful for those who type far ahead and then watch in dismay as a Bat kills them.

- **step** [*nostep*]: (3.4 to 5.2.) When **step** is set, lists of things, like inventories or `*` responses to “Which item do you wish to **. . .**? ” questions, are displayed one item at a time on the top of the screen, rather than clearing the screen, displaying the list, then re-displaying the dungeon level.

- **askme** [*noaskme*]: (3.4 to 5.2.) Upon reading a scroll or quaffing a potion which does not automatically identify itself upon use, rogue will ask you what to name it so you can recognize it if you encounter it again. (In 5.3, 5.4 and PC rogue always asks; see “Objects you can find”.)

- **seefloor** [*seefloor*]: Display the floor around you on the screen as you move through dark rooms. Due to the amount of characters generated, this option defaults to *noseefloor* if you are using a slow terminal. (5.3 and later.)

- **passgo** [*nopassgo*]: Follow turnings in passageways. If you run in a passage and you run into stone or a wall, rogue will see if it can turn to the right or left. If it can only turn one way, it will turn that way. If it can turn either or neither, it will stop. This algorithm can sometimes lead to slightly confusing occurrences which is why it defaults to *nopassgo*. (Not in 3.4 or 3.6.)

- **tombstone** [*tombstone*]: Print out the tombstone at the end if you get killed. This is nice but slow, so you can turn it off if you like. (5.3 and later; 5.4 calls it **score**.)

- **inven** [*overwrite*]: Inventory type. This can have one of three values: *overwrite*, *slow*, or *clear*. With *overwrite* the top lines of the map are overwritten with the list when inventory is requested or when “Which item do you wish to **. . .**? ” questions are answered with a `*`. However, if the list is longer than a screenful, the screen is cleared. With *slow*, lists are displayed one item at a time on the top of the screen, and with *clear*, the screen is cleared, the list is displayed, and then the dungeon level is re-displayed. Due to speed considerations, *clear* is the default for terminals without clear-to-end-of-line capabilities. (5.3 and later; *slow* does what **step** did.)

- **name** [account name]: This is the name of your character. It is used if you get on the top ten scorer's list.

- **fruit** [*slime-mold*]: This should hold the name of a fruit that you enjoy eating. It is basically a whimsey that rogue uses in a couple of places.

- **file** [*~/rogue.save*]: The default file name for saving the game. If your phone is hung up by accident, rogue will automatically save the game in this file. The file name may start with the special character `~` which expands to be your home directory. (3.4: the default is *rogue.save* in the current directory.)

- **menu** [*on*]: (PC only.) How rogue asks which item you want to use. With *on*, it lists the items in your pack that will do and you choose one by its letter. With *sel*, it does so for everything but eating and dropping. With *off*, it just asks for the letter; type a `*` to see the list.

- **macro** [*v*]: (PC only.) The keys that the `^F` command types for you. It can also be set with the `F` command.

## Scoring

(This section first appears in the 4.22 edition.)

Rogue usually maintains a list of the top scoring people or scores on your machine. Depending on how it is set up, it can post either the top scores or the top players. In the latter case, each account on the machine can post only one non-winning score on this list. If you score higher than someone else on this list, or better your previous score on the list, you will be inserted in the proper place under your current name. How many scores are kept can also be set up by whoever installs it on your machine. (3.4 and 3.6: the list is always the top ten scores. 4.22 and 5.2: the top ten players, with one non-winning score per account.)

(PC: Rogue maintains a list of the ten best scores on your machine, in the Guildmaster's Hall of Fame. If you score higher than someone else on this list, you will be inserted in the proper place under your current name. Those who reach the 26th level of the dungeon are Honored by the Guild.)

If you quit the game, you get out with all of your gold intact. If, however, you get killed in the Dungeons of Doom, your body is forwarded to your next-of-kin, along with 90% of your gold; ten percent of your gold is kept by the Dungeons' wizard as a fee.<sup class="fnref" id="fnref7"><a href="#fn7" aria-label="Note 7">7</a></sup> This should make you consider whether you want to take one last hit at that monster and possibly live, or quit and thus stop with whatever you have. If you quit, you do get all your gold, but if you swing and live, you might find more.

If you just want to see what the current top players/games list is, you can type

```
% rogue -s
```

## Acknowledgements

Rogue was originally conceived of by Glenn Wichman and Michael Toy. Ken Arnold and Michael Toy then smoothed out the user interface, and added jillions of new features. (PC: Jon Lane and Mel Sibony of A.I. Design adapted it for the IBM PC, and Epyx published their version in 1985.) We would like to thank Bob Arnold, Michelle Busch, Andy Hatcher, Kipp Hickman, Mark Horton, Daniel Jensen, Bill Joy, Joe Kalash, Steve Maurer, Marty McNary, Jan Miller, and Scott Nelson for their ideas and assistance; and also the teeming multitudes who graciously ignored work, school, and social life to play rogue and send us bugs, complaints, suggestions, and just plain flames. And also Mom.

## Notes

<ol class="footnotes">
<li id="fn1">As opposed to pseudo English sentences. <a class="fnback" href="#fnref1" aria-label="Back to text">↩&#xFE0E;</a></li>
<li id="fn2">A minimum screen size of 24 lines by 80 columns is required. If the screen is larger, only the 24x80 section will be used for the map. (5.3 and later.) <a class="fnback" href="#fnref2" aria-label="Back to text">↩&#xFE0E;</a></li>
<li id="fn3">Or until you get killed or decide to quit. (3.4 and 3.6, where the dungeon level “starts at one and goes up forever”.) <a class="fnback" href="#fnref3" aria-label="Back to text">↩&#xFE0E;</a></li>
<li id="fn4">Actually, it’s a dialect spoken only by the twenty-seven members of a tribe in Outer Mongolia, but you’re not supposed to <em>know</em> that. (5.3 and later.) <a class="fnback" href="#fnref4" aria-label="Back to text">↩&#xFE0E;</a></li>
<li id="fn5">On Version 6 systems, there is no equivalent of the ROGUEOPTS feature. (In 3.4 and 3.6 this is part of the text.) <a class="fnback" href="#fnref5" aria-label="Back to text">↩&#xFE0E;</a></li>
<li id="fn6">For those of you who use the Bourne shell <code>sh</code>(1), the commands would be <code>ROGUEOPTS="jump,noterse,name=Blue Meanie"; export ROGUEOPTS</code>. (3.4 and 3.6 use their own example, <code>jump,noterse,name=Conan the Barbarian,fruit=mango</code>.) <a class="fnback" href="#fnref6" aria-label="Back to text">↩&#xFE0E;</a></li>
<li id="fn7">The Dungeon’s wizard is named Wally the Wonder Badger. Invocations should be accompanied by a sizable donation. (5.3 and later.) <a class="fnback" href="#fnref7" aria-label="Back to text">↩&#xFE0E;</a></li>
</ol>

Copyright © 1980, 1981 Michael Toy and Ken Arnold.
