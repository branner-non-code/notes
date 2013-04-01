Syntax
------

1.  ​20130312. Use full, explicit module names, including full explicit
    method names, rather than abbreviating in any way. This aids
    readability and drop-in replacement.

2.  ​20130313. Tom Ballinger recommends against using the backslash to
    continue lines. Instead, place content within redundant parentheses.

3.  ​20130313. If only one variable is to be inserted in a string, can
    use

        '{}'.format(variable)

    rather than

        '{0}'.format(variable)

[end]
