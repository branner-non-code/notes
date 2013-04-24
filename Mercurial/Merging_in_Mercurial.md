Merging in Mercurial
====================

With Vim
--------

Following http://mercurial.selenic.com/wiki/MergingWithVim, add the following to `~/.hgrc`:

        [ui]
        merge = vimdiff
        
        [merge-tools]
        vimdiff.executable = vim
        vimdiff.args = -d $base $local $output $other +close +close

[end]
