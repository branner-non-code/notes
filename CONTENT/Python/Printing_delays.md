Printing delays
---------------

1.  ​20130319. I found some `print` output within a `try`-`except`
    block, itself within a `for` loop, itself within a *with* block, was
    being delayed by many minutes, and I fixed it by the use of

        sys.stdout.flush()

[end]
