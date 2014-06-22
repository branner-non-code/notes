SQLite examples for use in REPL
-------------------------------

1.  What is the schema?

        sqlite3 hl.db
        SELECT * FROM sqlite_master WHERE type='table';

2.  Open SQLite with a database:

        sqlite3 hl.db
        .quit

3.  From 20130226: Report the schema?

        sqlite3 hl.db
        SELECT * FROM sqlite_master WHERE type='table';

4.  From 20130226: Inserting a headline, basic command

        INSERT INTO headlines (headline, url, source, date, lookupdate) VALUES (the_headline, the_url, the_source, the_date, todaydatetime);

5.  20130227: Find the \<symbol\> id using

        SELECT id FROM shares WHERE ticker='<symbol>';

6.  20130227: Working commands to create `shares` table:

        DROP TABLE IF EXISTS shares;
        CREATE TABLE shares(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ticker VARCHAR(5) NOT NULL, 
            owned INTEGER, 
            UNIQUE (ticker));

    Notes:

    1.  `UNIQUE` comes at end and raises an error if an attempt is made
        to add a duplicate value to the field in question. Tested and
        works.

    2.  `PRIMARY KEY AUTOINCREMENT` — not sure what happens in
        `AUTOINCREMENT` is omitted.

7.  20130227: Successful insert and show that you have the id:

        INSERT INTO shares (ticker) VALUES ('VZ');
        SELECT id FROM shares WHERE ticker='VZ';

8.  20130227: Loading data via script? Saved script and then ran as
    follows from command line:

        sqlite3 hl.db < insert_all_tickers.script

    Note: fund listings are apparently not included in my data source.



[end]
