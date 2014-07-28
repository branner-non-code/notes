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

[end]
