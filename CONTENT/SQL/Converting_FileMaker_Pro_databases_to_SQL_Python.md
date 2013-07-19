## Converting FileMaker Pro databases to SQL/Python

[This is a record of work in progress, not yet complete.]

### Starting point and goals

1. **Starting point**. Initially, I had three mostly flat FileMaker ("FMP") tables, each of which had a great many fields per record.

1. **End goal**. My end goal was to move permanently to SQL, with Python functions to manipulate all the data. Later I would add a web-based front-end. 

1. **Important secondary goal**. I wanted to be able to keep track of all history — all altered or deleted content — without needing to deal with versioning software or having history overburden normal use of the db.

1. **Continuity**. Although FMP supports SQL queries, I continued using my old, native workflow whenever I interacted with FMP. I needed to be able to continuing using the FMP database up to the very moment that I stopped using FMP and switched to the SQL implementation.

### Procedure

1. Dumping FMP data to several tab-delimited files.

1. Creation of new SQL schemata for SQLite3 database.

1. Creation of Python scripts to populate the SQLite3 db. Progressive testing of same.

1. 

### New schema

1. The FMP table of expressions in Chinese script was out
