Scrapers
========

PyQuery
-------

​20130211. David Lundgren recommends `pyquery`
(<https://github.com/gawel/pyquery>), a wrapper on `libxml2`. He says it
is extremely fast and has a familiar, `query`-like syntax.

Beautiful Soup 4
----------------

1.  20130218? Installation of this library for Python 3 was challenging.
    On Ubuntu 12.04 I it was sufficient to install

        sudo pip install beautifulsoup4

    but on OS 10.6.8 and 10.8.2 I had to turn to

        sudo pip-3.2 install beautifulsoup4

2.  20130218? Within code it is imported as

        from bs4 import BeautifulSoup as BS

3.  ​20130218. Can iterate over a list of all examples of a given tag
    and then act on them:

        for item in soup.find_all('li'):
            print(item.a, item.cite, item.span)

4.  ​20130218. `prettify` is useful when used on a restricted element of
    this kind:

        for item in soup.find_all('li'):
            print(item.prettify())

5.  ​20130218. What appeared to be a space in one element turned out not
    to be a true space (codepoint 32) but non-breaking space `\xa0`
    (codepoint 160) (HTML `&nbsp;`). Look for a process to make all
    space-like things into spaces, uniformly. Till then, use
    `replace()`:

        for item in soup.find_all('li'):
            link_complex = item.a
            citation = item.cite
            the_span = item.span
            print(str(citation).replace('\xa0'+str(the_span), ''))

urllib
------

1.  ​20130211. As of Python 3 there are now a number of changes to what
    had been `urllib2` in Python 2:

    1.  Module `urllib2` now merged into `urllib`.

    2.  Exception `urllib2.URLError` is now `urllib.error.URLError`.

    3.  Method `urllib2.urlopen()` is now `urllib.request.urlopen()`.

2.  ​20130213. It seems that the output of
    `U.request.urlopen(url).read()` is always going to be bytecode and
    has to be converted to Unicode. Add `.decode()` to it. More fully, I
    used `decode()`

        data_list = U.request.urlopen(url).read().strip()            
        data_list = data_list.decode().split('\r\n')

[end]
