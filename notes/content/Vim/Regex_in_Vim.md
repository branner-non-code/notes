## Regex annoyances

### Major differences from Python/Perl usage in matching

| Python | function | Vim | notes |
|:------:|:--------:|:---:|:-----:|
| `?`      | 0 or more | `*` | greedy |
|        |     "     | `\{-}` | non-greedy |
| `+`      | 1 or more | `\+` | greedy |
|        |     "      | `\{-1,}` | non-greedy|
| `+?`   |  0 or 1 | `\=` |
| `(...)` | group | `\(...\)` 
| `\0` | whole match | `&` or `\0`
|  | most recent match | `~`

### Other searching tricks

 * Enclose item in `\<` and `\>` to search for "whole word".
 * Use `^f` to edit Vim command line in new Vim sub-buffer.

### Good reference documents

 * http://vimdoc.sourceforge.net/htmldoc/pattern.html
 * http://vimregex.com

[end]
