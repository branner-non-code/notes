## Git remove from repo not from directory

### By unstaging

 1. To unstage a file after adding but before committing:

        git reset HEAD <file>
        
 1. For explicit response, use `-q`

### By use of `.gitignore`

 1. Remove file
 2. Add `file` to `~/.gitignore`
 3. Use `git config --global core.excludesfile ~/.gitignore` to respect `.gitignore` globally.

[end]
