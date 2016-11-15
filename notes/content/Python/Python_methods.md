## Python methods

### Static vs. class vs. abstract methods

Following https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods (accessed 20161115)


### Python public and private methods

(Following my own post: http://stackoverflow.com/a/38864561/621762)

The "dunder" (double underscore, `__`) prefix prevents access to attribute, except through accessors.

```python
class Foo():
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
>>> f = Foo()
>>> f.__attr                          # Not directly accessible.
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Foo' object has no attribute '__attr'
>>> '__attr' in f.__dir__()           # Not listed by __dir__()
False
>>> f.__getattribute__('__attr')      # Not listed by __getattribute__()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Foo' object has no attribute '__attr'
>>> f.attr                            # Accessible by implemented getter.
0
>>> f.attr = 'Presto'                 # Can be set by implemented setter.
>>> f.attr
'Presto'
>>> f.__attr = 'Tricky?'              # Can we set it explicitly?
>>> f.attr                            # No. By doing that we have created a 
'Presto'                              # new but unrelated attribute, same name.
```

[end]

[end]