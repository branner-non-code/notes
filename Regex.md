Regex
-----

1.  ​20130305. Had trouble with escaping `*`, but it seems to work as
    expected on 20130306:

        In [1]: s = '1234*grubby-boo'

        In [2]: s
        Out[2]: '1234*grubby-boo'

        In [3]: import re

        In [4]: re.sub('\*', '&', s)
        Out[4]: '1234&grubby-boo'

    Not sure what was wrong earlier.

2.  ​20130319. I had URLs ending with a lot of junk preceded by
    `?instance…`. Rather than using

        url_tail = re.compile('(.+)\?instance.+$')
        x = re.search(url_tail, url).match(0)
        if x:
            url = x

    it was simpler just to use

        url = url.split('?')[0]

    Lesson: where a single unique character occurs in a regex search
    expression, consider using `split`, instead.

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

    Unpacking 
    ----------

    `*a_list` unpacks the list into a tuple (which must be an
    “assignment target”):

        In [90]: a_list = [i for i in range(10)]

        In [91]: print(*a_list)                 
        0 1 2 3 4 5 6 7 8 9

[end]
