Regex annoyances
----------------

1. Differences from Python/Perl usage:
 | Python | function | Vim | notes |
 | ------ |:--------:|:---:|:-----:|
 | ?      | 0 or more | * | greedy |
 |        |          | \{-} | non-greedy |
 | +      | 1 or more | \+ | greedy |
 |        |           | \{-1,| non-greedy|
