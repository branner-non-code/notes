Regex inverse matching
======================

 * task: find all lines lacking some "item" 
 * strategy: Line of whole characters, each of which is not followed by "item"
 * code:
  1. find line of zero or more whole characters 
~~~
^.*$
~~~
  1. now add negative lookahead to each `.`
~~~
^((?!item).)*$
~~~

 * consulted http://stackoverflow.com/a/406408, accessed 20120426.
