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

[end]
