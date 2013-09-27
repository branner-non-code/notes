## Python SQLite3, Notes about `cursor.lastrowid`

 1. Holds the value of the record-ID of the last successful `INSERT` statement.
 1. Its type is either `int` or `NoneType` — not a function.
 2. Does not "reset" after being used once, unlike `cursor.fetchall()`.
 3. Does not reset if `INSERT` fails; retains prior value; this may be a source of error.
 3. Is set to `None` if any SQL other than `INSERT` is used.
