## Keep a Git fork current with the origin

1. Want to contribute to https://github.com/nltk/nltk

1. Go there and click Fork. 

1. Clone to my local environment with 

        git clone git@github.com:brannerchinese/nltk.git 

1. Inside clone, run 

        git branch -a

   which shows:

        * develop
          remotes/origin/HEAD -> origin/develop
          remotes/origin/align
          remotes/origin/brill
          remotes/origin/develop
          remotes/origin/py25

   meaning:

     2. presently on local master branch (indicated by asterisk);
     2. there is also remote master branch belonging to the remote named "origin", which is the "remotes/origin/master" entry. 

1. Now `less .git/config` shows local master branch:

        [remote "origin"]
                url = git@github.com:brannerchinese/nltk.git
                fetch = +refs/heads/*:refs/remotes/origin/*

1. To pull any changes made since creation of the fork, run

        git remote add nltk git@github.com:nltk/nltk.git

   Now less .git/config shows

        [remote "nltk"]
                url = git@github.com:nltk/nltk.git
                fetch = +refs/heads/*:refs/remotes/nltk/*

1. To fetch and merge any new changes made in nltk, run 

        git pull nltk <branch_I_want_to_merge_into>

[end]
