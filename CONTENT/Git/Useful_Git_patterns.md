## Useful git patterns

### Working in general

 1. To find out what has been staged:

        git diff --cached

   or, for a graphic version:

        git gui

 1. To find out what has been changed:

        git diff

 1. To find out what is changed and staged:

        git status

 1. To find out, but only as a dry run, what will be staged:

        git add -Avn .

 1. To retrieve remote content without automatically merging:

        git fetch
        git fetch --dry-run -v

   The latter is the most explicit.

### Working with branches and merging

 1. To create a new branch:

        git branch branch_name

 1. To list all branches, including remotes:

        git branch -a

 1. To find out how the current branch differs from the remote master:

        git diff remotes/origin/master

   or

        git diff remotes/origin/master..current_branch

 1. To work within an existing branch or to return to the master branch:

        git checkout branch_name
        git checkout master

 1. To push or pull the commits within a branch to or from repo:

        git push -u origin branch_name
        git pull origin branch_name

   Before pulling for the first time, make sure to create and check out the desired branch.

 1. To find out what differs between two branches:

        git diff --name-status master..branch_name

 1. To merge only a selected file from another branch into the current branch

        git checkout branch_name -- file_name

 1. To merge but without automatic commit:

        git merge --no-commit branch_name
        git status

   Git now shows successful auto-merges as `modified` and unsuccessful ones as `both modified`. Inspect the successful merges with

        git diff --cached file_name

   This file can still be edited, saved, and committed locally. But to choose one or the other version, use one of the two following commands:

        git checkout HEAD file_name
        git checkout branch_name file_name

### Terms

 1. **detached HEAD**: HEAD refers to a specific commit that is not necessarily the same as **master**.

[end]
