# Nesting tuples

Normally adding tuples together merges them:
```
In [1]: a = (1, )

In [2]: b = (2,3)

In [3]: a + b
Out[3]: (1, 2, 3)
```

In order to nest one inside another, any tuple to be nested must be explicitly placed within the tuple-parentheses:
```
In [4]: a + (b,)
Out[4]: (1, (2, 3))

In [5]: (a,) + b
Out[5]: ((1,), 2, 3)

In [6]: (a,) + (b,)
Out[6]: ((1,), (2, 3))

```

[end]
