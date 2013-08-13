## Python SQL, retrieving last-saved record ID

### In Python use `cursor.lastrowid`

This is faster than a second SQL `execute` statement by almost 50%:

~~~
$ python -m timeit -s "\
> import sqlite3;\
> connection=sqlite3.connect(':memory:');\
> cursor=connection.cursor();\
> cursor.execute('''CREATE TABLE foo (id integer primary key autoincrement ,\
>                                     username varchar(50),\
>                                     password varchar(50))''')" "\
> cursor.execute('INSERT INTO foo (username,password) VALUES (?,?)',\
>                ('test','test'));\
> found = cursor.execute('''SELECT id FROM foo \
>                                     WHERE username='test' \
>                                     AND password='test' ''')"
100000 loops, best of 3: 10.1 usec per loop
$
$ python -m timeit -s "\
> import sqlite3;\
> connection=sqlite3.connect(':memory:');\
> cursor=connection.cursor();\
> cursor.execute('''CREATE TABLE foo (id integer primary key autoincrement ,\
>                                     username varchar(50),\
>                                     password varchar(50))''')" "\
> cursor.execute('INSERT INTO foo (username,password) VALUES (?,?)',\
>                ('test','test'));\
> found = cursor.lastrowid"
100000 loops, best of 3: 5.74 usec per loop
$ 
~~~

#### Notes about `cursor.lastrowid`

 1. Its type is either `int` or `NoneType` — not a function.
 2. Does not "reset" after being used once, unlike `cursor.fetchall()`.
 3. Does not reset if `execute` fails; retains prior value.
 3. Is set to `None` if any SQL other than `INSERT` is used.

### In SQL

Is there a solution? A join, perhaps?

[end]
