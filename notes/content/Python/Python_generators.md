## Python generators

Do in fact use lazy evaluation:

```
In [1]: import time

In [2]: y = (time.sleep(x * 100) for x in range(10))

In [3]: next(y)

In [4]: # appears after 0 seconds

In [5]: next(y)

In [6]: # appears after 100 seconds
```

[end]