# Sorting a list of Unicode strings in Python 2.6, case-insensitively and ignoring diacritics

## Problem

Tricky because the sort-key `key=str.lower` apparently only works for ASCII strings, not Unicode strings. Error

```
TypeError: descriptor 'lower' requires a 'str' object but received a 'unicode'
```

## Working solution

Declare locale and let `LANG` environment set the encoding:

```
import locale
locale.setlocale(locale.LC_ALL, '')
listname = sorted(listname, cmp=locale.strcoll)
```

Seems to work; My encoding is set to `en_US.UTF-8`, which treats A, a, and ā as the same letter; that’s what I want for sorting in this particular case.

## Specifying the encoding

This is also possible, but according to the Python docs at http://docs.python.org/release/2.6.6/library/locale.html?highlight=locale#locale.setlocale, it seems the actual encoding can be left out and supplied from one’s environment.

That’s what the empty single quotes are in `locale.setlocale(locale.LC_ALL, '')`; but they need to be there because `setlocale()` takes a 2-tuple. Trying that on my system returns `en_US.UTF-8`. If I omit the single quotes altogether, the function returns `C` and the sort is case sensitive. 

---

Adapted from an [old blog post](http://brannerchinese.wordpress.com/2012/03/06/sorting-a-list-of-unicode-strings-in-python-case-insensitively-and-ignoring-diacritics/), dated 20120306?
