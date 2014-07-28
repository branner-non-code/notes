## Create set with more than 255 syllables

The limit on the number of discrete arguments to a function is 255. This limit can be avoided by embedding arguments in a single data structure. 

For example, the expression 

~~~
set(1, 2, …, 256)
~~~

will raise

~~~
SyntaxError: more than 255 arguments
~~~

Circumvent it by placing all the arguments in a list:

~~~
set([1, 2, …, 256])
~~~

[end]
