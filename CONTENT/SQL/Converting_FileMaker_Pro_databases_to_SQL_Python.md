## Converting FileMaker Pro databases to SQL/Python

[This is a record of work in progress, not yet complete.]

### Starting point and goals

1. **Starting point**. Initially, I had three mostly flat FileMaker ("FMP") tables, each of which had a great many fields per record. In all, there are perhaps 1.7 million discrete fields, though there is much repeated content among them. I have been curating them manually since about 2004.

1. **End goal**. My end goal was to move permanently to SQL, with Python functions to manipulate all the data. Later I would add a web-based front-end. 

1. **Important secondary goal**. I wanted to be able to keep track of all history — all altered or deleted content — without needing to deal with versioning software or having history overburden normal use of the db.

1. **Continuity**. Although FMP supports SQL queries, I continued using my old, native workflow whenever I interacted with FMP. I needed to be able to continuing using the FMP database up to the very moment that I stopped using FMP and switched to the SQL implementation.

### Procedure

1. Everything was done using scripts, so that all steps would be reproducible and could be incrementally improved.

1. Dumping FMP data to several tab-delimited files.

1. New SQL schemata for SQL database. 
 * SQLite3 is being initially used; PostgreSQL may be used later.
 * Join tables are used to connect different types of content, rather than tagging proper.

1. Python scripts to populate the SQL db. Progressive manual testing of these in Ipython, as well as manual correction of the data; no unit testing done but exceptions are implemented for expected edge cases. Initially, the Python SQLite3 module is being used but I may turn to SQLAlchemy later. 

1. Python functions to use the SQL database.

###  FMP script to export the three tables (This needs to be updated; 20130809.)
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

### Schemata

#### New schema for main database

In all, sixteen (16) tables (20130729): (This needs to be updated; 20130809.)

1. character data => 4 tables: 
 * `kanji`
 * `xref_kanji_trad_simp` (joins simplified and traditional forms, when they differ)
 * `kanji_sources`
 * `kanji_and_source_xref` (the last is a join table to link `kanji` and `kanji_sources`);
2. category data => 3 tables: 
 * `category`
 * `xref_categories_close` (join table for `category`; note that this and `xref_categories_antonyms` allow for the cross-reference of categories, while `xref_entry_to_categories` and `xref_entry_to_antonyms` link individual entries to categories)
 * `xref_categories_antonyms` (second join table for `category`)
3. definition data => 6 tables:
 1. gloss => 1 table `gloss`
 2. literal => 3 tables 
  * `literal`
  * `origin`
  * `xref_literal_origin` (join table to connect `literal` and `origin`)
 3. Pīnyīn => 2 tables:
  * `pinyin`
  * `xref_pinyin_variants` (join table for `pinyin`)
4. entry => 3 tables:
  * `entry` (join table for `kanji`, `pinyin`, `gloss`, `literal`; `kanji_sources` is normally excluded)
  * `xref_entry_to_categories` (join table for `entry`, `category`; note that this and `xref_entry_to_antonyms` link individual entries to categories, while `xref_categories_close` and `xref_categories_antonyms` allow for the cross-reference of categories)
  * `xref_entry_to_antonyms` (second join table for `entry`, `category`)
  
We should have a separate set of tables controlling English lemmata, distinct from the categories. The categories, then, would be reduced in number. (20130729)

Every table also has a unique integer primary key and a `time_of_commit` field, important for the backup database.

Some join tables also have a "precedence" field (e.g., `xref_categories.categ_to_categ_precedence`, `xref_entry_to_categories.entry_to_categ_precedence`, `xref_pinyin_variants.py2_label_precedence`), in order to rank the multiple possible outcomes of joins.

Any table, even one with only a single significant (non-date) field, cannot retain `UNIQUE` in the backup db, since changes to it can lead to multiple copies of it in the backup.

Initially, the SQL database had a table of traditional-simplified character expression pairs, as did the corresponding FMP table. By giving the corresponding table in the new database just a single character expression field and adding a join table to link traditional to simplified, I've reduced the number of total fields by about 12%, with an increase in running-time of about 30% for the import script. (20130727)

#### Script for constructing the main database.

1. During initial work and testing, the `CREATE` codeblock for each table is preceded by a `DROP TABLE IF EXISTS` expression for the same table, so that the script can be run repeatedly without risk of corruption.
2. Once all the problems seemed to have been fixed, I altered `main()` so as to allow only new content to be added:

        def main(anything=''):                                     
            con = sqlite3.connect('malediction.db')                
            with con:                                              
                cursor = con.cursor()                              
                # If there was any argument to main(), reinitialize the tables in
                # question here; otherwise, merely supplement them.                                                                                                         
                if anything:                                       
                    query = open('malediction_sql_database.sql', 'r').read()           
                    cursor.executescript(query)                    

2. The script ends with the line 
        SELECT * FROM sqlite_master WHERE type='table';

   so that if it is run from the SQLite3 prompt its success or failure can be determined by eye.
3. The SQL script is normally being called from within the Python script that populates the db from the FMP dump files, using:

        con = sqlite3.connect('database.db')
        with con:
            curs = con.cursor()
            query = open('script.sql', 'r').read()
            curs.executescript(query)

   so that the Python script can be run repeatedly without having to deal with a second REPL.

#### Schema for backup database

The script that populates the backup database is the same as the one for the main database, with these two important exceptions:

1. Each table has a `main_db_id` that corresponds to the `id` field (the primary key) of the corresponding table in the main database; it would not do to use the same `id` value as a primary key in the backup db, since there might be multiple backed-up records with the same `id` value in the main database.
2. Each table has a `deleted_from_main` boolean field, to indicate whether the corresponding record in the main db was actually deleted or not. Changes other than outright deletion of a record can be ascertained by running a `diff` function on any two corresponding records.

#### Changes made to Malediction project as of 20130809

 1. Wrote UML diagram in OmniGraffle; led to finding a number of inefficiencies and errors. 
 2. Divided importing script into two parts: one for "reference" tables, such as those to pair simplified and traditional character-expressions, and another for the population of the contents of the actual dictionary, including various parts of the entry and the categories and Pīnyīn readings to which a given entry may need to be joined. Running the latter script alone now takes about 26 seconds; running the whole set of functions used to take around three minutes.
 3. Renamed some functions for clarity.
 4. Moved some function calls to a single place in `main()` rather than having them reappear several times, each in a different subfunction.
 5. Timestamps are now recorded in a table and the id of a given timestamp record is used in all other tables. That makes it possible to determine quickly whether any commits have been made to the database within a particular window.

[end]
