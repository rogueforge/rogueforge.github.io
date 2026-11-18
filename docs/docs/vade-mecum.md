---
title: The Rogue's Vade-Mecum
summary: A companion to A Guide to the Dungeons of Doom, for Rogue 3.4 to 5.4 and PC Rogue 1.48.
---
# The Rogue's Vade-Mecum

By George Sicherman  
Revised and expanded by the Archmage Yendor

This edition corrects the text against the games' source code and adds notes for Rogue 3.4, 5.4 and PC Rogue 1.48.

## Introduction

To play *rogue*, the dungeon game written by M. C. Toy and friends, you need know no more than how to operate a terminal. To survive in a *rogue* dungeon for long, you need a great deal of specialized knowledge. This document is designed to provide some of that knowledge. You are supposed to have read *A Guide to the Dungeons of Doom* by M. C. Toy. (The Guide was revised by K. C. R. C. Arnold for version 4.)

This document describes version 4.2 of Rogue. Discrepancies in other versions are noted in the text. In general, “V3” means versions 3.4 and 3.6 (a note marked “3.4” shows where they differ, and a table's V3 column is 3.6), “V4” means version 4.2 (and later versions to 5.2), and “V5” means version 5.3. “PC” means PC Rogue 1.48 (A.I. Design/Epyx), which generally follows V4 but has the V5 monsters. Notes marked “5.4” apply only to version 5.4.

## Architecture

### Rooms

Each level of a dungeon normally contains nine rectangular rooms, arranged three by three. Up to three rooms may be replaced by winding or dead-end passages.

A room will always be at least two paces long and from two to five paces wide, not counting the walls. It may be lighted or dark. In a dark room you can see only one pace in each direction; in a lighted room you can see all over.

In V4 and V5, one level in twenty will have a *treasure room*. A treasure room is a room filled with lots of scrolls, flasks, weapons, sandwiches, and a horrible smell. The smell comes from having eight or ten monsters packed into one room. To make matters worse, some of the monsters may be denizens of the next level down. When you appear in the doorway, several of the monsters will attack you, as will any monsters you brush against.

It is entirely up to you whether to stand and fight or head for the stairs. If you want to fight, do it in the doorway.

### Mazes

In V5, and in PC below level 10, you may find a maze in place of a room. A maze wanders throughout a rectangular area. Like rooms, mazes may contain treasure, magic objects, and monsters. Mazes may also be treasure rooms; these are as dangerous as ordinary treasure rooms, except that the monsters cannot easily gang up on you.

### Doors

Each room will contain one or more doors leading to passages. A door may be secret; you will discover such a door only if you *search* for it. No wall of a room can contain more than one door, and walls that face the edge of the display never contain doors.

### Passages

Any two adjacent rooms may be joined by a passage between the corresponding walls. Rooms that are not adjacent may be joined by a winding passage. Each level will contain at least eight passages, enough to let you travel from any room to any other. Passages are always dark; you cannot light them with staves or wands.

In V5 passages may have secret connections.

### Stairways

A stairway is a passage to the next lower level. Actually a stairway is nothing more than a hole in the floor, so you cannot go back up without magical assistance. Monsters never use stairways. Each level has just one stairway.

### Traps

While exploring the dungeon, you must beware of the following booby traps:

- **Trap Door**: Plunges you into the next lower level.
- **Bear Trap**: Holds you fast for three turns.
- **Sleeping-Gas Trap**: Puts you to sleep for five turns.
- **Arrow Trap**: Wounds you.
- **Poison Dart Trap**: Wounds you by 1d4 and may weaken you (in V3 it always does).
- **Rust Trap (V5 only)**: Rusts your armor.
- **Teleport Trap**: Sends you somewhere else in the current level.
- **Mysterious Trap (5.4 only)**: Harmless; it just prints a strange message.

Experience and good armor help avert arrows and poison darts (in V3, only experience). (In 3.4 a trap vanishes once it has been sprung.)

The probability of a level's being booby trapped is the level number divided by 10. Levels 10 and below are always booby trapped.

### Searching

Each time you search you have one chance in five of finding a secret door if one lies next to you, and one chance in two of finding a trap. When you wear a ring of searching, your searches become more effective but not certain. If you are looking for an outlet from a room, the most efficient pattern of searching is to search at every third pace:

```
        -----------------
        |.@..@..@..@..@.|
        |...............|
```

When you are blind, searching is a waste of time.

```
   Probability of Missing a Secret Door.

        Number of    Probability
        Searches     of Missing
        ------------------------
           1            .800
           2            .640
           3            .512
           4            .410
           5            .328
           6            .262
           7            .210
           8            .168
           9            .134
          10            .107
          12            .069
          15            .035
```

## Monsters

The dungeon is populated with 26 kinds of monster, corresponding to the 26 letters of the alphabet.

| Monsters (V3, V4) |  |  |  |  |  |
|---|---|---|---|---|---|
|  | Name | HD | AC | Level | Damage |
| A | giant ant | 2 | 3 | 3–12 | 1d6 |
| B | bat | 1 | 3 | 1–8 | 1d2 |
| C | centaur | 4 | 4 | 8–17 | 1d6+1d6 |
| D | dragon | 10 | −1 | 22– | 1d8+1d8+3d10 |
| E | floating eye | 1 | 9 | 2–11 | 0d0 |
| F | violet fungi | 8 | 3 | 15–24 | variable |
| G | gnome | 1 | 5 | 6–15 | 1d6 |
| H | hobgoblin | 1 | 5 | 1–10 | 1d8 |
| I | invisible stalker | 8 | 3 | 16–25 | 4d4 |
| J | jackal | 1 | 7 | 1–7 | 1d2 |
| K | kobold | 1 | 7 | 1–6 | 1d4 |
| L | leprechaun | 3 | 8 | 7–16 | 1d1 |
| M | mimic | 7 | 7 | 19– | 3d4 |
| N | nymph | 3 | 9 | 11–20 | 0d0 |
| O | orc | 1 | 6 | 4–13 | 1d8 |
| P | purple worm | 15 | 6 | 21– | 2d12+2d4 |
| Q | quasit | 3 | 2 | 10–19 | 1d2+1d2+1d4 |
| R | rust monster | 5 | 2 | 9–18 | 0d0+0d0 |
| S | snake | 1 | 5 | 1–9 | 1d3 |
| T | troll | 6 | 4 | 13–22 | 1d8+1d8+2d6 |
| U | umber hulk | 8 | 2 | 18– | 3d4+3d4+2d5 |
| V | vampire | 8 | 1 | 20– | 1d10 |
| W | wraith | 5 | 4 | 14–23 | 1d6 |
| X | xorn | 7 | −2 | 17–26 | 1d3+1d3+1d3+4d6 |
| Y | yeti | 4 | 6 | 12–21 | 1d6+1d6 |
| Z | zombie | 2 | 8 | 5–14 | 1d8 |

The first column tells the monster's *hit dice*: its hit points are determined by rolling as many eight-sided dice as this number. For example, a Dragon's hit points could be anywhere between 10 and 80. The remaining columns give the armor class (q.v.) of the monster, the dungeon levels it inhabits, and the damage it does to you. Plus signs separate multiple attacks; for instance, a Xorn can attack you four times in one turn. (3.4: Bat armor class 6; Jackal 1–6, Kobold 1–7, Hobgoblin 1–9, Snake 1–10.) Some monsters have special powers:

- If the *Giant Ant* hits you, you must save against poison or lose one point of strength. A class-one rogue will get stung 65% of the time; experience helps you resist stings.
- The *Bat* moves about even while fighting.
- The *Dragon* belches fire (not in V3).
- The *Floating Eye* cannot hurt you, but it can paralyze you with its hypnotic gaze. (PC: the *Ice Monster* instead shoots frost like the Dragon's fire; unless you save against magic, it freezes you for 7 turns.)
- If the *Violet Fungi* seizes you, it (they?) engulfs you so you cannot run from it. It does not actually strike you, but exudes a rotting poison. The longer you struggle with it, the faster you lose hit points.
- The *Invisible Stalker* is invisible. It also moves about while fighting (not in 3.4).
- The *Leprechaun* steals some of your gold and promptly vanishes. If you save against magic, you lose only 2+1d120 on dungeon level 7, 2+1d130 on level 8, and so on. Otherwise you lose five times as much. If you kill the Leprechaun, you will find a crock of gold. Occasionally you will meet a chief Leprechaun; his hoard is five times as big as a normal Leprechaun's.
- The *Mimic* can imitate objects, including stairways.
- The *Nymph* steals something valuable and promptly vanishes.
- If an *Orc* and a gold hoard are in the same room, the Orc will run to guard the gold instead of attacking you. (In V3 it is the *Dragon* that does this.)
- The *Rust Monster* does not hurt you, but it corrodes any kind of armor except unstudded leather (in V3, leather too).
- In PC the *Slime* is sluggish unless next to you, and when you miss it, it usually divides in two.
- In V3 the *Troll* regenerates, making it hard to kill.
- Unless you save against magic, the gaze of the *Umber Hulk* confuses you for 20 to 40 turns (V5: about 20).
- The *Vampire* can inflict bites that reduce your maximum hit points by 1d5 (V5: 1d3). In V3 it cannot, but it regenerates instead.
- The *Wraith* can inflict poisoned wounds that reduce your level of wizardry and your maximum hit points. (If your level falls below 1, you die.)

In version 5 the catalogue of monsters is slightly different. The renamed monsters mostly keep their old statistics, but the *Quagga* is a different beast from the Quasit (armor class 3, 1d5+1d5, and carries nothing), the *Black Unicorn* does 1d9+1d9+2d9, the *Xeroc* 4d4 and the *Centaur* 1d2+1d5+1d5, and some monsters turn up at different depths: the venus flytrap from level 12, the xeroc from 16. (In PC most monsters come a level shallower than in V4, but the xeroc stays at 19 and the griffin comes from 17.)

| Version 4 | Version 5 |  |  |
|---|---|---|---|
| A | giant ant | R | rattlesnake |
| E | floating eye | I | ice monster |
| F | violet fungi | F | venus' fly-trap |
| G | gnome |  |  |
| I | invisible stalker | P | phantom |
| J | jackal | E | emu |
| K | kobold | K | kestrel |
| M | mimic | X | xeroc |
| P | purple worm | J | jabberwock |
| Q | quasit | Q | quagga |
| R | rust monster | A | aquator |
| U | umber hulk | M | medusa |
| X | xorn | U | black unicorn |
|  |  | G | griffin |

PC has the V5 set, except that the *Slime* (2 hit dice, armor class 8, 1d3) takes the snake's place and the *Ur-vile* the black unicorn's, and it spells "kestral". PC's renamed monsters all keep their V4 statistics (so the quagga is a quasit and the ur-vile a xorn), but its ice monster and leprechaun bite for 1d2.

The *Griffin* has 13 hit dice, armor class 2, and 4d3/3d5 damage (PC: 4d3/3d5/4d3). The *Griffin*, like the *Bat* and the *Kestrel*, can fly twice as fast as you can run.

Each dungeon level initially contains one or more monsters (the average number is four). They stay put until you do something to get their attention, and the *Violet Fungi* never stir under any circumstances. Sleeping bats, centaurs, eyes, gnomes, invisible stalkers, leprechauns, mimics, nymphs, purple worms, wraiths, and yetis go on snoring till you attack them. (From V4, a greedy orc wakes as soon as it sees you.) The other monsters usually wake up when you approach them.

Every 80 turns or so a new monster will crawl out of the woodwork and start prowling around the current level at random. This monster will not be a dragon, floating eye, violet fungi, leprechaun, mimic, or nymph (in V3, nor a troll or purple worm; PC allows the ice monster, and its emus, zombies, quaggas and ur-viles come only this way).

When you kill a monster you will occasionally find gold or a magic object on the carcass (not in 3.4). Such objects are no more likely to be beneficent than objects found in the ordinary way. The probability of finding something depends on the kind of monster:

| Object-carrying Monsters |  |
|---|---|
| Monster | Probability |
| Centaur | .15 |
| Dragon | 1.00 |
| Gnome | .10 |
| Mimic | .30 |
| Nymph | 1.00 |
| Orc | .15 |
| Purple Worm | .70 |
| Quasit | .30 |
| Troll | .50 |
| Umber Hulk | .40 |
| Vampire | .20 |
| Yeti | .30 |

## Objects

As you explore the dungeon, you will find various objects. Some are inherently magical; others are not magical unless they happen to bear a spell or curse.

```
            Distribution of Items (PC as V4)

        Symbol Item          %(3.4) %(V3) %(V4) %(V5)
        ---------------------------------------------
        ]      Armor             10     9     8     7
        :      Food              20    18    17    16
        !      Potion            30    27    27    26
        =      Ring              --     5     5     4
        ?      Scroll            30    27    30    36
        /      Staff or Wand     --     5     5     4
        )      Weapon            10     9     8     7
```

### Magical Objects

#### Scrolls

Scrolls have strange titles. When you read one, it vanishes and something strange happens.

- **Identify:** identifies any object you possess. Normally used for magical objects, but can also determine the strength of weapons or armor.
- **Identify armor; identify potion; identify ring, wand or staff; identify scroll; identify weapon:** like *identify*, but they work only for particular kinds of objects.
- **Enchant armor:** the armor you are wearing will glow blue for a moment, indicating that it has been strengthened. If the armor has a curse, this will lift it.
- **Enchant weapon:** the weapon you are wielding will glow blue for a moment, indicating that it has been strengthened. If the weapon has a curse, this will lift it.
- **Vorpalize weapon (PC only):** the weapon you are wielding flashes with white light and gains +1 to hit and damage. It also becomes a weapon of slaying against one kind of monster, chosen at random but favoring the deadliest; *identify* tells you which, and the weapon flashes the first time you see one. Against that kind it is a further +4 to hit and damage, and you can *zap* it once to make one of them vanish. Reading a second scroll on the same weapon destroys it.
- **Food detection:** all food on the current level will be displayed.
- **Light:** lights up the room you are in. Does not work in passages.
- **Magic mapping:** draws a map of the current level, showing all rooms, doorways, passages, and stairways. In V5 it shows all traps too.
- **Monster confusion:** causes your hands to glow red. The next monster you hit will be confused.
- **Remove curse:** lifts the curse from accursed objects so that you can take them off or put them down.
- **Sleep:** puts you into a refreshing sleep for 4-8 turns.
- **Teleportation:** teleports you at random to somewhere else in the current level.
- **Aggravate monsters:** all monsters on the current level will sense your presence and react accordingly.
- **Create monster:** creates a monster right before your eyes. The monster will be appropriate to the dungeon level; e.g., you cannot create a Dragon on Level 1.
- **Gold detection:** reports the location of all gold hoards on the current level. If none, you will feel a pull downwards.
- **Hold monster:** paralyzes any monster within two paces (PC: three) of you. If you attack it, you break the spell.
- **Protect armor:** rustproofs the armor you are wearing. It does not lift a curse.
- **Genocide (not in 3.4):** lets you wipe out any one species of monster throughout the dungeon. There is only one of these (V3: no limit).
- **Blank paper (not in 3.4):** does nothing.
- **Scare monster:** If you set this scroll on the floor, no monster will step on it. If you stupidly read it, it will vanish and you will hear maniacal laughter in the distance.

```
                   Distribution of Scrolls

        Name                          %(3.4) %(V3) %(V4) %(V5) %(PC)
        ------------------------------------------------------------
        Aggravate Monsters                 3     1     4     3     4
        Blank Paper                       --     1     1    --     1
        Create Monster                     4     5     5     4     5
        Enchant Armor                      8     8     8     7     8
        Enchant Weapon                    10    10    10     8    10
        Food Detection                    --    --    --     2     4
        Genocide                          --     1     1    --    --
        Gold Detection                     4     4     4    --    --
        Hold Monster                       2     2     3     2     3
        Identify                          20    21    27    --    27
        Identify Armor                    --    --    --     7    --
        Identify Potion                   --    --    --    10    --
        Identify Ring, Wand, or Staff     --    --    --    10    --
        Identify Scroll                   --    --    --    10    --
        Identify Weapon                   --    --    --     6    --
        Light                             11    10    --    --    --
        Magic Mapping                      5     5     5     4     5
        Monster Confusion                  8     8     8     7     8
        Protect Armor                     --    --    --     2    --
        Remove Curse                      10     8     8     7     8
        Scare Monster                      4     4     4     3     4
        Sleep                              5     5     5     3     5
        Teleportation                      6     7     7     5     7
        Vorpalize Weapon                  --    --    --    --     1
```

#### Potions

Potions are magic drinks. When you drink one, something strange happens to you. They come in various colors for easy identification. Unfortunately, the code changes from one game to the next.

- **Gain strength:** you will feel stronger. Add 1 to your strength rating.
- **Healing:** you will feel better. Increase your hit points, though not above your maximum, by throwing a number of four-sided dice equal to your experience level. If this would take you above your maximum, raise the maximum +1. Also cures blindness.
- **Levitation:** lifts you into the air. You will be unable to pick objects up or use stairs until the potion wears off.
- **Magic detection:** displays all magic objects on the current level, including weapons and armor that are enchanted, accursed, or rusty. If you have grabbed all the magic objects, you will have a strange feeling for a moment, then it will pass.
- **Monster detection:** you will sense the presence of monsters. Displays all monsters on the current level. (Of course, more may arrive later.) If you have killed all the monsters, you will have a strange feeling for a moment, then it will pass.
- **See invisible:** you will be able to perceive invisible creatures, particularly Invisible Stalkers, for about 850 turns (3.4: 150; PC: 300). It also cures blindness.
- **Extra healing:** like a potion of healing, but double strength. Also cures blindness and (V5) hallucination.
- **Haste self:** you will feel yourself moving much faster. Score more hits on monsters, and outrun them if they're chasing you. If you drink two at once, you will faint.
- **Raise level:** adds 1 to your experience level.
- **Restore Strength:** restores your strength to its highest previous value.
- **Blindness (not in 3.4):** you can't see until the potion wears off 850 turns later (PC: 300). If it's any consolation, you can't be transfixed by Floating Eyes or confused by Umber Hulks.
- **Confusion:** your moves will be in a random direction until the potion wears off 25 turns later.
- **Hallucination:** the appearance of objects and monsters will change continuously.
- **Paralysis:** you can't move until the potion wears off three turns later.
- **Poison:** subtracts 1d3 from your strength rating. Cures hallucination. If you wear a ring of *Sustain Strength*, your strength will endure—and the potion will not cure hallucination!
- **Thirst quenching (not in 3.4):** this potion tastes extremely dull. Not even carbonated!

In PC you can also throw a potion at a monster. It always hits and shatters: confusion and blindness confuse the monster, paralysis holds it, and healing, extra healing, raise level and haste self help it. Other potions are wasted.

```
             Distribution of Potions (PC as V4)

        Name              %(3.4) %(V3) %(V4) %(V5)
        ------------------------------------------
        Blindness             --     4     4     5
        Confusion              8     8     8     7
        Extra healing          5     5     5     5
        Gain strength         20    15    15    13
        Hallucination         --    --    --     8
        Haste self             3     4     4     5
        Healing               15    15    15    13
        Levitation            --    --    --     6
        Magic detection        6     6     6     6
        Monster detection      5     6     6     6
        Paralysis             10    10    10    --
        Poison                10     8     8     8
        Raise level            2     2     2     2
        Restore strength      15    14    14    13
        See invisible          1     2     2     3
        Thirst quenching      --     1     1    --
```

#### Rings

Rings (not in 3.4) confer magic powers on the wearer. You can wear only one ring on each hand at one time. Rings are set with various stones for easy identification. As with potions, the code changes from game to game.

- **Add strength:** increases your fighting strength.
- **Dexterity:** increases your fighting dexterity.
- **Protection:** protects you against hits from monsters.
- **Searching:** helps you find secret doors and traps.
- **See invisible:** lets you see invisible things, like Invisible Stalkers.
- **Increase damage:** monsters will be hurt worse by your blows.
- **Maintain armor (not in v3):** prevents rust monsters from corroding the armor you are wearing.
- **Regeneration:** makes your wounds heal faster, one HP per turn. If you wear two rings of regeneration at once, you will gain two HP per turn.
- **Slow digestion:** lets you travel twice as far on a ration of food. If you wear two of these, you will never get hungry.
- **Stealth:** enables you to sneak up on monsters without being noticed.
- **Sustain strength:** prevents you from being weakened by potions, dart traps, and Giant Ants.
- **Teleportation:** frequently teleports you without warning to somewhere else in the current level.
- **Aggravate monster:** attracts monsters.
- **Adornment:** looks impressive! but no magic powers.

The effect of a ring of *Protection*, *Add Strength*, *Dexterity*, or *Increase Damage* is determined by its increment. Increments are listed in inventories as signed integers; e.g., “a +2 ring of dexterity.” A ring's increment may be −1; such a ring will be accursed, which means you cannot take it off without a scroll of *Remove Curse*. Two apparently identical rings may bear different increments. Rings of *Teleportation* and *Aggravate Monster* are always accursed.

Wearing almost any ring will make you get hungry faster. (In V3 only Regeneration, Searching, and Sustain Strength do.) You can compute your rate of digestion by adding the appropriate increments from the table to 1.0.

```
    Distribution and Metabolic Effect of Rings (V4)
    
        Name               | %(V3) %(V4) Effect
        -------------------+-------------------                 
        Add strength       |   9     9    +1.00 
        Adornment          |   1     1     ----
        Aggravate monsters |  11    10     ----
        Dexterity          |   8     8     +.33  
        Increase damage    |   8     8     +.33  
        Maintain armor     |  --     5    +1.00 
        Protection         |   9     9    +1.00 
        Regeneration       |   4     4    +2.00 
        Searching          |  10    10     +.33  
        See invisible      |  10    10     +.20  
        Slow digestion     |   9     9     -.50 
        Stealth            |   7     7    +1.00 
        Sustain strength   |   5     5    +1.00 
        Teleportation      |   9     5     ----
```

A ring's increment or decrement does not affect its effect on your digestion.

#### Staves and wands

Staves and wands (not in 3.4) may be pointed in any direction. (You can also use them as weapons if necessary.) Staves are made of various materials, most of them woods. Wands are made of inorganic materials. The only difference between staves and wands is that staves do more damage when you use them as weapons.

When you first find a staff or wand, it bears 2+1d5 charges. When you have exhausted the charges, it has no more magic power.

- **Light:** lights up the room you are in. Unlike the others, this starts with 9+1d10 charges.
- **Striking (not in V5):** for hitting monsters on the head. It always hits its mark (in V3 it is only +3 to hit), bears a +3 damage increment, and does 1d8 damage (PC: +4 and 2d8). One charge in twenty bears a +9 increment and does 3d8 damage.
- **Lightning:** shoots a bolt of lightning. It never misses, though the monster may save against magic. Its range is six paces, and its damage is 6d6. Bolts can bounce off walls.
- **Fire:** shoots a burst of flame. In other respects it resembles lightning.
- **Cold:** shoots a blast of ice. In other respects it resembles lightning.
- **Magic missile:** shoots a magic missile at a monster. Its range is unlimited. It never misses, bears a +1 damage increment, and does 1d4 (PC: 1d8) of damage unless the monster saves against magic.
- **Haste Monster:** makes a monster hit you faster than you hit it, and outrun you when it's chasing you.
- **Invisibility (V5 only):** confers invisibility on a monster.
- **Polymorph:** changes a monster into some other kind of monster.
- **Slow monster:** makes a monster hit you slower than you hit it, and run twice as slow as you when it's chasing you.
- **Drain life:** drains the life from a monster. You lose half your hit points, and the monster loses an equal amount (in V3, twice as much). If you are whole, this is an excellent way of dealing with such horrors as dragons and purple worms.
- **Teleport Away:** teleports a monster to somewhere else in the current level. A useful way to buy time.
- **Cancellation:** cancels a monster's magic powers. For instance, it will prevent an umber hulk from confusing you with its gaze (not in V3). Works on ants, dragons, eyes, fungi, invisible stalkers, leprechauns, nymphs, rust monsters, umber hulks, vampires, and wraiths. Except in V3, it also unmasks mimics.
- **Teleport to:** teleports a monster to you. Don't use this unless you know you can defeat the monster and want the experience.
- **Nothing:** a dud. The only reason to carry one of these is in the hope that a nymph will steal it instead of something valuable.

```
          Distribution of Staves and Wands (V3, V4, PC)
  
            Cancellation   5    Magic missile 10
            Cold           3    Nothing        1
            Drain life     9    Polymorph     15
            Fire           3    Slow monster  11
            Haste monster  9    Striking       9
            Light         12    Teleport away  5
            Lightning      3    Teleport to    5
```

#### The Amulet of Yendor

The *Amulet of Yendor* is unique. It confers upon its owner the power of levitation. You cannot escape from a dungeon without it, since the elevators have been out of order for centuries.

### Ordinary Objects

#### Weapons

You may acquire many kinds of weapons in *rogue*.

```
                      Weapons

        Weapon                    held thrown
        --------------------------------------
        arrow                     1d1   2d3*
        crossbow (not in V5)      1d1   1d1
        crossbow bolt (not in V5) 1d2   2d5*
        dagger                    1d6   1d4
        dart                      1d1   1d3
        long sword                3d4*  1d2
        mace                      2d4   1d3
        rock (V3 only)            1d2   1d4
        short bow                 1d1   1d1
        sling (V3 only)           0d0   0d0
        shuriken (V5 only)        1d2   2d4
        spear                     2d3*  1d6
        two-handed sword          4d4*  1d2
 
        staff                     2d3   1d1
        wand                      1d1   1d1

        bare hands                1d4   ---

        * In V3: arrow 1d6, crossbow bolt 1d10, long sword 1d10,
          spear 1d8, two-handed sword 3d6; and darts, daggers,
          and spears do their "held" damage when thrown.
```

To improve your aim, wield a short bow to shoot arrows, and a crossbow to shoot crossbow bolts. (Except in V4, an arrow or bolt thrown by hand does only 1d1. In PC anything thrown by hand does its “held” damage.) To shoot an item, *wield* the appropriate weapon and *throw* the item.

Every weapon has two increments, one for accuracy and one for damage. Against most monsters, damage increments are worth more than accuracy increments. Either increment may be raised by enchantments or lowered by curses. If a weapon is cursed, you can let go of it only by reading a scroll of *Enchant Weapon* or *Remove Curse*. One weapon in ten is accursed, and one in twenty is enchanted.

Staves and wands (except *Striking*) carry no increments, and except in V3 they cannot be raised by magic scrolls.

#### Armor

This table shows the kinds of armor you may find.

```
           Classes and Distribution of Armor

        Name                  Class Class(V5)  %
        ----------------------------------------
        Leather armor          [8]    [2]     20
        Studded leather armor  [7]    [3]     15
        Ring mail              [7]    [3]     15
        Scale mail             [6]    [4]     13
        Chain mail             [5]    [5]     12
        Splint mail            [4]    [6]     10
        Banded mail            [4]    [6]     10
        Plate mail             [3]    [7]      5
```

Enchantments may raise the strength of armor, curses may lower it, and Rust Monsters (and, in V5, Rust Traps) may lower non-leather armor (in V3, any armor) as far as class 9/1. (Street clothes are class 10/0.) Accursed armor cannot be taken off without a scroll of *Enchant Armor* or *Remove Curse*. Twenty per cent of all armor is accursed, and eight per cent is enchanted.

Class −5/15 armor is proof against bats and hobgoblins. Class −19/29 armor is proof against anything, even purple worms.

In V5 and PC the better the armor, the higher its class; PC's classes are one higher than V5's (leather 3, street clothes 1). In older versions the better the armor, the lower its class.

#### Food

You enter the dungeon with one ration of food. In the dungeon you will find two kinds of food: standard rations, and fruits. Unless you set the “fruit” option to something palatable, the fruits will be slime molds. One ration in ten is a fruit (3.4: one in twenty, and another one in twenty is an awful-tasting ration).

Standard rations come in two flavors: good, and awful. They are equivalent except that you gain 1 experience point when you eat awful-tasting food. (Slime molds are always yummy in this game.)

An average ration of food will keep you going for 1300 turns. After at most 1700 turns without eating, you will be told that you are hungry. (In 3.4 each meal simply resets the clock: you get hungry 1000 turns after your last meal.) If you persist, you will be told 150 turns later that you are weak from hunger. The remedy is to *eat* some food. If you do not, after another 150 turns you will start fainting at frequent, unpredictable intervals. Eventually you will die of starvation (in V3 you just go on fainting).

## Experience

When you defeat a monster, you gain experience points according to the following table:

```
                     Experience (V4)

        A     9  |  H*   3  |  O*    5  |  U  200
        B*    1  |  I  120  |  P  4000  |  V  350
        C    15  |  J*   2  |  Q    32  |  W   55
        D  6800  |  K*   1  |  R    20  |  X  190
        E*    5  |  L   10  |  S*    2  |  Y   50
        F    80  |  M  100  |  T   120  |  Z    6
        G*    7  |  N   37
```

```
                     Experience (PC)

        A    20  |  H*   3  |  O*    5  |  U  190
        B*    1  |  I*  15  |  P   120  |  V  350
        C    25  |  J 4000  |  Q    32  |  W   55
        D  6800  |  K*   1  |  R     9  |  X  100
        E*    2  |  L   10  |  S     1  |  Y   50
        F    80  |  M  200  |  T   120  |  Z    6
        G  2000  |  N   37
```

To these values, add a bonus of one-sixth the monster's hit points (one-eighth for starred monsters). The bonus is multiplied by 4 for monsters with more than six hit dice, and by 20 for monsters with ten or more. You also get a bonus for killing monsters below dungeon level 26, since these monsters are abnormally tough. (None of these bonuses exists in V3.)

You gain 1 experience point for eating awful-tasting food.

Your experience level is determined according to the following table. Each time your experience level rises, your current and maximum hit points increase by 1d10. You also grow more adept at fighting, and your wounds heal faster.

```
                      Experience Level

        Experience  Experience  Experience Heal Rate
        Points (V4) Points (V5)   Level    (HP:turns)
        ---------------------------------------------
                0           0       1        1:19
               10          10       2        1:17
               20          20       3        1:15
               40          40       4        1:13
               80          80       5        1:11
              160         160       6        1:9
              320         320       7        1:7
              640         640       8        1:3
            1,280       1,300       9        1d2:3
            2,560       2,600      10        1d3:3
            5,120       5,200      11        1d4:3
           10,240      13,000      12        1d5:3
           20,480      26,000      13        1d6:3
           40,920      50,000      14        1d7:3
           81,920     100,000      15        1d8:3
          163,840     200,000      16        1d9:3
          327,680     400,000      17        1d10:3
          655,360     800,000      18        1d11:3
        1,310,720   2,000,000      19        1d12:3
        2,621,440   4,000,000      20        1d13:3
        ---------   8,000,000      21        1d14:3
```

## Fighting

### Basic strategy

When you attack a monster, your chance of hitting it is 5% times your experience level, plus 5% times the monster's armor class, plus 5% for each point of your weapon's bonus to hit. A monster's chance of hitting you is 5% times its hit dice, plus 5% times your armor class, minus 5% for each increment on any rings of protection you are wearing. In V4 and V5 add 20% while you are helpless, and also until the first time you recover from being frozen or put to sleep; in PC, always add 20%. A fight consists of you and a monster hitting each other until one of you runs out of hit points. During a fight you should always keep one eye on your HP.

The following table gives each monster's maximum ability to wound you.

```
        Maximum Damage by Monster (V3, V4).

          A  6  |  H  8  |  O  8  |  U 34
          B  2  |  I 16  |  P 32  |  V 10
          C 12  |  J  2  |  Q  8  |  W  6
          D 46  |  K  4  |  R  0  |  X 33
          E  0  |  L  1  |  S  3  |  Y 12
          F --  |  M 12  |  T 28  |  Z  8
          G  6  |  N  0
```

```
        Maximum Damage by Monster (V5; PC: G 39, I 2, L 2, Q 8, U 33, X 12).

        A  0  |  H  8  |  O  8  |  U 36
        B  2  |  I  0  |  P 16  |  V 10
        C 12  |  J 32  |  Q 10  |  W  6
        D 46  |  K  4  |  R  6  |  X 16
        E  2  |  L  1  |  S  3  |  Y 12
        F --  |  M 34  |  T 28  |  Z  8
        G 27  |  N  0
```

Thus, if you are fighting a Hobgoblin and your hit points fall to 8 or less, the Hobgoblin can kill you in a single turn and you had better think about running away. (In PC, monsters do only half damage, rounded up, until you first go below dungeon level 1.)

How hard you can hit a monster depends on your weapon and your physical strength.

| Strength and Damage |  |  |  |
|---|---|---|---|
| Strength (V3) | Strength (V4) | Strength (PC) | Damage |
| 3 | 3 | 3 | −4 |
| 4 | 4 | 4 | −3 |
| 5 | 5 | 5 | −2 |
| 6 | 6 | 6 | −1 |
| 7–15 | 7–15 | 7–15 | 0 |
| 16–17 | 16–17 | 16 | +1 |
| 18 | 18 | 17 | +2 |
| 18/01–18/75 | 19–20 | 18–19 | +3 |
| 18/76–18/90 | 21 | 20–21 | +4 |
| 18/91–18/99 | 22–30 | 22–30 | +5 |
| 18/00 | 31 | 31 | +6 |

When you start out as a level-1 rogue, your fights will tend to go badly for two reasons:

1. you lack dexterity;
2. you have only 12 hit points.

At level 1, Hobgoblins are your most dangerous opponents (1d8). With strength 16, no experience, a (+1,+1) mace, +1 ring mail, and 12 hit points, if you fight a Hobgoblin to the death you stand about one chance in six of being killed (V3: one in ten), assuming that you attack first. (If you are down to 1 hit point, the odds turn against you.) But even a Jackal or Snake may land some lucky blows while avoiding your clumsy swings. When you are dangerously low on hit points, start running! This not only forestalls disaster, it gives you a chance to recover from your wounds.

Since monsters can run diagonally as well as you can, your best bet is to head straight for the nearest corridor in the opposite direction from the monster. When you have recovered enough to be able to withstand another blow, you can strike again. A set of rooms connected in a circle is especially useful; it lets you go on running indefinitely, or at least until your path is blocked by another monster.

The etiquette of fighting is as follows: if you step into a space adjacent to a monster, the monster will strike first. If you and the monster step simultaneously into adjacent spaces, you may strike first. A sleeping monster will not strike first.

### Free-for-alls

Now and then you will be jumped by two or more monsters at once, or be fighting one monster when another monster joins in the fighting. It is good strategy to retreat into a doorway or passage. Since passages have room for only one monster at a time, you can dispatch your opponents singly.

If you are cornered, try to kill the most critical monsters first. Gnomes, Hobgoblins, and Orcs are critical because you can kill them fast and they can hurt you significantly if you don't. Trolls, Umber Hulks, and Xorns are critical for the opposite reason: they can kill you fast if you don't take them out of action. Monsters such as Centaurs, Jackals, and Mimics are not critical; their strength is not disproportionately greater than their endurance.

### Escaping

Since monsters can run diagonally as well as you can, your best bet is to head straight for the nearest corridor in the opposite direction from the monster. The longer you run, the more your wounds heal. When you have recovered enough to be able to withstand another blow, you can strike again.

A set of rooms connected in a circle is especially useful; it lets you go on running indefinitely. Another way to go on running is to run around a monster that is sound asleep. These methods fail if another monster attacks you from the other direction, so if you are in great danger, consider using a magic wand instead of running away.

### Monsters with special powers

Some monsters are best attacked with missile weapons such as bow and arrows. Floating Eyes, Leprechauns, and Nymphs are sitting ducks for such attacks, since they always sit still unless attacked or aggravated. When you find one, you can withdraw to a safe distance and start shooting. If the room is too small for this tactic, you are better off leaving the monster alone. Leprechauns and Nymphs need only one hit on you to get what they want. (You can guard valuable items against a Nymph by simply dropping them before the fight.)

Long-range attacks are advisable against any special monster, provided you know the monster's position in advance. Normally you get such information by means of potions of *Monster Detection* or staves or wands of *Light* (in V3, scrolls of *Light* too). Room size is not critical when you fight non-thieving monsters, since you can switch to a mace or sword when the monster is about to reach you.

In any case, when you finish dispatching a monster with bow and arrows, switch back to a mace or sword at your first opportunity.

### Floating Eyes

When a Floating Eye hits you, it transfixes you for two or three turns. While you are transfixed it keeps attacking you, and the hypnotic effect is cumulative. Thus you may remain transfixed until you starve or another monster comes along and eats you. (V5 and PC have no Floating Eye. V5's Ice Monster freezes you the same way, and if your frozen time piles up past 50 turns you die of hypothermia. PC's Ice Monster instead freezes you with frost bolts from a distance, for 7 turns at a time.)

The better your armor, the more likely you are to avoid this fate. This table gives your chances, assuming that your first blow fails to kill the Eye.

```
         Probability of Being Permanently Transfixed

               AC      Prob. | AC      Prob.
               --------------+--------------
                3      0.000 |  7      0.346
                4      0.038 |  8      0.425
                5      0.156 |  9      0.498
                6      0.257 | 10      0.564
```

It helps to have a ring of *Protection*.

### Rust Monsters

When fighting a Rust Monster, take your armor off! You don't need it against a Rust Monster, and it will deteriorate rapidly if you leave it on. Since a Rust Monster can normally score two hits on your armor before you get it off, advance notice of Rust Monsters is very useful.

Naturally this advice does not hold if you are being attacked by other monsters, or if your armor is already so rusty that it cannot get worse, or if you are wearing accursed armor.

Rust Monsters are found at levels 9 to 18 (PC: 8 to 17). At these levels you should usually wear your second-best or third-best suit of armor, to save your best suit from Rust Monsters.

### Using magic

When you are in a tight spot, don't panic! There is more than one way to skin a monster. Take inventory and see what you have on hand.

#### Potions

A potion of *Healing* will instantly cure some of your wounds, although this may not help you very long against super-monsters like Dragons and Purple Worms. A potion of *Haste Self* will enable you to move twice as fast as your opponent. If you are greatly weakened, a potion of *Restore Strength* may turn the battle in your favor at the cost of one turn.

If you are desperate, an unidentified potion may help you out.

#### Scrolls

A scroll of *Genocide* will not only annihilate your opponent, it will forestall further attacks by his relatives. A scroll of *Hold Monster* is also very effective; *Confuse Monster* is less effective, because you must hit the monster to confuse it and a confused monster can still hit you. A scroll of *Teleportation* gives you a breathing spell.

The best place to drop a scroll of *Scare Monster* is in a straight passage. The monster will halt, gnashing its teeth at you. Being too stupid to run away, it can be dispatched at your leisure with missile weapons.

#### Staves and wands

Most staves and wands are good in a fight. *Haste Monster*, *Teleport To*, *Invisibility*, and *Nothing* are obvious exceptions. There are four things to watch out for:

1. A staff or wand may run out of charges just when you need it most. Unless you were forewarned by a scroll of Identify, you will find out only when you try to use the staff or wand and nothing happens. Do not waste staves and wands!
2. Some monsters are resistant to magic attacks. Shoot a bolt of cold at a troll and it may bounce back at you.
3. Staves of *Drain Life* are non-directional. If two or more monsters are attacking you, they share the damage equally.
4. When you use a staff or wand of *Polymorph*, anything can happen. A Troll could turn into a Jackal, but it could just as easily become a Purple Worm.

#### Time Warp

Thanks to a potion of *Haste Self* or a staff of *Slow Monster*, you may find yourself moving twice as fast as the monster you are fighting. There are three ways to use this advantage.

1. You can run. This will save your hide, but does you little credit.
2. You can stand and fight, dealing two blows for each of the monster's. This does you credit, but may also do you in, particularly when you are fighting a Xorn.
3. You can fight and run on alternate turns. This way you can gradually wear down even a Xorn without sustaining a scratch.

On the other hand, if you may have unwittingly used a staff of *Haste Monster*, you have only two options: fight or run. If you run, even a Snake can gradually do you in without sustaining a scratch from you. Never run from a hasty monster!

## More about using magic

### Identification

The easiest way to identify an object is with a scroll of Identify. If you do not have one, there are other ways.

#### Scrolls

You can usually identify a scroll by reading it. Scrolls of *Identify*, *Genocide*, *Magic Mapping*, *Food Detection*, *Gold Detection*, *Light*, and *Sleep* announce themselves immediately (the detection scrolls only if there is something to detect). Scrolls of *Monster Confusion*, *Enchant Weapon*, *Enchant Armor*, *Remove Curse*, *Aggravate Monsters*, *Scare Monster*, and *Blank Paper* produce characteristic messages. Scrolls of *Teleportation* and *Create Monster* produce no message, but their effect is obvious. Only a scroll of *Hold Monster* cannot be recognized by reading it (unless a monster is standing near you).

#### Potions

You can identify a potion by quaffing it. The only potions that occasionally cannot be recognized this way are *Monster Detection* and *Magic Detection*.

#### Rings

You can tell whether a ring is cursed by putting it on and then trying to remove it. If it is cursed you will fail. This method cannot be wholeheartedly recommended.

A few rings can be readily recognized by their effects. A ring of *Add Strength* will immediately alter your displayed strength. You can tell a ring of *Regeneration* by the remarkable speed with which your wounds heal after a battle. A ring of *Sustain Strength* makes itself known as soon as a Giant Ant stings you, and a ring of *Maintain Armor* as soon as a Rust Monster bites you. A ring of *Teleportation* jumps you all over the dungeon.

A ring of *Searching* announces itself when you first find a trap without searching for it. A ring of *See Invisible* has no effect until you see your first Invisible Stalker at level 16 (V5 and PC: 15) or lower. You can tell that you are wearing a ring of *Aggravate Monsters* when a Leprechaun attacks you without provocation.

Other rings must be recognized by gradual inference.

#### Staves and wands

Most staves and wands produce characteristic effects. A staff of *Light* announces itself explicitly. Staves of *Lightning*, *Fire*, and *Cold* produce the same kind of messages, but an inventory will tell you what they shoot. Staves of *Magic Missile* and *Striking* have characteristic messages.

Staves of *Drain Life* resemble staves of *Teleport Away*. The difference is that when you drain a monster's life away you will be told that you have defeated it, and your hit points will be lower.

A staff of *Teleport To* may be mistaken for a staff of *Cancellation* if you use it against a monster that is already attacking you. The only way to distinguish them is by zapping a distant monster. It is very hard to recognize a staff of *Cancellation* until you use it on a monster with special powers. You can easily mistake a staff of *Nothing* for either of these.

Wands of *Slow Monster* and *Haste Monster* are easy to recognize. You will land two blows to the monster's one, or one to its two. A wand of *Polymorph* is just as easy to recognize except when it happens to change a monster into itself.

#### Armor

As soon as you wear a suit of mail, its strength is displayed. The only drawback is that the mail may be cursed. This hazard is somewhat compensated by the prospect of discovering that your spare suit of scale mail is +3.

### Gaining strength

Potions of *Restore Strength* raise your strength to its highest previous level. Since such potions are fairly common, you should try to maximize your highest strength. The best time to drink a potion of *Gain Strength* is when your strength is at maximum; that is, at the beginning of the game or just after you drink a potion of *Restore Strength*. Experienced rogues save their potions of *Gain Strength* until they find a potion of *Restore Strength*. If your strength is 6 or lower, you may wish to drink a potion of *Gain Strength* at once, to keep monsters from kicking sand at you.

### Enchanting armor

There are three popular ways to use a scroll of *Enchant Armor*:

1. To remove an accursed suit of armor. Of course a scroll of *Remove Curse* will serve just as well, if you can only find one.
2. To create one very good suit of armor. Plus-3 banded mail is a great comfort when you are expecting Vampires or Xorns.
3. To create a good suit of rust-proof armor (not in V3, where leather rusts too). Normal leather armor is class-8; if you raise it to class 5 you are well protected against Trolls and Rust Monsters alike.

### Polymorph

If you are well supplied with wands of *Polymorph* early in your career, you can have some fun when you find a sleeping monster in a long, lighted room. Go as far away from the monster as you can, change it into something vicious, and kill it with arrows. The experience will promote you to a high level of wizardry.

Dragons, Purple Worms, and Xorns are not good candidates for this campaign. They are likely to ignore your arrows and eat you.

If you have a spare scroll of *Scare Monster*, you can take on any creature. You may even choose to read a scroll of *Aggravate Monsters* first.

### Using Black Magic

Don't throw away that wand of *Haste Monster*! Besides making cheap presents for Nymphs, bad magic things can often be put to good use.

#### Scrolls

A scroll of *Aggravate Monsters* will draw Leprechauns and Nymphs from small rooms to big ones where you can shoot them down. If you are standing on a scroll of *Scare Monster*, then you can fearlessly attract all monsters (except Dragons).

#### Potions

A potion of *Levitation* can be very handy for passing a trap in front of a doorway. It also lets you pass by monsters without waking them.

*Poison* cures hallucination (unless you are wearing a ring of *Sustain Strength*).

If you're afraid of Umber Hulks or Medusas (or Floating Eyes), quaff a potion of *Blindness*. Then again, maybe you're better off confused!

#### Rings

If you're outmatched in a fight, put on a ring of *Teleportation*. It might save your life at the cost of some inconvenience.

#### Staves and Wands

Don't count on a wand of *Invisibility* to keep a Medusa from confusing you: her gaze works just as well when you can't see her, and the zap wakes her up.

When two monsters are pursuing you through a room, use a wand of *Haste Monster* to speed up the monster you'd rather fight. When you reach the doorway, the Zombie and not the Troll will be attacking you; this may give you time for a draught of *Healing* or a change of armor.

*Teleport To* can also be used for this purpose.

#### Traps

Trap Doors and Teleport Traps are both good for escaping from monsters.

## Exploring

At the higher levels of the dungeon, try to discover and explore every room. Remember that each of the nine sectors of the level must be occupied by a room, a winding passage, or a dead-end passage. With enough searching you should be able to find them all.

There are only two foolproof ways to distinguish a dead-end passage from a passage that leads to a room:

1. Every room must be at least two paces long and two paces wide, not counting the walls. If there is not enough space at the end of the passage for the room to exist, you are in a dead-end passage.
2. A scroll of *Magic Mapping* settles all doubts.

If you cannot tell whether you are in a dead-end passage, search for a while and then give up. Do not judge by the length of the passage; some dead-end passages are very short.

When you enter a dark room, it is good practice to find the doorways at once. On the other hand, there is no need to walk along a wall that cannot have any doorways because of its position. If a room extends to the edge of the screen, you do not even need to verify that the wall on that side of the room exists.

To traverse a dark room with straight sweeps is easy but not economical. For example:

```
        |.............
        +@@@@@@@@@@@@.
        ----------+---
```

By running straight across the room, you explore an area three paces wide. A better method is shown below:

```
        -----+--------
        |.@.@.@.@.@.@.
        +@.@.@.@.@.@..
        ----------+---
```

By zigzagging you can explore an area four paces wide. In this example you save a whole trip. In general you can expect to save 33% on mileage.

To avoid traps, retrace your steps as much as possible instead of treading on new spaces. By zigzagging as shown above, you can cut your risk roughly in half.

When you have descended to a level at which the monsters threaten to end your career permanently, it becomes very important to discover doorways and stairways. Do not stubbornly insist on exploring every room. Be content with finding a moderate hoard of gold or a valuable object or two. If pursued by something you cannot withstand, just head like blazes for the stairway.

And when you find a stairway on level 19 or lower (V5: 16), test it by walking on it. It could be a mimic!

## Secret Commands

Typing a control-P (^P) makes you a Dungeon Master with enormous power, but only if you know the password. (This is used mainly to debug the program, and is left out of the standard V4 and V5 programs; in V5 sources the command is + rather than ^P. PC has no wizard mode at all.)

You may also start out as a Dungeon Master by invoking *rogue* with a null argument; i.e.,

```
        rogue '' ...
```

You will still need the password.

If you become a Dungeon Master, you can sense all monsters on the current level (in V3, type ^X to see them). You can also use the following special commands (3.4 has only C, @, ^D, ^F, ^I, ^P and ^W):

- **C**: Put a new object in your pack. You must specify the type and ordinal; e.g., “!” and “6” for a potion of *Monster Detection*.
- **@**: Display your present coordinates.
- **^A**: Count the objects in your pack.
- **^C**: Display the corridors.
- **^D**: Go down to the next lower level.
- **^E**: Display how much longer you can go without eating.
- **^F**: Display the current level, showing everything but monsters. Secret doors appear as **&** (V4: as highlighted walls).
- **^H**: Give yourself a +1,+1 two-handed sword, +8 plate mail, and nine more levels of experience.
- **^I**: List the gold hoards and objects lying around on the current level.
- **^N**: Recharge a staff or wand.
- **^P**: Become an ordinary magic user.
- **^T**: Teleport yourself somewhere.
- **^U**: Go up to the next higher level.
- **^W**: Identify something.

These commands are not robust. By abusing them you can go up to dungeon level −3, drink a tiger's eye potion, or wear a ring of Lightning.

## Winning

If you ever manage to get out of the dungeon alive, you can sell all your booty to the Guild and retire from exploring. The Amulet of Yendor is worth 1,000 gold pieces. The worth of other magical objects in V4 is shown in the following table (V3 and V5 prices differ somewhat; PC has *Vorpalize weapon* and *Food detection* in place of *Genocide* and *Gold detection*, at the same prices; in 3.4 any potion or scroll fetches 50 to 149 at random).

```
                            Scrolls
        -----------------------+-----------------------
        Genocide ........ 300  | Remove curse ..... 105
        Scare monster ... 200  | Identify ......... 100
        Hold monster .... 180  | Create monster .... 75 
        Teleportation ... 165  | Gold detection .... 50 
        Enchant armor ... 160  | Aggravate monsters  20 
        Magic mapping ... 150  | Sleep .............. 5  
        Enchant weapon .. 150  | Blank paper ........ 5  
        Monster confusion 140  |                    
        
                            Potions          
        -----------------------+-----------------------                
        Raise level ..... 250  | Magic detection .. 105
        Extra healing ... 200  | See invisible .... 100
        Haste self ...... 190  | Blindness .......... 5  
        Gain strength ... 150  | Confusion .......... 5  
        Monster detection 130  | Paralysis .......... 5  
        Healing ......... 130  | Poison ............. 5  
        Restore strength  130  | Thirst quenching ... 5  
        
                             Rings            
        -----------------------+-----------------------
        Stealth ......... 470  | Maintain armor ... 380
        Regeneration .... 460  | See invisible .... 310
        Dexterity ....... 440  | Sustain strength . 280
        Searching ....... 420  | Slow digestion ... 240
        Protection  ..... 400  | Teleportation ..... 30 
        Add strength .... 400  | Aggravate monster . 10 
        Increase damage . 400  | Adornment ......... 10 
        
                        Staves & Wands   
        -----------------------+-----------------------
        Slow monster      350  | Cancellation       280
        Teleport away     340  | Light              250
        Cold              330  | Magic missile      170
        Lightning         330  | Striking            75 
        Fire              330  | Teleport to         50 
        Polymorph         310  | Haste monster        5  
        Drain life        300  | Nothing              5  
```

The prices for rings, staves and wands are basic. Each charge on a staff or wand adds 20 gold pieces to the value, and each increment on a ring adds 100 (V3: 20); a ring is also worth the value of its stone. For example, a +1 ring of increase damage set in granite is worth 505 (V3: 420). Any ring with a decrement is worth 10 (V3: 50). All unidentified magic objects go for half price.

The price of armor and weapons is given below.

```
             Market Prices of Armor and Weapons

                 Armor           |      Weapons
      ---------------------------+--------------------
      leather armor ....... 120  |
      studded leather armor 220  | dagger .......... 2
      ring mail ........... 225  | spear ........... 5
      scale mail .......... 330  | mace ............ 8
      chain mail .......... 475  | long sword ..... 15
      splint mail ......... 580  | short bow ...... 15
      banded mail ......... 590  | crossbow ....... 30
      plate mail .......... 750  | two-handed sword 75
```

Each increment (decrement) on a suit of armor raises (lowers) the price by 110 gold pieces. Each increment (decrement) on a weapon raises (lowers) its price by three times the basic price. No price can fall below zero.

Rations of food (including fruits) sell for 2 gold pieces each. (In 3.4 a slip in the code makes a ration worth 10, an awful one 17, and a fruit 77.)

## Glossary

- **Agate**: a stripey or cloudy kind of chalcedony.
- **Alexandrite**: a stone that looks green in sunlight and red in dungeon light.
- **Amethyst**: a kind of purple quartz.
- **Aquator**: a monster that attacks by squirting a jet of water.
- **Balsa**: a very light tropical wood.
- **Beryllium**: a light, brittle metal.
- **Black unicorn**: an evil, solitary, one-horned magic horse. (PC: replaced by the *ur-vile*.)
- **Carnelian**: a red variety of chalcedony.
- **Centaur**: a monster with the head and trunk of a man and the body of a horse. It carries a club.
- **Cinnabar**: red mercuric sulfide. Not the best material for a staff.
- **Crimson**: deep purplish red.
- **Cyan**: bright greenish blue.
- **Diamond**: crystallized carbon, clear and harder than anything else.
- **Dogwood**: a hard, tough wood resembling boxwood.
- **Dragon**: a huge, red, winged, fire-breathing reptile.
- **Electrum**: an alloy of silver and gold.
- **Emerald**: a bright green beryl.
- **Emu**: a large flightless bird.
- **Fall**: a Shakespearean staff. Hopefully this will be dropped from future versions of **rogue**.
- **Floating eye**: a transparent, one-eyed sea creature.
- **Garnet**: a deep red, glassy stone.
- **Germanium**: a brittle greyish metal.
- **Gnome**: an ugly, misshapen dwarf that lives underground.
- **Granite**: a hard, grey, igneous rock.
- **Griffin**: a fierce monster with the head and wings of an eagle and the body and claws of a lion.
- **Hobgoblin**: a large, hairy, nasty underground creature, usually armed and mailed.
- **Ice monster**: a humanoid monster that can radiate a freezing ice mist from one eye.
- **Invisible stalker**: an invisible airborne creature, single-minded and relentless.
- **Ironwood**: any of various very hard woods.
- **Jabberwock**: a fierce monster. Little is known about it except that it possesses “jaws that bite” (2d12) and “claws that scratch”
- (2d4).
- **Jackal**: a cowardly, yellow wild dog of Asia and North Africa.
- **Jade**: a hard, green, opaque stone.
- **Kestrel**: a large seabird.
- **Kobold**: a small, vicious underground creature that walks erect and carries a sword.
- **Kryptonite**: a green meteoric stone from the planet Krypton.
- **Kukui**: a large tropical tree.
- **Lapis lazuli**: an azure-blue opaque stone.
- **Leprechaun**: a clever fairy in the form of a little man with a pot of gold.
- **Manzanita**: a desert shrub.
- **Medusa**: a snake-haired, horrible woman whose gaze can turn creatures to stone.
- **Mimic**: an underground carnivore that can imitate objects.
- **Moonstone**: a kind of milky white quartz.
- **Nymph**: a nature spirit in the form of a beautiful maiden.
- **Obsidian**: a dark, glassy volcanic rock.
- **Onyx**: a kind of agate with layers of color.
- **Opal**: a milky form of silica that can refract light into colors.
- **Orc**: an ugly, stupid biped, ill-tempered and foul-smelling.
- **Pearl**: a round tumor from the inside of a shellfish.
- **Peridot**: a deep yellow-green stone.
- **Pewter**: an alloy of tin and lead.
- **Purple worm**: a giant burrowing animal with a circular mouth full of sharp teeth.
- **Quagga**: probably a misprint for *quaggoth*, a big, shaggy, ferocious humanoid creature. Real *quaggas* are striped donkey-like animals, now extinct.
- **Quasit**: a small, sneaky, demonlike creature.
- **Rattlesnake**: a poisonous snake with a rattle in its tail.
- **Ruby**: a deep red form of corundum.
- **Rust monster**: a grotesque, long-tailed quadruped that feeds on metal.
- **Sapphire**: a deep blue form of corundum.
- **Shuriken**: a small, jagged-edged disk, thrown as a weapon.
- **Silicon**: a hard grey substance extracted from rocks.
- **Taaffeite**: a rare mauve-colored stone.
- **Tiger's eye**: a yellowish-brown stone whose colors seem to play.
- **Topaz**: a yellowish crystalline stone; also, a dark yellow color.
- **Troll**: a large, greenish personage, fearless and very strong, with an appetite for human flesh.
- **Tungsten**: a heavy, greyish-white metal.
- **Turquoise**: an opaque, unstable blue-green stone; also, a light bluish-green color.
- **Umber Hulk**: a large, dark-colored monster with huge claws and four eyes.
- **Ur-vile**: a black, eyeless creature of evil lore, borrowed from Stephen Donaldson's Thomas Covenant novels. PC only.
- **Vampire**: a nocturnal ghoul that sucks blood from its victims.
- **Venus' Fly-Trap**: a large green plant that behaves like Violet Fungi (see below).
- **Vermilion**: deep yellowish red.
- **Violet Fungi**: a large fungus whose tendrils seize living creatures and rot their flesh.
- **Wraith**: a malevolent spirit that drains the life from its opponents.
- **Xeroc**: see *mimic*.
- **Xorn**: a three-armed, three-legged monster that can rearrange its molecules.
- **Yeti**: a large, white, shaggy creature that walks erect and dwells in the mountains of Tibet.
- **Zebrawood**: a hard tropical wood with stripes.
- **Zircon**: a clear reddish stone.
- **Zombie**: a walking corpse.

## Acknowledgements

Helpful comments and criticism were offered by J. T. Nutter, T. R. Pellitieri, and E. A. Flinn.

## Appendix: messages in Rogue

What some of the game's messages mean, with the object or trap that causes them.

- A cloak of darkness falls around you. (! Blindness)
- A gush of water hits you on the head. (^ Rust. V5 only.)
- A small dart just hit you in the shoulder. (^ Poison Dart)
- A small dart whizzes by your ear and vanishes. (^ Poison Dart)
- A sting momentarily weakens you. (= Sustain Strength. V5 and PC: “A bite momentarily weakens you.”)
- A strange white mist envelops you and you fall asleep. (^ Sleeping Gas)
- An arrow shoots past you. (^ Arrow)
- Bummer, this food tastes awful. (: Ration of Food. Only while hallucinating, and only if it tastes awful.)
- Hey, this tastes great. It makes you feel warm all over. (! Restore Strength)
- My, that was a yummy ... (: Slime-Mold. 3.4 says “Yum, that tasted good.”)
- Nothing happens. (/ Any. Only if its charges are exhausted.)
- Oh, bummer! Everything is dark! Help! (! Blindness. Only while hallucinating.)
- Oh no! An arrow shot you. (^ Arrow)
- Oh, now this scroll has a map on it. (? Magic Mapping)
- Oh, wow! Everything seems so cosmic! (! Hallucination)
- Oh, wow, that tasted good. (: Ration of Food. Only while hallucinating.)
- Oh, wow! You're floating in the air! (! Levitation. Only while hallucinating.)
- The ... appears confused (? Monster Confusion. Only after you hit a monster.)
- The monster freezes. (? Hold Monster. V5 only.)
- The bolt bounces. (/ Lightning)
- The bolt whizzes by you (/ Lightning. Only if it bounces off a wall or monster.)
- The corridor glows and then fades. (/ Light. Only if you are standing in a passage.)
- The flame bounces (/ Fire. Only if it bounces off a wall or monster.)
- The flame whizzes by you (/ Fire. Only if it bounces and misses you.)
- The ice bounces (/ Cold. Only if it bounces off a wall or monster.)
- The ice whizzes by you (/ Cold. Only if it bounces and misses you.)
- The missile vanishes with a puff of smoke. (/ Magic Missile. Only if it misses or the monster counters your magic.)
- The monsters around you freeze. (? Hold Monster. V5 only.)
- The room is lit by a shimmering blue light. (/ Light)
- The rust vanishes instantly. (= Maintain Armor; ? Protect Armor.)
- The scroll turns to dust as you pick it up. (? Scare Monster. Only if you previously dropped it. 3.4: “...as it hits the ground,” when you drop it a second time.)
- The veil of darkness lifts. (! Blindness. Only when the potion wears off or you drink ! Healing, ! Extra Healing, or ! See Invisible.)
- This potion tastes extremely dull (! Thirst Quenching)
- This potion tastes like ... juice. (! See Invisible)
- This scroll is an identify scroll. (? Identify. Not in V5.)
- This scroll seems to be blank. (? Blank Paper)
- Wait, what's going on here. Huh? What? Who? (! Confusion)
- What a trippy feeling! (! Confusion. Only while hallucinating.)
- You are caught in a bear trap. (^ Bear Trap)
- You are hit by the bolt. (/ Lightning. Only when the bolt bounces off a wall.)
- You are too weak to use it. (/ Drain Life. Only when you are down to 1 hit point.)
- You begin to feel better (! Healing)
- You begin to feel greedy and you sense gold. (? Gold Detection. Not in PC.)
- You begin to feel much better. (! Extra Healing)
- You can move again. (! Paralysis or ^ Sleeping Gas. Only when the effect wears off.)
- You can't move. (! Paralysis)
- You feel a pull downward. (? Gold Detection. Only when there is no gold on the current level.)
- You feel a strange sense of loss. (? Enchant Weapon. Only if you are not wielding a weapon. In V5 also ? Protect Armor with no armor on, or ? Hold Monster with no monster nearby; 5.4 also ? Enchant Armor.)
- You feel a wrenching sensation in your gut. (, Amulet of Yendor)
- You feel as if somebody is watching over you. (? Remove Curse)
- You feel in touch with the Universal Oneness. (? Remove Curse. Only while hallucinating.)
- You feel momentarily sick. (! Poison. Only if you are wearing = Sustain strength.)
- You feel stronger, now. What bulging muscles! (! Gain Strength)
- You feel very sick now. (! Poison)
- You feel yourself moving much faster. (! Haste Self)
- You feel yourself slowing down (! Haste Self. Only when the potion wears off.)
- You fell into a trap! (^ Trap Door)
- You have a strange feeling for a moment, then it passes. (! Magic Detection or Monster Detection. Only when there is nothing to detect.)
- You have a tingling feeling. (/ Drain Life. Only when no monsters are in the room.)
- You have been granted the boon of genocide. (? Genocide. Not in PC.)
- You hear a faint cry of anguish in the distance. (? Create Monster. Only when you are already surrounded.)
- You hear a high-pitched humming noise. (? Aggravate Monsters)
- You hear maniacal laughter in the distance. (? Scare Monster; PC also ? Vorpalize Weapon if you are not wielding a weapon.)
- You sense the presence of magic on this level. (! Magic Detection)
- You start to float in the air. (! Levitation)
- You suddenly feel much more skillful. (! Raise Level)
- Your ... glows blue for a moment. (? Enchant Weapon)
- Your armor glows faintly for a moment. (? Enchant Armor. Not in V5.)
- Your armor glows silver for a moment. (? Enchant Armor. V5 only.)
- Your armor is covered by a shimmering gold shield. (? Protect Armor)
- Your hands begin to glow red (? Monster Confusion)
- Your hands stop glowing red (? Monster Confusion. Only after you hit a monster.)
- Your nose tingles and you smell food. (? Food Detection)
- Yuk, this food tastes awful (: Ration of Food. Only if it tastes awful.)
- Yum, that tasted good. (: Ration of Food)

George Sicherman's own copy of the Vade-Mecum is at [sicherman.net](https://www.sicherman.net/rvm.html).

Copyright © 1999 George Sicherman.
