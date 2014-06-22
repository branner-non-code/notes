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

On using

~~~
find -iname '*.py' -print0 | xargs -0 grep -n -w 'immutable_unique_id'
~~~

there seem to be several definitions for different types of objects:

~~~
./pypy/objspace/std/longtype.py:128:    def immutable_unique_id(self, space):
./pypy/objspace/std/inttype.py:193:    def immutable_unique_id(self, space):
./pypy/objspace/std/unicodeobject.py:35:    def immutable_unique_id(self, space):
./pypy/objspace/std/floattype.py:287:    def immutable_unique_id(self, space):
./pypy/objspace/std/stringobject.py:34:    def immutable_unique_id(self, space):
./pypy/objspace/std/complexobject.py:36:    def immutable_unique_id(self, space):
~~~

In `longtype.py`:

~~~
class W_AbstractLongObject(W_Object):
    ...

    def immutable_unique_id(self, space):
        if self.user_overridden_class:
            return None
        from pypy.objspace.std.model import IDTAG_LONG as tag
        b = space.bigint_w(self)
        b = b.lshift(3).or_(rbigint.fromint(tag))
        return space.newlong_from_rbigint(b)
~~~

In `inttype.py`:

~~~
class W_AbstractIntObject(W_Object):
    ...

    def immutable_unique_id(self, space):
        if self.user_overridden_class:
            return None
        from pypy.objspace.std.model import IDTAG_INT as tag
        b = space.bigint_w(self)
        b = b.lshift(3).or_(rbigint.fromint(tag))
        return space.newlong_from_rbigint(b)
~~~

In `unicodeobject.py`:

~~~
class W_AbstractUnicodeObject(W_Object):
    ...

    def immutable_unique_id(self, space):
        if self.user_overridden_class:
            return None
        return space.wrap(compute_unique_id(space.unicode_w(self)))
~~~

In `floattype.py`:

~~~
class W_AbstractFloatObject(W_Object):
    ...

    def immutable_unique_id(self, space):
        if self.user_overridden_class:
            return None
        from rpython.rlib.longlong2float import float2longlong
        from pypy.objspace.std.model import IDTAG_FLOAT as tag
        val = float2longlong(space.float_w(self))
        b = rbigint.fromrarith_int(val)
        b = b.lshift(3).or_(rbigint.fromint(tag))
        return space.newlong_from_rbigint(b)
~~~

In `stringobject.py`:

~~~
class W_AbstractStringObject(W_Object):
    ...

    def immutable_unique_id(self, space):
        if self.user_overridden_class:
            return None
        return space.wrap(compute_unique_id(space.str_w(self)))
~~~

In `complexobject.py`:

~~~
class W_AbstractComplexObject(W_Object):
    ...

    def immutable_unique_id(self, space):
        if self.user_overridden_class:
            return None
        from rpython.rlib.longlong2float import float2longlong
        from pypy.objspace.std.model import IDTAG_COMPLEX as tag
        real = space.float_w(space.getattr(self, space.wrap("real")))
        imag = space.float_w(space.getattr(self, space.wrap("imag")))
        real_b = rbigint.fromrarith_int(float2longlong(real))
        imag_b = rbigint.fromrarith_int(r_ulonglong(float2longlong(imag)))
        val = real_b.lshift(64).or_(imag_b).lshift(3).or_(rbigint.fromint(tag))
        return space.newlong_from_rbigint(val)
~~~

----

But what about `space`?

From http://doc.pypy.org/en/latest/objspace.html:

> The object space creates all objects and knows how to perform operations on the objects. You may think of an object space as being a library offering a fixed API, a set of operations, with implementations that correspond to the known semantics of Python objects.

[end]