## PyGotham 2014 talk: Daniel Kronovet, "Setting up Your Python Development Environment"

20140817

### REPL functions

`Out` as a dictionry

### PyText

```
py.test -x # fail fast
py.test --pdb # auto debug
py.test -s # for use with ipdb
```

Tests should be independent.

micro-testing (unit tests) vs. macro-testing (integration tests but less coverage)

### Debugging

Use single line `import pdb; pdb.set_trace()` in mid-code.x

or

`py.test --pdb ...`


### Best practices

 * Disable creation of pic-files.
 * Use autoreload.

[end]