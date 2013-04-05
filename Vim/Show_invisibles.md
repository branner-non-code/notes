Show invisibles
---------------

 1. Simplest is to use 
 ~~~
:set invlist
~~~
 http://superuser.com/questions/19640/how-to-distinguish-between-r-n-and-n-in-vim, 20120315.

 1. http://superuser.com/questions/97692/vim-show-line-feeds-carriage-return recommends, 20120315:
 ~~~
:set listchars=eol:$,tab:\[SPACE]\[SPACE]
:highlight SpecialKey ctermfg=5
~~~

