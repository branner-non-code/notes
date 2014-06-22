## SQLite3, either-or NOT NULL for multiple fields

Use 

    CREATE TABLE the_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
        field1 TEXT UNIQUE,
        field2 TEXT UNIQUE,
        CHECK (field1 IS NOT NULL OR field2 IS NOT NULL)
    );

[end]
