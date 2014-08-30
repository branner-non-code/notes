## HomeBrew update errors

Following http://tech.nerocrux.org/2013/11/when-brew-update-is-dead/ (accessed 20140830)

On error:

```
Please, commit your changes or stash them before you can merge.
error: The following untracked working tree files would be overwritten by merge:
```

The following resets the git repository that HomeBrew pulls from:

```
cd `brew --prefix`
git remote add origin https://github.com/mxcl/homebrew.git
git fetch origin
git reset --hard origin/master
```

[end]
