---
short: Advanced Rogue 5.8s
year: 1989
machine: Unix
status: planned
summary: Advanced Rogue 5.8 with special rooms, shops and new items added by an unknown hand by 1989.
origin: Two copies, from Carnegie Mellon (1989–90) and from 1993
verified: Restored 2007 (5.8s.1); not yet rebuilt from a binary
---
# Advanced Rogue 5.8s

A variant of [Advanced Rogue 5.8](advanced-rogue-5-8.md) that somebody
other than its Bell Labs authors made by 1989. It keeps 5.8's version
string, "5.8 (Bell Labs) 1/03/85", so only its contents tell it apart. The
"s" was added in 2007 and stands for its special rooms.

## What it adds

Most of the additions will be familiar to anyone who played Hack:

- **Special rooms.** A level may have a shop or a throne room. 5.8's
  treasure rooms take on the character of the monsters guarding them: a
  nest of giant rats, an ant hill, a beehive of killer bees, a morgue of
  ghouls, a tomb of mummies, or a den of orcs, hobgoblins, trolls or
  vampires. The shops come with shopkeepers, and their names are Hack's
  own: "Skibbereen" keeps a bookshop, "Zum Loch" a liquor store.
- **Weapons and armor**, among them a boomerang, a crysknife, a worm
  tooth, a flail, a pick-axe, a shield, a helmet and gloves.
- **Potions, scrolls, wands and rings**, among them booze and fruit juice,
  scrolls of amnesia, fire and punishment (with its heavy iron ball), wands
  of death, sleep and make invisible, and rings of levitation and of
  protection from stoning.
- A different mix of monsters, and new ways to die, such as choking on food.

None of it carried over into [Advanced Rogue 7.7](advanced-rogue-7-7.md)
or [XRogue](xrogue-8-0.md), and nobody has been found to claim it.

## The surviving copies

Two copies survive, and they are nearly the same:

- **Carnegie Mellon, 1989–90.** In July 1989 Jacques Parker, a student on
  CMU's Andrew system, asked rec.games.rogue whether there were public
  versions of "Arogue, Srogue, and/or Urogue". By late August he had this
  one. His copy's files date from 24 August 1989 to 28 April 1990. His
  README says he added `overlay.c` to work around his system's
  `overlay()`, and marked his other changes "xxx" or "jp27", his user
  name. He also wrote an `ARogue.help` and kept the files he changed as
  `.org`.
- **1993.** A copy with files dated 7 May 1993, without Parker's changes.
  RogueBasin says it was found at M.I.T.

## Restoration source material

The project's 2007 restoration started from these copies and was released
as a beta on 2 August 2007, then as 5.8s.1. It added the same portable
save and machine layer as [Advanced Rogue 5.8.2](advanced-rogue-5-8.md).

## Repository

Not yet on GitHub.
