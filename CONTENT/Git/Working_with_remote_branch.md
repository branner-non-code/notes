## Working with a remote branch

### Check out the remote branch

Assuming a remote branch `development`:

~~~
git checkout -b development origin/development
~~~

### Populate the new remote branch from the remote repo

~~~
git fetch development
~~~

After that, you can use `pull` and `push` normally.

[end]
