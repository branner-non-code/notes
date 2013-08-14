## SQL Null issues

### Null vs. empty string

Useful Stack discussion.

http://programmers.stackexchange.com/questions/32578/sql-empty-string-vs-null-value

### SQLite behavior

> The goal is to make SQLite handle NULLs in a standards-compliant way. But the descriptions in the SQL standards on how to handle NULLs seem ambiguous. It is not clear from the standards documents exactly how NULLs should be handled in all circumstances. 

http://www.sqlite.org/nulls.html

### C. J. Date's opposition

See discussion at http://www09.sigmod.org/sigmod/record/issues/0809/p23.grant.pdf

### Another overview:

> While Null indicates the absence of any value, the empty string and numerical zero both represent actual values.

https://en.wikipedia.org/wiki/Null_%28SQL%29#Controversy

### SQLite3 `NULL` == Python `None`

See http://docs.python.org/3.2/library/sqlite3.html?highlight=sqlite3#introduction.

[end]
