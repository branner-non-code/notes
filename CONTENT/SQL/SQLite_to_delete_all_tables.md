## SQLite to delete all tables

~~~
sqlite> PRAGMA writable_schema = 1;
sqlite> delete from sqlite_master where type = 'table';
sqlite> PRAGMA writable_schema = 0;
sqlite> PRAGMA INTEGRITY_CHECK;
ok
~~~

[end]
