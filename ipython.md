python
=======

1.  ​20130221. For deep reloading of modules, use

        %load_ext autoreload
        %autoreload 2

    (see <http://stackoverflow.com/a/9179917/621762>) rather than
    `IPython.lib.deepreload` (see
    <https://github.com/ipython/ipython/issues/1626>). ~~Consider
    putting the first command into `.ipythonrc`.~~ **20130312**. Not
    into `.ipythonirc`; start-up scripts now go into a `startup/`
    directory (with `.ipy` extension) in one’s Ipython profile. I am
    using <~/.ipython/profile\_default/startup/>.

2.  ​20130218. For pasting text, use `%cpaste` now and place `--` on the
    last line to end pasted input.

3.  ​20130318. To open an editor directly within Ipython, use `edit` or
    `%edit`. To continue to work on the previous buffer, use `edit -p`
    or `%edit -p`. Use `%edit _NN` to edit the same text as input prompt
    \#NN.

[end]
