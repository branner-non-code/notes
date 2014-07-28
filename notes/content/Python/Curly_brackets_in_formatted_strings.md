## Curly brackets in formatted strings

The `format()` command for strings inserts data inside of curly brackets in a string:

    >>> 'Insert five here: {}.'.format(5)
    'Insert five here: 5.'

If you want literal brackets in a string modified by `format()`, you have to escape the brackets by doubling them:

    >>> 'Here is what brackets look like: {{}}.'.format()
    'Here is what brackets look like: {}.'

To place data inside of literal brackets, you need triple brackets — double-escaped brackets for the literal brackets and then another pair of brackets as the socket for the data:

    >>> 'Now put five inside of brackets: {{{}}}.'.format(5)
    'Now put five inside of brackets: {5}.'

[end]
