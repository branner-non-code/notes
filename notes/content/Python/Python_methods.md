## Python decorators for object-oriented method behaviors

Python supplies special decorators for a number of tools common in object-oriented programming. Their functionality is implemented as ordinary built-in functions, but they are made available as decorators for easier application.

**Functionality for restricting access to a property (attribute) of a class**:

 * as function: `property(fget=None, fset=None, fdel=None, doc=None)`
 * as decorators: `@property`, `@x.getter`, `@x.setter`, `@x.deleter` for some attribute `__x`.
 
**Functionality for methods of a class**:

 1. Making a method "static" — available whether its class has been instantiated or not:
 
    * as function: `staticmethod(function)`
    * as decorator: `@staticmethod`

 1. Making a method "abstract" — available only for subclassing.
 
    * as function: `abc.abstractmethod(funcobj)`
    * as decorator: `@abc.abstractmethod`

**Functionality to modify attributes of a class, to take effect in all future instantiations**:

 * as function: `classmethod(function)`
 * as decorators: `@classmethod`

(A decorator appears on the line before before a function definition, as seen in the examples below. It seems at first to modify that function. In reality, the decorator incorporates the function into some other piece of code, built-in or otherwise, behind the scenes.)

### Python public and private methods

The "dunder" (double underscore, `__`) prefix prevents access to attributes, except through the accessors `@property`, `@attr.setter`, and `@attr.deleter`.

```python
class C():
    def __init__(self):
        self.__attr = 0

    @property              # This is a "getter", though not so named explicitly.
    def attr(self):
        """The doc-string for the whole property goes here."""
        return self.__attr

    @attr.setter
    def attr(self, value):
        self.__attr = value

    @attr.deleter
    def attr(self):
        del self.__attr
```

The `@property` decorator is always required here, even if some of the others are omitted. It allows a docstring to be associated with the whole property `attr`. Technically, `@property` subsumes the function of `@attr.getter`, although the two can be used separately:

```python
class C():
    def __init__(self):
        self.__attr = 0

    @property
    def attr(self):
        """Supply getter functionally for property "attr"."""
        return None

    @attr.getter
    def attr(self):
        return self.__attr
```

Some examples:

```python
>>> f = C()                           # Instantiate the object, to begin.

>>> f.__attr                          # Not directly accessible.
...
AttributeError: 'C' object has no attribute '__attr'

>>> '__attr' in f.__dir__()           # Not listed by __dir__()
False

>>> f.__getattribute__('__attr')      # Not listed by __getattribute__()
...
AttributeError: 'C' object has no attribute '__attr'

>>> f.attr                            # Accessible by the implemented getter.
0

>>> f.attr = 'Presto'                 # Can be set by the implemented setter.

>>> f.attr
'Presto'

>>> f.__attr = 'Tricky?'              # Can we set it explicitly?

>>> f.attr                            # No. By doing that we have created a
'Presto'                              #   new and different attribute.
>>> f.__attr                          #   The dunder is a part of that 
'Tricky?'                             #   attribute's name.

>>> del f.__attr                      # Not directly delible.
...
AttributeError: __attr

>>> del f.attr                        # Delete f.attr
>>> f.attr                            # Now it's gone.
...
AttributeError: 'C' object has no attribute '_C__attr'
```

(Actually, there is a way to access a protected property while circumventing the `@property` functionality. Let's use `i` to represent the instance name, `cls`  the class name, and `a` the protected attribute name. The protected property can be read and assigned directly using `i._cls__a`.)


### Static vs. class vs. abstract methods

#### Bound instance methods are the default

Examples here are for Python 3; Python 2 behaves somewhat differently.

Methods are functions that are "bound" by default in Python 3: they are normally called on an instance of the class in which they are defined. That instance may be assigned to a variable:

```python
class Example:
    def default(self):
        return '子程式'

>>> e = Example()
>>> e.default()
'子程式'
```

Or the class may be instantiated on the fly, by instantiating `Example` (as `Example()`) but not assigning it to a persistent variable.

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

But it can't be called on the uninstantiated class itself — here, `Example` without `()`:

```python
>>> Example.default()
...
TypeError: default() missing 1 required positional argument: 'self'
```

Here, when the interpreter says it requires the argument `self` it means it needs a particular instance of `Example` in order to call `default` on. It needs an instance because `default` was defined with `self` as its first parameter. But there is no such instance:

```python
>>> Example.default.__self__
...
AttributeError: 'function' object has no attribute '__self__'
```

#### Static methods: methods without an instance

To call a method without having to have an instance, use the `@staticmethod` decorator, and omit the `self` argument:

```python
class Example:
    @staticmethod
    def static():                       # Note: no "self" argument
        return 'no instance required'

    def default(self):                  # Note: "self" argument present
        return 'instance definitely required'

>>> Example.static()
'no instance required'

>>> Example.default()
...
AttributeError: type object 'Example' has no attribute 'default'
```

In Python 3, a static method can be called on the class itself or on an instance. If you simply omit `self`, the method can be called on the class. Though, it can not be called on an instance — `self` represents that instance itself.

```python
class Example:
    def default():                      # Note: no "self" argument
        return 'can be called on class but not on instance'

    def default2(self):                 # Note: "self" argument present
        return 'can be called on instance but not on class'

    @staticmethod
    def default3():                     # Note: no "self" argument
        return 'can be called on class or instance'
```

Here are examples called on an uninstantiated class `Example` itself:

```python
>>> Example.default()
'can be called on class but not on instance'

>>> Example.default2()
...
TypeError: default2() missing 1 required positional argument: 'self'

>>> Example.default3()
'can be called on class or instance'
```

And here are examples called on an instance of the class, created non-persistently with `Example()`:

```python
>>> Example().default()
...
TypeError: default() takes 0 positional arguments but 1 was given

>>> Example().default2()
'can be called on instance but not on class'

>>> Example().default3()
'can be called on class or instance'
```

(**Note**: In Python 2, `Example.default()` and `Example.default2()` are not allowed — an instance method _must_ have that instance passed to it. `Example.default()` can't receive the instance because has no `self` parameter at all, and `Example.default2()` has `self` but no instance is being passed to it.)

#### Class method: method called on a class itself, without instances

This differs from a regular method that has no `self` parameter: it must have a `cls` parameter, which refers to the class itself, not the method.

This parameter can be used to access attributes of the class and modify them for all future instantiations:

```python
class Example:
    x = 'original'

    def sample(self):
        """Output the instance and the attribute x, as found."""
        print('instance: {}, x: {}'. format(self, self.x))

    @classmethod
    def class_method(cls, x=None):
        """Modify the class attribute x."""
        cls.x = x
        print('x: {}'.format(cls.x))

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
...
TypeError: uncallable() takes 0 positional arguments but 1 was given

>>> Example().uncallable()
...
TypeError: uncallable() takes 0 positional arguments but 1 was given
```

#### Abstract method: leave implementation for creation or modification only by inheritance

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

(TODO: Examples of subclassing would be useful here.)

[end]