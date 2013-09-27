## Check-in week ending 20130920

### Review of technical matter

  1. Hash tables working: using chaining with lists — abandoned plan to chain with nested hash tables, because in order to avoid collisions at every level I would either need to use a different modulus on each level (could add one to previous level's modulus) or a different hash function. Too much bother. Optional resizing added. Test suite written, all working, posted to public repo.
  1. Did timings for hash table code, showing the great improvement in speed if resizing and amortization is used.
  2. Paired with Matthew Zadrozny and compared our `insertionsort` implementations. His is simpler but runs 50% slower, evidently because of extra operations related to the use of a `while` loop where I have two `for` loops. We explored the possibility that `while` is intrinsically slower than `for`, but that doesn't appear to be the case.
  3. Beginning study of substring searches — moved notes to `.py` file and `test_...` file.

### Mandarin dictionary

  1. Began work to refactor output to screen.

### Undergraduate student's thesis

  1. Found syntax error preventing compilation.
  2. Cleaned up repo.
  3. Added student's Proposal into the repo and added my own comments.
  4. Looked up standard rules on Git commit message style.

### IAS

  1. (Administrative and infrastructure tasks done. Second monitor and desk ordered.)

### To Do

#### Review of technical matter

  1. Substrings.
  1. Heaps.
  1. Binary search tree.

#### Mandarin dictionary

  1. Refactor command-line output.
  1. Refactor genertic SQL commands — some can be combined as joins.
  1. Adding characters for new entry not yet working.
  2. Adding an entry for characters not in the all-kanji table does not work.

[end]
