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

    Don't know why it didn't originally work.

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

[end]
