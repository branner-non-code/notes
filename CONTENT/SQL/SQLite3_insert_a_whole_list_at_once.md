## SQLite3, insert a whole list at once

Given a table

    CREATE TABLE kanji_all (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tzyh TEXT UNIQUE,
        timestamp_id DATETIME NOT NULL,
        FOREIGN KEY (timestamp_id) references timerecords(id)
    );

it is slightly faster (savings of 19% with 70K rows) to insert it all at once with `executemany()`, even having to populate a special list first:

    content = [(id, i, timestamp_id) for id, i in enumerate(content)]
    cursor.executemany('INSERT INTO kanji_all VALUES (?,?,?)', content)

rather than use a loop that executes many discrete `INSERT` statements:

    for tzyh in content:
        cursor.execute('INSERT INTO kanji_all (tzyh,timestamp_id) VALUES (?,?)', (tzyh, timestamp_id))

[end]
