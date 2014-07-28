## Dictionary keys and values

### Traditional dictionary

~~~
d = {'a' : 1, 'b' : 2, 'c' : 3}
tuple(d.keys()) # generate tuple of keys
tuple(d.values()) # generate tuple of values
~~~

### Ordered dictionary: `OrderedDict`

The `OrderedDict` is a special subclass of the Python dictionary, retaining the order in which key-value pairs were added. To retrieve a tuple of all keys or all values from either data structure use:

~~~
from collections import OrderedDict
d = OrderedDict((('a', 1), ('b', 2), ('c', 3)))
tuple(d.keys()) # generate tuple of keys
tuple(d.values()) # generate tuple of values
~~~

[end]
