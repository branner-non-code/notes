Compression
-----------

​20130320. If I am compressing whole web pages, there is a significant
savings in using `bz2`. But if I am isolating the Chinese to compress,
the compressed form is actually longer (as a bytecode string) than the
original unicode string! However, the compressed form is smaller on
disk.

[end]
