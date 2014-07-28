## MATLAB - use a single range for multiple functions

20120128. Assign a range (in brackets and colon-delimited) to a symbolic variable and then use the variable where a range would be.

~~~
syms x x_range;
x_range = [-pi:-pi/2:0;pi/2:pi];
y = sin(x.^2).*cos(x);
y1 = ezplot(y, x_range);
~~~

[end]
