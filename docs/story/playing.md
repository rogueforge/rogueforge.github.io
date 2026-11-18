---
glyph: glyph-star
summary: The rebuilt sources are exact copies of 1980s programs. To play them on a modern machine they need porting, and the ports turned up bugs of their own.
---
# Playing them today

A byte-identical rebuild is a historical document: it compiles only with
the 1980s toolchain and runs only on a PDP-11 or VAX, real or simulated.
To play it on a modern computer it has to be ported. The ports start
from the rebuilt source, so each change from the original is a separate,
named commit that can be read on its own.

## The ports

Each port is a series of small commits on top of the rebuilt source,
grouped by what they fix:

- **c89** and **gcc4**: changes modern C compilers require, such as
  declaring functions before use and not writing to string constants.
- **posix** and **ncurses**: replacing system calls and terminal
  handling that no longer exist.
- **lp64**: giving pointers and integers their real sizes on 64-bit
  machines.
- **save**: making saved games work, where the original saved an image
  of the program's memory.

## The bugs

Then come the bug fixes, between 63 and 104 for each version. A modern
system, an address sanitizer and a lot of automated play expose problems
that a 1981 VAX never showed:

- reading and writing past the end of arrays, and off the edge of the
  map;
- using objects after they have been freed, such as a thrown weapon or
  an item a nymph has stolen;
- score files that could be corrupted, read by the wrong user, or
  locked forever;
- saved games that could be edited or restored by someone else;
- the year on the tombstone after 1999.

Each fix is a separate commit marked `BUGFIX`, with the original
behaviour preserved wherever it was a design decision, not a mistake.
Fixes from earlier restorations are carried forward and credited to
their authors.

## Building

The Linux ports build with gcc or clang using a single `Makefile.linux`
that explains every flag it uses and why the 1981 code needs it. They
will be published as branches of each version's repository on
[GitHub](https://github.com/rogueforge). Until then, the earlier
restorations of several versions can still be downloaded from the
[legacy site](http://rogue.rogueforge.net/).
