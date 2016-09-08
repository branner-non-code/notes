## Function to convert Markdown to HTML with `grip`

Install `grip` on OS X with Homebrew. It is currently (20160908) the best free tool for this purpose.

```bash
function dpb_grip {
  grip $1.md --export $1.html
}
```

[end]