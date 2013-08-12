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

### In SQL

Is there a solution? A join, perhaps?

[end]
