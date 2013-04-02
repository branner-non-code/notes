Regex annoyances
================

Major differences from Python/Perl usage in matching
----------------------------------------------------
| Python | function | SQL |
|:------:|:--------:|:---:|
| `?`      | 0 or more | `%` |
| `.`      | 1 exactly | `_` |
| `.+`     | 1 or more (greedy?) | `_%` |

 Remember to use `LIKE` when describing the contents of a field, rather than `=`:

    DELETE FROM urls WHERE url LIKE 'http_%http%';
