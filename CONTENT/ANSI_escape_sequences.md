## ANSI escape sequences

### Usage

~~~
'\033[' + str(i) + 'm'
~~~

 Where: `i` is in range 31-37, 41-47 (w/background), 90-95, 100-105 (w/background)

 0: end of escape sequence; default colors.

### Some colors that look good on both black and white backgrounds:

 * 42: dark green with background highlighted
 * 33: dark yellow
 * 43: dark yellow with background highlighted
 * 36: light blue
 * 37: grey
 * 90: grey
 * 94: blue
 * 91: red
 * 101: red with background highlighted
 * 95: purple
 * 105: purple with background highlighted

[end]
