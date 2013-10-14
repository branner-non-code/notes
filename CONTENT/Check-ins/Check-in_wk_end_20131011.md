## Check-in week ending 20131011

### Prosody

### Study of _yán_ 焉

  1. Received deadline for final submission of this paper. Must reduce discussion of locative contraction and add treatment of interrogative.
    1. 20131010: proofreading and *-r content mostly done.
    1. 20131011: must get citation for Starosin 1989 pages.
    1. Must get interrogative research done, but perhaps most of this should go into a separate paper.
  2. Resumed examination of A/B contrast in _Goangyunn_ readings: 
    1. As of 20131011: Characters 拔卒取受喟歃渴溺祭坺楄扁葐坋菔匐棓菩撣㒔葃翵洹越繁蟠䄶儃襡韣圜湲沄䫟枸句怐溉汽
    1. 20131011: beginning correspondence tables for rimes and initials.
  3. 20131010: Proofreading complete of existing paper; must now add additional section on A/B contrast and track down Starostin material on *-r.


### Character dictionary



### Review of technical matter

  1. Substrings. Now two versions of program to find longest substring with a limited number of unique characters: one using only a list, and the other using a set to identify unique characters and a list to keep track of the order in which characters were added to the set. Some small refactoring may still be necessary in the latter, but it seems that until input strings become very large, the latter program is slower than the former, despite the better lookup speed of sets.

### Mandarin dictionary

  1. 20131005. 43 items.

### Wényán 文言 markup system



### Other coding

  1. Began migration of blog from WordPress (dissatisfied that much functionality no longer works when Ghostery is enabled) to GitHub pages, with Pelican support. But `pelican-import` had a reproducible error, which I traced to the presence of a formfeed character ("FF", U+000C) in WordPress's export XML file. The formfeed was neither being stripped nor converted to something that printed on WordPress, and I reported this as a bug (http://core.trac.wordpress.org/ticket/25548). 
  2. I found that Pelican's import function was failing silently, and traced the problem to the use of `LXML`'s XML parser in `BeautifulSoup4`; replacing that with the HTML parser eliminated the problem. I submitted both an issue (https://github.com/getpelican/pelican/issues/1113) and a pull-request (https://github.com/getpelican/pelican/pull/1114), and it seems the latter has now been accepted.


### To Do

#### Prosody

  1. _Zàn_ matter.
  2. _Yùlǎn shī_ matter.
 
#### Other coding

  1. Blaggregator set-up.

#### Review of technical matter

  1. Refactor substring.py.
  1. Binary search tree.
  1. Heaps.

#### Mandarin dictionary

  1. Refactor command-line output.
  1. Refactor genertic SQL commands — some can be combined as joins.
  1. Adding characters for new entry not yet working.
  2. Adding an entry for characters not in the all-kanji table does not work.

[end]
