## Python methods

### Static vs. class vs. abstract methods

#### Bound instance methods are the default

Examples here are for Python 3; Python 2 behaves somewhat differently.

Methods are "bound" by default in Python 3: they can only be called on an instance of the class in which they are defined. That instance may be assigned to a variable:

```python
class Example:
    def default(self):
        return '子程式'

>>> e = Example()
>>> e.default()
'子程式'
```

Or it may be instantiated on the fly

```python
>>> Example().default()
'子程式'
```

We can show that `default` is bound to a _particular_ instance in either case, because we can ask for that instance's memory location using the `__self__` attribute:

```python
>>> Example().default.__self__
<__main__.Example at 0x10c0ce588>

>>> e.default.__self__
<__main__.Example at 0x10c073780>
```

But it can't be called on the uninstantiated class itself:

```python
>>> Example.default()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: default() missing 1 required positional argument: 'self'
```

Here, when the interpreter says it requires the argument `self` it means it needs a particular instance of `Example` in order to call `default` on. There is no such instance:

```python
>>> Example.default.__self__
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-265-288eb236fab6> in <module>()
----> 1 Example.default.__self__

AttributeError: 'function' object has no attribute '__self__'
```

#### Static methods: methods without an instance

To call a method without having to have an instance, use the `@staticmethod` decorator, and omit the `self` argument:

```python
class Example:
    @staticmethod
    def static():
        return 'no instance required'

    def default(self):
        return 'instance definitely required'

>>> Example.static()
'no instance required'

>>> Example.default()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-81-0ee562c33c8c> in <module>()
----> 1 Example.default()

AttributeError: type object 'Example' has no attribute 'default'
```

In Python 3, a static method can be called on the class itself or on an instance. If you simply omit `self`, the method can be called on the class but not on an instance — `self` represents that instance itself.

```python
class Example:
    def default():
        return 'can be called on class but not on instance'

    def default2(self):
        return 'can be called on instance but not on class'

    @staticmethod
    def default3():
        return 'can be called on class or instance'

>>> Example.default()      # called on class
'can be called on class but not on instance'

>>> Example().default()    # called on instance
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: default() takes 0 positional arguments but 1 was given

>>> Example().default2()   # called on instance
'can be called on instance but not on class'

>>> Example.default2()     # called on class
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: default2() missing 1 required positional argument: 'self'

>>> Example().default3()   # called on instance
'can be called on class or instance'

>>> Example.default3()     # called on class
'can be called on class or instance'
```

(In Python 2, `Example.default()` and `Example.default2()` are not allowed — an instance method must receive that instance. `Example.default()` has no `self` parameter at all, and `Example.default2()` has `self` but no instance is being passed to it.)

#### Class method: method called on a class itself, without instances

This differs from a regular method that has no `self` parameter: it must have a `cls` parameter, which refers to the class itself, not the method.

This parameter can be used to access attributes of the class and modify them for all future instantiations:

```python
class Example:
    x = 'original'

    def sample(self):
        return 'instance: {}, x: {}'. format(self, self.x)

    @classmethod
    def class_method(cls, x=None):
        cls.x = x
        return 'x: {}'.format(cls.x)

>>> Example().sample()    # first instantiation
'instance: <__main__.Example object at 0x10c1605f8>, x: original'

>>> Example().sample()    # second instantiation
'instance: <__main__.Example object at 0x10c1591d0>, x: original'

>>> Example().sample()    # third instantiation
'instance: <__main__.Example object at 0x10c159320>, x: original'

>>> Example.class_method('changed by user')
'x: changed by user'

>>> Example().sample()    # fourth instantiation; attribute changed!
'instance: <__main__.Example object at 0x10c159400>, x: changed by user'
```

Without this `cls` parameter, a class method does not seem to be callable at all:

```python
class Example:
    @classmethod
    def class_method(cls):
        return 'cls: {}'.format(cls)

    @classmethod
    def uncallable():
        return 'cannot be called'

>>> Example.class_method()
"cls: <class '__main__.Example'>"

>>> Example().class_method()
"cls: <class '__main__.Example'>"

>>> Example.uncallable()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-215-24d82097b8f7> in <module>()
----> 1 Example.uncallable()

TypeError: uncallable() takes 0 positional arguments but 1 was given

>>> Example().uncallable()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-216-633d8ae56478> in <module>()
----> 1 Example().uncallable()

TypeError: uncallable() takes 0 positional arguments but 1 was given
```

#### Abstract method: leave future implementation completely free, for modification by inheritance

A method can be prepared for future implementation implicitly using `pass` or `return` as the dummy body, or explicitly using `@abc.abstractmethod`. Explicitly declaring a method to be abstract means that it cannot be called directly, and a class that contains only abstract methods cannot be instantiated at all, although it can be subclassed.

An explicit abstract method requires you to import the `abc` module and specify a special argument `metaclass=abc.ABCMeta` in the class definition:

```python
import abc

class C(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def an_abstract_method(self):
        pass
```

Even with the `@abc.abstractmethod` decorator, some sort of nominal body seems to be needed in the method: a docstring or `pass`, for instance:

```python
class C(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def an_abstract_method(self):
        """(dummy docstring)"""
```

The decorators `@classmethod` and `@abc.abstractmethod` can be composed, in order to create an abstract class method. `@classmethod` is applied after `@abc.abstractmethod` — in other words, `@classmethod` appears _before_ `@abc.abstractmethod`:

```python
import abc

class C(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def abstract_class_method(cls):
        """(dummy docstring)"""
```

(TODO: Examples would be useful here.)


### Python public and private methods

(Following my own post: http://stackoverflow.com/a/38864561/621762)

The "dunder" (double underscore, `__`) prefix prevents access to attributes, except through the accessors `@property`, `@attr.setter`, and `@attr.deleter`.

```python
class C():
    def __init__(self):
        self.__attr = 0

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        self.__attr = value

    @attr.deleter
    def attr(self):
        del self.__attr
```

Some examples:

```python
>>> f = C()

>>> f.__attr                          # Not directly accessible.
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'C' object has no attribute '__attr'

>>> '__attr' in f.__dir__()           # Not listed by __dir__()
False

>>> f.__getattribute__('__attr')      # Not listed by __getattribute__()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'C' object has no attribute '__attr'

>>> f.attr                            # Accessible by the implemented getter.
0

>>> f.attr = 'Presto'                 # Can be set by the implemented setter.

>>> f.attr
'Presto'

>>> f.__attr = 'Tricky?'              # Can we set it explicitly?

>>> f.attr                            # No. By doing that we have created a
'Presto'                              # new but unrelated attribute, same name.
```

[end]