Git
===

Commands
--------

1.  ​20130214. `git add -A` is comparable to `hg addr`~~, but one seems
    to need to add `-r *` in order to cover everything. Needs more
    research~~.

2.  ​20130214. `git stash` discards current contents and allows next
    pull to replace current contents.

3.  ​20130311. `git pull <url>`: adds someone else’s pulled version of
    my repo to my own repo.

Useful adjunct programs
-----------------------

1.  ​20130219. `tig` or other commit browser to examine current
    repository.

2.  ​20130219. `tree`: Command-line program to show directory structure;
    useful for `.git`.

Organization
------------

1.  Git stores all content in the `objects/` directory.

2.  Repository history is a graph of commits — each one can point to
    previous commits. They are identified by `SHA1` hashes.

3.  A Git branch is simply a reference to a SHA1 hash that refers to a
    particular commit.

4.  A “commit” is essentially just a snapshot of the current local
    repository.

5.  `checkout`: create a new branch, starting at the repository state at
    the moment of checkout — all that is done is that the original
    commit’s hash is saved to `.git/res/heads/branches`.

    1.  `git checkout master`: restores you to master

    2.  `git checkout -b name`: creates a new branch, “`name`”

    3.  Checking out a raw SHA1 creates a “detached head”.

6.  `.git/HEAD` keeps track of which commit is the current one at which
    we are located.

7. **20130331**. Renaming a file so that only capitalization changes is not reflected in repo. Following [http://stackoverflow.com/a/10523903/621762], first rename to a temporary name and then back to the newly capitalized form. In addition, used setting 

    git config core.ignorecase false

to ensure that Git recognizes case changes. But this alone is not enough to ensure that the earlier name is deleted from the repo!

[end]

