## How to import functions on an object (as class methods rather than in flat procedural code)?

 1. If I have a number of programs sharing functions, I can store those functions in an independent module, say `utils`, and import them into each program, as a modular way of reusing code (Python 3.3):

        # utils1.py
        def compare_weight(obj1, obj2):
            return obj1 == obj2

        # persecute1.py
        import utils1
        witch, duck = 1, 2
        print(utils1.compare_weight(witch, duck))

 Output (Ipython 1.0.0):

        In [1]: run persecute1.py
        False

 1. And if I want to call those functions as class methods, such as:

        # utils2.py
        def compare_weight(self):
            return self.obj1 == self.obj2

        # persecute2.py
        import utils2
        class Cases(object):
            def __init__(self):
                self.obj1 = 1
                self.obj2 = 2

            def compare_weight(self):
                return self.obj1 == self.obj2

        witch, duck = 1, 2
        this_case = Cases()
        this_case.obj1 = witch
        this_case.obj2 = duck
        print(this_case.compare_weight())

 Output: 

        In [2]: run persecute2.py
        False

 So far so good. 

 1. But if I again store the class method in an external module, then how does it get called?

 Answer: As an argument to the method. The object still has to be passed, but since the method is passed on the imported module `utils`, the object is now passed as an argument.

        # persecute3.py
        import utils2
        class Cases(object):
            def __init__(self):
                self.obj1 = 1
                self.obj2 = 2

        witch, duck = 1, 2
        this_case = Cases()
        this_case.obj1 = witch
        this_case.obj2 = duck
        print(utils2.compare_weight(this_case))

 Output:

        In [3]: run persecute3.py
        False

### Timing with `timeit`

`Timeit` shows only a small speed hit.

First, saved `utils2.py`:

~~~
def compare_weight(self):
    return self.obj1 == self.obj2
~~~

Actual timing — importing the module increases the time required for a single call by around 500%:

~~~
python -m timeit '''\
def compare_weight(obj1, obj2):
    return obj1 == obj2
witch, duck = 1, 2
_ = compare_weight(witch, duck)'''

10000000 loops, best of 3: 0.195 usec per loop

#utils2.py
def compare_weight(self):
    return self.obj1 == self.obj2

python -m timeit -s '''\
import utils2
class Cases(object):
    def __init__(self):
        self.obj1 = 1
        self.obj2 = 2
    def compare_weight(self):
        return self.obj1 == self.obj2;''' '''\
witch, duck = 1, 2
this_case = Cases()
this_case.obj1 = witch
this_case.obj2 = duck
this_case.compare_weight()'''

1000000 loops, best of 3: 0.948 usec per loop


python -m timeit -s '''\
import utils2
class Cases(object):
    def __init__(self):
        self.obj1 = 1
        self.obj2 = 2''' '''\
witch, duck = 1, 2
this_case = Cases()
this_case.obj1 = witch
this_case.obj2 = duck
utils2.compare_weight(this_case)'''

1000000 loops, best of 3: 1 usec per loop
~~~

Or, if the function call is (more realistically) in a class method:

~~~
python -m timeit -s '''\
import utils2
class Cases(object):
    def __init__(self):
        self.obj1 = 1
        self.obj2 = 2
    def do_it(self):
        utils2.compare_weight(self)
        ''' '''\
witch, duck = 1, 2
this_case = Cases()
this_case.obj1 = witch
this_case.obj2 = duck
this_case.do_it()'''

1000000 loops, best of 3: 1.09 usec per loop
~~~

But these timing differences drop to an increase of about 220-230% when there are large numbers of function calls:

~~~
python -m timeit '''\
def compare_weight(obj1, obj2):
    return obj1 == obj2
witch, duck = 1, 2
for i in range(1000000):
    _ = compare_weight(witch, duck)'''

10 loops, best of 3: 128 msec per loop


python -m timeit -s '''\
import utils2
class Cases(object):
    def __init__(self):
        self.obj1 = 1
        self.obj2 = 2
    def compare_weight(self):
        return self.obj1 == self.obj2;''' '''\
witch, duck = 1, 2
this_case = Cases()
this_case.obj1 = witch
this_case.obj2 = duck
for i in range(1000000):
    _ = this_case.compare_weight()'''
    
10 loops, best of 3: 278 msec per loop

python -m timeit -s '''\
import utils2
class Cases(object):
    def __init__(self):
        self.obj1 = 1
        self.obj2 = 2''' '''\
witch, duck = 1, 2
this_case = Cases()
this_case.obj1 = witch
this_case.obj2 = duck
for i in range(1000000):
    _ = utils2.compare_weight(this_case)'''

10 loops, best of 3: 289 msec per loop

python -m timeit -s '''\
import utils2
class Cases(object):
    def __init__(self):
        self.obj1 = 1
        self.obj2 = 2
    def do_it(self):
        for i in range(1000000):
            _ = utils2.compare_weight(self)''' '''\
witch, duck = 1, 2
this_case = Cases()
this_case.obj1 = witch
this_case.obj2 = duck
this_case.do_it()'''

10 loops, best of 3: 298 msec per loop
# a 7% increase over  the 
~~~

[end]
