## Shortcut to deep copy of a Python list

[Edited 20140220]

~~~
In [1]: x = [1, 2, 3]

In [2]: y = x

In [3]: x.append(4)

In [4]: y
Out[4]: [1, 2, 3, 4]

In [5]: x = [1, 2, 3]

In [6]: y = x[:]

In [7]: x.append(4)

In [8]: y
Out[8]: [1, 2, 3]
~~~

[end]