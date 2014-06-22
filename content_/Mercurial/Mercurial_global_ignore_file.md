Mercurial global files
======================


Global .hgrc
------------

 1. Place this in `$HOME/`. Include:

        [ui]
        verbose = True
        editor = vim
        merge = vimdiff
        ignore = ~/.hgignore
        
        [merge-tools]
        vimdiff.executable = vim
        vimdiff.args = -d $base $local $output $other +close +close
        
        [extensions]
        progress =
        
        [progress]
        delay = 0

 1. Other `.hg/hgrc` content in local repos will add to or override this.

Global .hgignore
----------------

 1. Place reference in global `.hgrc` as

        [ui]
        ignore = ~/.hgignore

 1. Currently (20130609) using: 
 
        use glob to specify files not to be tracked
        syntax: glob
        
        # vim temporary files
        **.swp
        
        # EMACS and Vim temporary files
        **~
        
        # LaTeX temporary files
        **.synctex.gz
        **.aux
        
        # OS X metadata store
        **.DS_Store
        
        # Python compiled flle
        **.pyc
        
        # Don't need to upload this each time
        **last_content.txt
        
        # Leave Eclipse metadata out.
        **.metadata
        
        # Any virtual environment.
        **v_env3/*
        **v_env2/*
        **v_env27/*
        
        # Any .git or .hg directory
        **.git/*
        **.hg/*


[end]
