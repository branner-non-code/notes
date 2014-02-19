**Problem**: find the source-code for a Python built-in function, `id()`.

### CPython (3.3.4)

Use `find` with `grep`, supplying `-w` option to `grep` in order to 

~~~
$ find -iname '*.c' -print0 | xargs -0 grep -n -w '"id"'
...
./Python/bltinmodule.c:2371:    {"id",              builtin_id,         METH_O, 
...
~~~

`bltinmodule.c` seems to be the right place to look for built-ins.

Examining line 2371 of `Python/bltinmodule.c` shows 

~~~
{"id",              builtin_id,         METH_O, id_doc},
~~~

and seeking `builtin_id` in the same file brings up:

~~~
static PyObject *
builtin_id(PyObject *self, PyObject *v)
{
    return PyLong_FromVoidPtr(v);
}
~~~

### PyPy (2.2.1)

Using `locate` to find files containing "builtin" identifies a file `pypy/module/__builtin__/__init__.py`. Searching for `id` there hits

~~~
class Module(MixedModule):
    interpleveldefs = {
        'id'            : 'operation.id',
    }
~~~

After

~~~
$ find -iname '*.py' -print0 | xargs -0 grep -n -w 'def id'
...
./pypy/interpreter/baseobjspace.py:671:    def id(self, w_obj):
./pypy/module/__builtin__/operation.py:97:def id(space, w_object):
~~~

The meaning of this depends on what `space` means. In `pypy/module/__builtin__/operation.py` at line 97 we find:

~~~
def id(space, w_object):
    "Return the identity of an object: id(x) == id(y) if and only if x is y."
    return space.id(w_object)
~~~

In `pypy/interpreter/baseobjspace.py` at line 671 we find:

~~~
class ObjSpace(object):
    """Base class for the interpreter-level implementations of object spaces.
    http://pypy.readthedocs.org/en/latest/objspace.html"""

    def __init__(self, config=None):
        "NOT_RPYTHON: Basic initialization of objects."
        ...
    
    def id(self, w_obj):
        w_result = w_obj.immutable_unique_id(self)
        if w_result is None:
            # in the common case, returns an unsigned value
            w_result = self.wrap(r_uint(compute_unique_id(w_obj)))
        return w_result
~~~

Still need to use 

~~~
find -iname '*.py' -print0 | xargs -0 grep -n -w 'immutable_unique_id'
~~~

But what about `space`?

From http://doc.pypy.org/en/latest/objspace.html:

> The object space creates all objects and knows how to perform operations on the objects. You may think of an object space as being a library offering a fixed API, a set of operations, with implementations that correspond to the known semantics of Python objects.

[end]