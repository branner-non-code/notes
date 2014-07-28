## Pushing to multiple Git repos simultaneously

### Remote "all"

To `.git/config` add:

```
[remote: "all"]
        url = <url of first repo>
        url = <url of second repo>
        <etc.>
```

Note that there is still only one `[remote: "origin"]`, but other repos can be pushed to and pulled from.

To push to all (apparently the default):

```
git push all
```

### Mirror

You can also add a mirror repo:

```
[remote "<name>"]
        url = <url of repo>
        fetch = +refs/*:refs/*
```

In case changes have been made there, pull from it using:

```
git pull <name> master
```

[end]
