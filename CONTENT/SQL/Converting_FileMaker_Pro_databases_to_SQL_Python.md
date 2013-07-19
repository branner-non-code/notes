## Converting FileMaker Pro databases to SQL/Python

[This is a record of work in progress, not yet complete.]

### Starting point and goals

1. **Starting point**. Initially, I had three mostly flat FileMaker ("FMP") tables, each of which had a great many fields per record.

1. **End goal**. My end goal was to move permanently to SQL, with Python functions to manipulate all the data. Later I would add a web-based front-end. 

1. **Important secondary goal**. I wanted to be able to keep track of all history — all altered or deleted content — without needing to deal with versioning software or having history overburden normal use of the db.

1. **Continuity**. Although FMP supports SQL queries, I continued using my old, native workflow whenever I interacted with FMP. I needed to be able to continuing using the FMP database up to the very moment that I stopped using FMP and switched to the SQL implementation.

### Procedure

1. Everything was done using scripts, so that all steps would be reproducible and could be incrementally improved.

1. Dumping FMP data to several tab-delimited files.

1. New SQL schemata for SQL database. 
 * SQLite3 is being initially used; PostgreSQL may be used later.
 * Join tables are used to connect different types of content, rather than tagging proper.

1. Python scripts to populate the SQL db. Progressive manual testing of same in Ipython; no unit testing done but exceptions are implemented for expected edge cases. Initially, the Python SQLite3 module is being used but I may turn to SQLAlchemy later. 

1. Python functions to use the SQL database.

###  FMP script to export the three tables
 1. character data (expressions in Chinese script) — one dump file:
  * **characters**: corresponding traditional and simplified forms
  * **sources**: records about which major dictionaries contain which expressions
 1. category data (categories to which definitions may be assigned) — one dump file:
  * individual categories themselves
  * various cross-references among categories
  * text description of the meaning of certain categories
 1. definition data — four dump files:
  * **gloss**: definitions with part-of-speech ("POS") tags, fields for syntax notes, measure words (for nouns), notes on coverbs and direct-object behavior in the case of verbal expressions, and important collocations;
  * **literal**: literal meaning and information about the origin of the expression;
  * **Pīnyīn**: whole Pīnyīn 拼音 renderings of whole expressions, with up to two variants per expression;
  * **entry**: for each record, one field from each of "gloss", "literal", and "Pīnyīn", above, for constructing join tables; also, boolean metadata indicating whether a given entry or field was expected to appear in the first printing of the book.

### New schema for main database

In all, eleven (11) tables:

1. character data => 3 tables: 
 * `kanji`
 * `kanji_sources`
 * `kanji_and_source_xref` (the last is a join table to link `kanji` and `kanji_sources`);
2. category data => 2 tables: 
 * `category`
 * `xref_categories` (join table for `category`)
3. definition data => 4 tables:
 1. gloss => 1 table `gloss`
 2. literal => 1 table `literal`
 3. Pīnyīn => 2 tables:
  * `pinyin`
  * `xref_pinyin_variants` (join table for `pinyin`)
4. entry => 2 tables:
  * `entry` (join table for `kanji`, `pinyin`, `gloss`, `literal`; `kanji_sources` is normally excluded)
  * `xref_entry_to_categories` (join table for `entry`, `category`)

Every table also has a unique integer primary key and a `time_of_commit` field, important for the backup database.

Some join tables also have a "precedence" field (e.g., `xref_categories.categ_to_categ_precedence`, `xref_entry_to_categories.entry_to_categ_precedence`, `xref_pinyin_variants.py2_label_precedence`), in order to rank the multiple possible outcomes of joins.

[end]
