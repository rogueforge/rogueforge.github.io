---
short: Rogue 4.22
year: 1982
machine: VAX
status: rebuilt
summary: A Rogue that survived only as a binary, in 4.1aBSD, now with source that compiles back into it.
released: Version string dated 9 February 1982; binary 13 March 1982
origin: 4.1aBSD, /games/rogue (CSRG Archive, Disc 1)
toolchain: 4.1BSD VAX C compiler with 4.1cBSD library variants
verified: Byte-identical
repo: rogue4.22-19820313-bsd41
---
# Rogue 4.22

Rogue 4.22 sits between the 3.x line and the 5.x redesign. It was never
widely distributed, and no source for it was known. What survived is the
96,356-byte VAX binary in the 4.1a release of BSD, dated 13 March 1982.

## The 2026 rebuild

The source was rebuilt from the binary until it matched byte for byte.
The binary keeps its symbols, so every function and variable came with a
name; the work was in recovering what each one said.

Some details only an exact rebuild would find. The strings were pulled
out of the source in alphabetical order of file name, with a second pass
for `save.c`, and the rebuild has to do the same to put each one at the
right address. The site's machine-dependent file has a test,
`>= '0' || c <= '5'`, that is always true, and a list of 62 system error
messages.

## Repository

<https://github.com/rogueforge/rogue4.22-19820313-bsd41>
