## Deep reloading of Ipython modules

Use
```
%load_ext autoreload
%autoreload 2
```
(see http://stackoverflow.com/a/9179917/621762) rather than `IPython.lib.deepreload` (see https://github.com/ipython/ipython/issues/1626). (20130221)

Place commands in startup script:

    .ipython/profile_default/startup/ipython3_startup.ipy

Note `.ipy` extension. 

**20130507**. However, although this works under Python 3.2 and 3.3, it seems to cause problems under Python 2.7. I am using IPython 0.13.2, installed with pip in separate virtualenv environments for Python 2.7 and Python 3.3. With Python 2.7, I frequently get errors having to do with `autoreload`, almost always leading back to `superreload(m, reload, self.old_objects)`. When `ipython3_startup.ipy` is disabled, the problem goes away. How can I maintain the startup instructions without getting this error in Ipython for Python 2.7?

[end]
