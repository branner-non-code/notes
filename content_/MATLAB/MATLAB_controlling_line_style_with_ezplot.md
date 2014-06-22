## MATLAB - controlling line style with ezplot

### Basics
For some function y, set another variable = ezplot(y) and use {{{set}}} to control its attributes:

```
syms x; y = sin(x);
y1 = ezplot(y);
set(y1, 'Color', 'm');  % m produces magenta, etc.
set(y1, 'Line', '-');   % or ':' for dotted line
set(y1, 'Marker', '+'); % + for plus sign, etc.
set(y1, 'LineWidth', 2); % >1 for thicker lines
```

### List of values

Taken from ''MATLAB® 7 Getting Started Guide'' (Sixteenth printing, Revised for MATLAB 7.11 [R2010b]), p. 3-59.

#### Color
 * 'c': cyan
 * 'm': magenta
 * 'y': yellow
 * 'r': red
 * 'g': green
 * 'b': blue
 * 'w': white
 * 'k': black

#### Line style
 * '-': solid
 * '--': dashed
 * ':': dotted
 * '.-': dash-dot
 * no character: no line

#### Marker type
 * '+': plus mark
 * 'o': unfilled circle
 * '*': asterisk
 * 'x': letter x
 * 's': filled square
 * 'd': filled diamond
 * '^': filled upward triangle
 * 'v': filled downward triangle
 * '>': filled right-pointing triangle
 * '<': filled left-pointing triangle
 * 'p': filled pentagram
 * 'h': filled hexagram
 * no character or none: no marker

[end]
