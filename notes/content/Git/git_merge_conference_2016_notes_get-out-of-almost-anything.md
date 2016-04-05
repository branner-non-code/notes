## Git Merge 2016 — Get Out of (Almost) Anything — Allen Smith loranallensmith@github.com

Repo at https://github.com/loranallensmith/oopsy

Git keeps almost everything.

How does Git store work?

It stores every version of very file, as snapshots. 

Options for fixing errors:

 * Undo a single commit:
 
   `git revert <commit>`

 * Amend the most recent unpushed commit:

   ```bash
   git rm --cached <name>
   git commit --amend
   ```

 * Restore clean copies of particular files before commit:

   ```bash
git checkout -- <list of files>
```

 * Restore clean copies of particular files after commit:
 
   ```bash
git reset --hard <tree-ish>
```

   Mixed and soft reset also exist; q.v.

 * In case of severe reset errors.
 
   Tracks where pointers have pointed — after hard reset, the removed commits still exist but are no longer directly accessible. The reflog can still show that these commits were pointed to at previous states of HEAD.
 
   ```bash
   git reflog
   ```
   
   Warnings:
   
   * Reflog is local only.
   * Reflog have an expiration date (90 days?), which can be changed.
   * Orphaned commits don't show up in reflog until pruned, which may happen automatically.

 * In case of committing to `master`:
 
   ```bash
   git branch <new branch>
   git reset --hard origin/master
   ```

 * I want to branch but `master` keeps changing

   Use rebase
   
   ```bash
   git rebase master
   ```
   
   Or you can `git merge master`.
   
   There is also an interactive rebase:
   
   ```bash
   git rebase --interactive <tree-ish>
   ```

 * Forgot to stage something belonging in a particular commit

   ```bash
   git commit --fixup=<commit>
   git rebase --autosquash -i
   ```

### Getting input from others

Version control is the story of what you built. There are two approaches to this:

 * historian's approach — every detail — sometimes required by auditors
 * raconteur's approach — cleaner history — the essence of how the code was made

### Git log usage:

```bash
git log --oneline # terse log output
git log --patch   # show patch-diffs for each commit
```


[end]