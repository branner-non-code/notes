## Pushing to multiple Git repos simultaneously

To `.git/config` add:

```
[remote: "all"]
        url = <url of first repo>
        url = <url of second repo>
      <etc.>
```

Note that there is still only one `[remote: "origin"]` that can be pulled from, but other repos can be pushed to.

[end]
