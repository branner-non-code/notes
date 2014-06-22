## MergeSort in Python

Python’s built-in sort function uses TimSort, a variety of MergeSort with preliminary optimizations to save time by identifying partially ordered subarrays. Part of the optimization process involves the much slower InsertionSort.

If no such subarrays are likely to be present, however, plain, unoptimized MergeSort may be faster. And it is available to Python through the NumPy library. Below is an example in which NumPy MergeSort is a third faster than the default Python sort function:

~~~
$ python -m timeit -s "
import numpy;\
from random import choice, seed;\
from string import ascii_uppercase;\
seed(137);\
gibberish = [choice(ascii_uppercase) for i in range(1000000)];\
gibberish_np = numpy.array(gibberish)" "\
gibberish_np = numpy.sort(gibberish_np, kind='mergesort')"
10 loops, best of 3: 29.7 msec per loop
$
$ python -m timeit -s "
from random import choice, seed;\
from string import ascii_uppercase;\
seed(137);\
gibberish = [choice(ascii_uppercase) for i in range(1000000)]" "\
gibberish.sort()"
10 loops, best of 3: 39.9 msec per loop
$
~~~

Numpy also supplies QuickSort and HeapSort, which are slower than MergeSort but which sort lists without additional space complexity, as does TimSort. See the [NumPy docs](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sort.html) for more information. 

[end]
