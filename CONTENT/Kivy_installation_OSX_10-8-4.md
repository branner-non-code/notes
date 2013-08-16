## Kivy installation on OS X, 10.8.4

### Starting from the command line

Many efforts to get Kivy working failed today, both compilation and then calling from the command line. The Finally I have placed an alias in my `.bash_profile`:

~~~
alias kivy='/Applications/kivy_172/Kivy.app/Contents/MacOS/Kivy'
~~~

(Kivy and related files are within a directory of their own, `kivy_172`.)

Now calling it as

~~~
kivy /Applications/kivy_172/examples/gestures/gesture_board.py
~~~

works.

[end]
