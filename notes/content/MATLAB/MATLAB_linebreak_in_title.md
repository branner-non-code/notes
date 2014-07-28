## MATLAB - linebreak in title

From http://www.mathworks.com/matlabcentral/newsreader/view_thread/305775 (20120128)

### strvcat

~~~
title(strvcat('Line1','Line2'))
~~~

### concatenated strings

~~~
str = {'This is the first line', 'This is the second line'}'
title(str)
~~~

### \n with sprintf

~~~
caption = sprintf('This is the first line.\nThis is the second line');
   title(caption)
~~~

[end]
