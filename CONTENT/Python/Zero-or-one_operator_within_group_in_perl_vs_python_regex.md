## Zero-or-one Operator within a Group in Perl vs. Python Regex

One feature of Perl-style regular expressions that is not implemented in Python is the use of the zero-or-one operator (metacharacter "question mark", `?`) with a parenthesis-delimited "group" or marked sub-expression. In Python, if such a group is found (below, `(ghi)?`), it can be referred back to with a back-reference (below, `\2`; code below is Python 3.3 in Ipython 0.13.2):

~~~
In [1]: re.sub('(abc)\t(ghi)', r'\2', 'abc\tghi')
Out[1]: 'ghi'
~~~

but if it is not found an error is raised instead of an empty string being returned (which is the norm):

~~~
In [2]: re.sub('(abc)\t(ghi)?', r'\2', 'abc\t') ... error: unmatched group
~~~

I’m aware of two work-arounds for this curious situation.
First, rewrite the optional sub-expression as an optional look-ahead marked sub-expression: `((?:ghi)?)`. There are two pairs of parentheses: one for the look-ahead syntax `(?:...)` and one for the optional matching group `(...?)`:

~~~
In [3]: re.sub('(abc)\t((?:ghi)?)', r'\2', 'abc\tghi') Out[3]: 'ghi' In [4]: re.sub('(abc)\t((?:ghi)?)', r'\2', 'abc\t') Out[4]: ''
~~~

Second, discard the zero-or-one operator and put a set-union operator (metacharacter "pipe", `|`) inside the parentheses so that the sub-expression now means "either nothing or else the target in question" (below, `(|ghi)`):

~~~
In [5]: re.sub('(abc)\t(|ghi)', r'\2', 'abc\tghi') Out[5]: 'ghi' In [6]: re.sub('(abc)\t(|ghi)', r'\2', 'abc\t') Out[6]: ''
~~~

The first work-around is marginally faster than the second:

~~~
$ python -m timeit -n 1000000 -s "from re import sub" "sub('(abc)\t((?:ghi)?)', r'\2', 'abc\tghi')" 1000000 loops, best of 3: 6.48 usec per loop $ $ python -m timeit -n 1000000 -s "from re import sub" "sub('(abc)\t(|ghi)', r'\2', 'abc\tghi')" 1000000 loops, best of 3: 6.97 usec per loop $
~~~

though it’s longer to type and more complex to understand and remember.
I vote for the second work-around.

I’ve just noticed that the replacement version of regex now at PyPi addresses this issue (version ["regex 2013-06-26"](https://pypi.python.org/pypi/regex)):

[end]
