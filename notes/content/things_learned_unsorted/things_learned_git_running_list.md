## Things Learned, Git (running list)

 1. To remove all unstaged changes:

        git clean -df
        git checkout -- .

 1. To remove any staged file:
 
        git reset <file>

 1. Rename Git branches with `git branch -m`.

 1. Git Submodule Discussion with Prasanna Swaminathan, 20150219.

   2. Branch and submodule are both pointers to single commits.
   2. When in the submodule, one sees the contents of that submodule, including the `.git` directory.
   2. When repo is cloned, submodule is not populated, although the directory for it is there. Needs `git submodule init` and `git submodule update` (can be done at clone-time with `--recursive`) to populate the submodule's particular commit. 
   2. Internally, a submodule is a detached HEAD at a particular commit.
   2. To work on a particular commit, one must first check out a particular branch. Even `master` has to be checked out.
   2. Branches are a separate structure, and as far as Prasanna knows there is no way to checkout a branch automatically.  This always has to be done manually.
   2. Subtrees are less suitable for a branch-based system, because more manual chekcout is needed.
   2. Submodule workflow:

      3. Dev and QA work on parallel repos.
      3. One is made a submodule of the other. 
      3. Submodule repo has to have last commit pushed. Either commit local changes or pull and checkout.
      3. Parent module is updated with `git submodule update`. (Prasanna is not clear on `sync`. But it seems useful if more than one remote is involved; this is not our case.)

   2. With the goal of always having QAF and dev repos on the same branch, he suggests (unfinished).
   2. DPB concludes that submodules are not the ideal infrastructure for QA-Dev parallelism.


 1. Keeping a Git fork current to changes in the original repository

    2. Have the original repo as a remote on one's local machine. The local fork is `origin remote`, the original is `upstream`.

       ```
       $ git remote -v
       origin	git@github.com:local_fork/repo.git (fetch)
       origin	git@github.com:local_fork/repo.git (push)
       upstream	git@github.com:original_version/repo.git (fetch)
       upstream	git@github.com:original_version/repo.git (push)
       ```
    
       To add the `upstream`, use
       
       ```
       git remote add upstream git@github.com:original_version/repo.git
       ```

       To pull in changes, use `git pull upstream master`.

    2. Syncing is done locally and involves git's `remote` functionality; forking is just a GitHub implementation of that, and is not part of git proper. 

 1. Getting all remote branches of a repository

    ```bash
    for b in `git branch -r | grep -v -- '->'`; do git branch --track ${b##origin/} $b; done
    git fetch --all
    git pull --all
    ```
    
    From http://stackoverflow.com/a/21189710/621762
    
    Note that the first line should only be run when there are new 

 1. Show all remote branches: `git branch -r`
 
 1. Discard all changes since last commit: `git checkout .` — this functions by "updating" all files (`.`) to match the versions in the index. This differs from `git stash` in that the `stash` is a stack of past discarded versions, and they can be recovered.

---

### Already moved to Notes on line.

(None)

[end]
