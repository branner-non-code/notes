## Git managing deleted and moved files

### Removal and addition of already-tracked files

~~~
git add -u <path>
~~~

will note the disappearance of those files from their original path, and

~~~
git add <path>
~~~

will note their appearance somewhere else.

### Moving an already-tracked file within a repo

~~~
git add -A <path>
~~~

This is a one-step equivalent to Mercurial's `addr` command.

### To unstage a file after adding but before committing

~~~
git reset HEAD <file>
~~~

The manpage for `git-reset` explains: "`git reset <paths>` is the opposite of `git add <paths>`."

### To unstage and remove a file only from the index 

~~~
git rm -f --cached <file>
~~~

### To compare current and cached versions of a file

~~~
git diff --cached <file>
~~~

[end]
