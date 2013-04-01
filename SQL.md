SQL
===

Resources
---------

1.  ​20130227. <www.w3schools.com/sql/> Includes interactive examples.

2.  ​20130221. Dom Roselli recommends:
    <http://www.dharma.com/downloads/SDK9.0_SQL.pdf> and he adds:

    > There is a SQL standard, but most implementations have proprietary
    > extensions to the language (many do the same types of things, but
    > with different syntax). So once you know what you’re going to
    > develop against, you can get dig into richer functionality of that
    > specific platform. However, this seems to be platform independent
    > and could be a good place to start.

3.  ​20130221. Resources for SQLite use with Python

    1.  Best Python-specific material seems to be
        <http://docs.python.org/2/library/sqlite3.html>.

    2.  <http://zetcode.com/db/sqlitepythontutorial/>

    3.  <http://greeennotebook.com/2010/06/how-to-use-sqlite3-from-python-introductory-tutorial/>

4.  ​20130221. SQL dialect reference:
    <http://en.wikibooks.org/wiki/SQL_dialects_reference>

5.  Resources for the SQLite command line:

    1.  Best quick set-up: 15 SQLite3 SQL Commands Explained with
        Examples
        <http://www.thegeekstuff.com/2012/09/sqlite-command-examples/>

    2.  Command Line Shell For SQLite
        <http://www.sqlite.org/sqlite.html>

SQLite3 command line
--------------------

​20130221. Example

    sqlite3 hl.db
    create table tickers(tkID integer, name varchar(6));
    create table hls(hlID integer, text varchar(120), link varchar(200), date text(10), source varchar(40));
    .quit

SQLite within Python
--------------------

1.  ​20130326. Even though connections are supposedly closed
    automatically, doing so explicitly with

        object.connection.commit()
        object.cursor.close()
        object.connection.close()

    is safer.

2.  ​20130221. Basic instructions used

        import sqlite3 as Q
        con = Q.connect('test.db')
        # use con = Q.connect(":memory:") to create the db in RAM!
        curs = con.cursor()
        con.close()

3.  ​20130221. Short program to find version number

        #!/usr/bin/python
        # -*- coding: utf-8 -*-

        import sqlite3 as lite
        import sys

        con = lite.connect('test.db')

        with con:
            
            cur = con.cursor()    
            cur.execute('SELECT SQLITE_VERSION()')
            
            data = cur.fetchone()
            
            print("SQLite version: {}".format(data[0]))

SQLite examples for REPL
------------------------

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

SQLite examples for Ipython
---------------------------

20130227.

    import sqlite3
    conn = sqlite3.connect('hl.db')
    c = conn.cursor()
    o = c.execute('''SELECT ticker,headline FROM headlines''')
    o.fetchall() # o is then populated with an index of tuples --- one tuple per record

`fetchall()`:

    In [28]: o = c.execute('''SELECT ticker,headline FROM headlines''')

    In [29]: o.fetchone()
    Out[29]: ('VZ', 'junk VZ headline')

    In [30]: o.fetchone()
    Out[30]: ('XOXO', 'junk XOXO headline')

    In [31]: o.fetchone()
    Out[31]: ('TLLP', 'junk TLLP headline')

​20130227. Other facts:

1.  Cannot reset cursor! From <>:

    > The SQLite interface in Python 3.1 is based on PEP 249, which only
    > specifies that cursors have to support sequential access to the
    > records of a query result. There’s no way to go back. If you need
    > to return to a previously fetched row, you should save it when you
    > first fetch it, e.g. create a list of the fetched data (or
    > actually, just use `fetchall`). Then you can work with the list
    > and go back and forth between rows as much as you want.
    >
    > The idea behind the design of the DB API is to support efficient
    > execution of code where you only need to process each row once.

    So one must make the database do as much selection as possible
    before beginning manipulation within Python.

2.  

Implementing with real headlines
--------------------------------

1.  ​20130227. Create the database and tables manually for now:

        sqlite3 hl.db
        DROP TABLE IF EXISTS prices;
        DROP TABLE IF EXISTS headlines;
        DROP TABLE IF EXISTS shares;
        CREATE TABLE shares(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ticker VARCHAR(5) NOT NULL, 
            owned INTEGER, 
            UNIQUE (ticker));
        CREATE TABLE headlines(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            idSharesFK INTEGER, 
            ticker VARCHAR(5) NOT NULL, 
            headline VARCHAR(255) NOT NULL, 
            url VARCHAR(255), 
            source VARCHAR(25), 
            date INTEGER, 
            lookupdate INTEGER, 
            lastrepdate INTEGER, 
            FOREIGN KEY(idSharesFK) REFERENCES shares(id));
        CREATE TABLE prices(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            idSharesFK INTEGER, 
            lookupdate INTEGER, 
            lastrepdate INTEGER, 
            chg_lastrep FLOAT, 
            pc_chg_lastrep FLOAT, 
            tradedate INTEGER, 
            lasttrade_value FLOAT, 
            div_per_shr FLOAT, 
            FOREIGN KEY(idSharesFK) REFERENCES shares(id));
        SELECT * FROM sqlite_master WHERE type='table';

    Note: this should go into a script for reproducibility before you
    push to repo.

2.  ​20130227. Use copy of `headline_length.py`, named
    `headline_play.py`. Add:

        import sqlite3 as SQ

3.  ​20130227. You should do the whole database section within a `with`
    block:

        with SQ.connect('hl.db') as connection: # ``Connection'' object represents the database.
                    # connect is the main method available within the module.
                cursor = connection.cursor() # A ``cursor'' instance is used for executing most SQL instructions.
                for symbol in contents:
                    headline_list = []
                    webpage = retrieve_webpage(symbol)
                    headline_list += process_webpage(webpage)
                    if headline_list:
                        cursor.execute('''INSERT INTO headlines (''' +\
                            '''ticker, headline, url, source) ''' +\
                            '''VALUES (?, ?, ?, ?);''', \
                            (symbol, i[0], i[1], i[2]))

    Now, on checking the database at the SQLite prompt, everything seems
    to have been added.

4.  ​20130227. In order to do this I omitted dates, which need a special
    conversion function. After that is written, both today’s date and
    `i[3]` must be converted to it. Then we can use:

                        cursor.execute('''INSERT INTO headlines (''' +\
                            '''ticker, headline, url, source, date, ''' +\
                            '''lookupdate) VALUES (?, ?, ?, ?, ?, ?);''', \
                            (symbol, i[0], i[1], i[2], i[3], today))

    However, this can wait until later.

    SQL will generate the same date I am using for Python with
    `SELECT date(’now’);`: 2013-02-27 etc. And dates in this format can
    be compared arithmetically!

    So we can use them in the db. All that remains is:

    1.  to convert Yahoo’s scraped date to this format

    2.  to add any code involving dates what is actually needed?

Other SQLite syntax and tricks
------------------------------

1.  ​20130227. Remember that `”’:memory:”’` can be used for a transient
    database in memory.

2.  ​20130227. To delete all a table’s contents, use
    `DELETE FROM headlines;`

[end]
