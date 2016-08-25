Brandon Rhodes - Oh, Come On Who Needs Bytearrays - PyCon 2015

https://www.youtube.com/watch?v=z9Hmys8ojno

"Strings that don't pretend that they have symbols inside of them so much as they know that their innards are really bytes — eight-bit codes."

 * `b''` prefix mandatory under Python 3.
 * mutability is functional-like: it is always a new object that is returned
 * bytearray is mutable and based on Python 3's `bytes`
   * awkward and requires `decode()` before the content can be treated as characters
   * models Python 2 `str`
   * elements are numbers, not characters

 1. applications:
 
    2. the bit vector. `bytearray` is more specific than `array.array`, containing integers only, and so faster; but `list` is faster still; `bytearray` is space-efficient.
    2. reusable buffer. `memoryview` creates an offset of a bytearray; can be used to to slightly beat `write` and has a better memory profile than `str`.
    2. accumulator (progressive concatenation of strings). `bytearray`s handle `+=` very quickly
    2. freestyle mutable string. All methods that `bytearray` shares with `str` are immutable! `bytearray` only changes when subjected to list-like operations.

 1. Slides contain useful links at end.

[end]