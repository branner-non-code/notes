## Printing and writing delays

### Flush buffers with `sys`

I found some `print` output within a `try`-`except` block, itself within a `for` loop, itself within a *with* block, was being delayed by many minutes, and I fixed it by the use of

        sys.stdout.flush()

### Flush buffers with `os`

        os.fsync()

### Flush buffers with `print`

The full `print` syntax is:

~~~
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
~~~

[end]
