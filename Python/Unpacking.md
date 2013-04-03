Unpacking 
----------

`*a_list` unpacks the list into a tuple (which must be an
“assignment target”):

~~~
In [90]: a_list = [i for i in range(10)]

In [91]: print(*a_list)                 
0 1 2 3 4 5 6 7 8 9
~~~

Note: "can use starred expression only as assignment target", i.e., a function argument, unpacking a tuple, or calling a function.

See discussion at http://www.python.org/dev/peps/pep-3132/.

[end]
