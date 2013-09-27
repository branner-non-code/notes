## Deep reloading of Ipython modules

### In startup script

Use
```
%load_ext autoreload
%autoreload 2
```
(see http://stackoverflow.com/a/9179917/621762) rather than `IPython.lib.deepreload` (see https://github.com/ipython/ipython/issues/1626). (20130221)

Place commands in startup script:

    .ipython/profile_default/startup/ipython3_startup.ipy

Note `.ipy` extension. 

### To check what is being reloaded
~~~
%aimport
~~~

[end]
