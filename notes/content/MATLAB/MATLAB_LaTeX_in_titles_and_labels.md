## MATLAB - LaTeX in titles and labels

Based on http://www.mathworks.com/matlabcentral/newsreader/view_thread/239315 (accessed 20120128)

Assign the desired legend to a variable and then set "interpreter" of the variable to "latex":

~~~
leg = legend('y', '$\frac{dy}{dx}$');
set(leg, 'interpreter', 'latex');
~~~

There are more complicated ways, shown at http://www.mathworks.com/matlabcentral/newsreader/view_thread/239315 .

[end]
