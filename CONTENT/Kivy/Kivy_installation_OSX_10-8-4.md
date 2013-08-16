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

### Making available to Python

 1. As of 20130816, we are talking about Python 2.7; Kivy is still in the midst of being ported to Python 3.3.
 2. Required two `pip` installations within the Python 2.7 `virtualenv`:

         pip install --upgrade Cython
         pip install --upgrade kivy

 Now (within Ipython):
 
         In [1]: import kivy.app
         [INFO   ] Kivy v1.7.2
         [INFO   ] [Logger      ] Record log in /Users/dpb/.kivy/logs/kivy_13-08-16_5.txt
         [INFO   ] [Factory     ] 144 symbols loaded
         [DEBUG  ] [Cache       ] register <kv.lang> with limit=None, timeout=Nones
         [DEBUG  ] [Cache       ] register <kv.image> with limit=None, timeout=60s
         [DEBUG  ] [Cache       ] register <kv.atlas> with limit=None, timeout=Nones
         [INFO   ] [Image       ] Providers: img_imageio, img_tex, img_dds, img_gif (img_pygame, img_pil ignored)
         [DEBUG  ] [Cache       ] register <kv.texture> with limit=1000, timeout=60s
         [DEBUG  ] [Cache       ] register <kv.shader> with limit=1000, timeout=3600s

 1. The next line in the documentation leads to an error:
         
         In [2]: from kivy.uix.label import Label
         [DEBUG  ] [Text        ] Ignored <pygame> (import error)
         [DEBUG  ] [Text        ] Ignored <sdlttf> (import error)
         [DEBUG  ] [Text        ] Ignored <pil> (import error)
         [CRITICAL] [Text        ] Unable to find any valuable Text provider at all!
         ...
         AttributeError: 'NoneType' object has no attribute 'register'

Why?

[end]
