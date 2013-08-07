## Git managing deleted and moved files

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

### Removal or moving of already tracked files

~~~
git add -u <path>
~~~

will note the disappearance of those files from their original path, and

~~~
git add <path>
~~~

will note their appearance somewhere else.

But there doesn't seem to be a one-step equivalent to Mercurial's `addr` command.

[end]
