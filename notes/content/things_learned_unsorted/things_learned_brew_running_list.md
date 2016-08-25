### Things learned, `brew`, running list

In case of errors when updating `brew`, use:

```bash
sudo chown -R `whoami` /usr/local
cd /usr/local
git add -Av .
git stash
git reset --hard
brew update
```

[end]