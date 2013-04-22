Regex inverse matching
======================

Task
----

find all lines lacking some "item" 

Strategy
--------
Line of whole characters, each of which is not followed by "item"

Code
----
 1. find line of zero or more whole characters.

~~~
 ^.*$
~~~

 1. now add negative lookahead to each `.`

~~~
^((?!item).)*$
~~~

Consulted
---------
http://stackoverflow.com/a/406408, accessed 20120426.
