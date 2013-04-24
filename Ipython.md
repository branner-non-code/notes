Ipython
=======

Deep reloading of modules
-------------------------
Use
    %load_ext autoreload
    %autoreload 2
(see http://stackoverflow.com/a/9179917/621762) rather than `IPython.lib.deepreload` (see https://github.com/ipython/ipython/issues/1626). (20130221)

Pasting text
------------
Use `%cpaste` now and place `--` on the last line to end pasted input. (20130218)

Open editor directly within Ipython
-----------------------------------
Use `edit` or `%edit`. To continue to work on the previous buffer, use `edit -p` or `%edit -p`. Use `%edit _NN` to edit the same text as input prompt \#NN. (20130318)

Startup scripts
---------------
Place commands in

    .ipython/profile_default/startup/ipython3_startup.ipy
Note `.ipy` extension. Currently using:
```
%load_ext autoreload
%autoreload 2
```

[end]
