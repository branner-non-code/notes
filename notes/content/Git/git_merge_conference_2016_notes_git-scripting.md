## Git Merge 2016 — Scripting Git, Patrick McKenna

Date: 20160405

patrickmckenna@github.com

Shell scripts for Git

 1. List new commits on a branch
 1. Run a test across a range of commits, stopping on any failure
 1. Using `libgit2` to interact directly with Git via regular languages

### What commits were added to `master` by my last `pull`?

Want to be able to use

```git
git-show-new <branch>
```

Outline:

```bash
if [ $# -ge 1 ]; then
  branch="$1"
else
  echo "git-show-new requires a branch name!"
  exit 1
fi
```

We use `git rev-list` — a fundamentally important "plumbing" command — (behind the scenes, rather than "porcelain", which is what we use on the surface)

Generates and travers commit graphs. (Commits form a directed acyclic graph, DAG.)

Use of `rev-list`

```git
git rev-list A ^B
```

Lists commits reachable from A but not from B. (A, B are anything that resolves to a commit, i.e., is "commitish"

(Slides will be available later)

Here `A` is the current commit `master` points to after `pull`; `B` is the commit master pointed to before `pull`.

TO find where master used to point, use: `master@{1}` for 1 commit previous (0 is current commit). This is the `@{...}` syntax. This command is looking up data in the reflog.

So we want:

```git
git rev-list master ^master@{1}
```

Or else use the `..` syntax:

```git
git rev-list "$branch"@{1}.."$branch"
```

Should we just output a list of SHA1s? Not informative. First, count them.

```git
git rev-list "$branch"@{1}.."$branch" | wc -l
```

To output commit info:

```git
git --no-pager log "$branch"@{1}.."$branch" --oneline
```

`oneline` prints abbreviated commit SHA1s and one-liners

So:

```bash
if [ $# -ge 1 ]; then
  branch="$1"
else
  echo "git-show-new requires a branch name!"
  exit 1
fi

printf "\n%s%s\n\n" $(git rev-list "$branch"@{1}.."$branch" | wc -l) \
  " commits were added by your last update to $branch:"
git --no-pager log "$branch"@{1}.."$branch" --oneline
```

If you weren't maintaining a local branch and only cared about the remote origin.

Notes:

 * requires an arg
 * doesn't accept multiple args
 * can be made into a Git alias:
 
   ```
   git config --global alias.show-new \
     "!f() { # contents of script go here } ; f"
   ```
   
   (semicolons instead of newlines in this case)

#### Run a test across a range of commits, stopping on any failure

(Based on @MHagger's script.)

Imagine fetching all changes and want to run regression tests.

Goal is to write:

```git
git-test-range [-k|--keep-going] RANGE -- COMMAND
```

Need to verify:

 * script is run fro inside a valid repo
 * working directory is clean

Git includes `git-sh-setup` "scriptlet" (or? "scriplet"). Meant for inclusion in other scripts — performs some useful checks and offers helper functions — good example of Git scripting, can be found on installation.

Are we running inside valid repo?

```bash
. "$(git --exec-path)/git-sh-setup"
```

To allow it to be run anywhere, set var `NONGIT_OK` first.

After sourcing script, check for clean working directory:

```git
require_clean_work_tree <command>
```

(Pass command to add comment.)

Now define function to actualy test a comit

```bash
test_rev() {
  local rev="$1"              # keward local is a Bash thing
  local command="2"           # suppress feedback messages
  git checkout -q "$rev" &&   # don't run command unless checkout successful
      eval "$command"
}
```

Now define a function to actually test a commit:

```bash
test_rev() {
  local rev="$1"             # keward local is a Bash thing
  local command="2"          # suppress feedback messages
  git checkout -q "$rev" &&  # don't run command unless checkout successful
      eval "$command"
  local retcode=$?           # shell functions can't return values, so we
  if [ $retcode -ne 0 ]      #   use return (exit) codes instead
  then
      printf "\n%s\n" "$command FAILED ON:"
      git --no-pager log -l --decorate $rev
      return $retcode        # make test_rev's return code same as command's
  fi
}
```

`$?` is the exit code of the last command that was run.

Next, we need to store the current revision, so that we can ``checkout` back to the commit we were on when we initially ran our script.

```bash
head=$(git symbolic-ref HEAD 2>/dev/null || git rev-parse HEAD)
```

`2>/dev/null` means discard any error messages; `2` is STDERR; STDIN and STDOUT have other numbers. 

The first git command here will error out and give us a non-zero return code if we run the script from a detached HEAD state; that will cause the second git command to run.

Why is `symbolic-ref` better than `git branch`? Because it's specific to whatever argument is passed to it; `git branch` returns more detail.

Next, define what we'll loop through. We already know about

 * `git rev-list`
 * specifying commit-ranges, e.g. `feature..master`

Finally, deal with test results

```bash
fail_count=0
for rev in $(git rev-list --reverse $range); do
  test_rev $rev "$command"
  retcode=$?
  if [] $retcode --eq 0 ]; then
        continue
  fi
  # ...
```

(Can't use `local` except within functions; this is not a function.)

More detail:

```bash
fail_count=0
for rev in $(git rev-list --reverse $range); do
  test_rev $rev "$command"
  retcode=$?
  if [] $retcode --eq 0 ]; then
        continue
  fi
  if [ $keep_going ]; then            # keep_going will be defined elsewhere
      fail_count=$((fail_count + 1))  # if a test fails, only continue if
      continue                        #   user chose that option
``else
      git checkout -fq ${head#refs/heads/}  # get back to where we started
      exit $retcode                         # otherwise HEAD detached
  fi
done
git checkout -fq ${head#refs/heads/}  # 
```

(In `head#refs/heads/`, remember `head` is a variable we defined earlier.)

We've skipped a few things:

 * input args
 * printing out final results

Complete version of this script at https://git.io/vVgTY.

Question: what about `git bisect` — runs binary search within a commit-range.

(Interesting pointer used on slides: app called "mouseposé".)

### Using `libgit2` + language-bindings

Problems arise with scripting when:

 * tasks are complicated
 * more features are desired
 * scale — "shelling out to Git" can get expenseive

`libgit2`:

 * pure C implementation of Git core methods (Git is mostly C but some shell and some PErl)
 * bindings for Python, Ruby, Node.JS, Go, ...
 * well-established and actively matained OSS project with wide industry support (though technically not part of the Git project)

Today we will use `rugged`, the Ruby binding. Need system tools `cmake` and `pkg-config`.

(break to download things and ask question)

`Rugged::Object` is the main class.

Primary interface to local Git repos: `Rugged::Repository`. 

Git has 4 fundamental object types:

 * blog
 * tree
 * commit
 * tree
 
Rugged has a corresponding class for each. (As does each other language-binding.)

`libgit2` can also be used from within the C API, to embed for best performance.

This is based on `git-httpd` by @carlosmn.

Let's build a Git-backed we server. Serve content directly from the Git object store (.git directory).  No need to checkout files onto disk. 

Example use case: Locally deploy one branch that needs a web server (e.g. `gh-pages`), while you work on another.

Use gems `mime` and `sinatra` (builds web servers). 

```ruby
require 'sinatra'
require 'rugged'
require 'mime/types'     # We use mime just in order to have types.
```

Must specify repo, branch (ref); must create repo object. Below, hard-code for simplictiy, but ideally we would use command line arguments or user input:

```ruby
repo_path = ENV['HOME'] + '/PATH/TO/REPO'
ref_name = 'refs/remotes/REMOTE/BRANCH'

repo = Rugged::Repository.new(repo_path)
```

Now use Sinatra to start defining how our server responds to GET requests

```ruby
get '*' do |path|                     # Sinatra GET method
  commit = repo.ref(ref_name).target
  path.slice!(0)                      # strip leading slash
  path = 'index.html' if path.empty?  # Default if no path passed in.
  # ...
```

Use supplied path to retrieve associated Git tree entry.

```ruby
entry = commit.tree.path path             # entry is a Ruby hash
puts path
blob = repo.lookup entry[:oid]           # oid is object ID
content = blob.content                   # return actual blob-content as string
halt 404, "404 not found" unless content
```

Whole thing:

```ruby
require 'sinatra'
require 'rugged'
require 'mime/types'     # We use mime just in order to have types.

repo_path = ENV['HOME'] + '/PATH/TO/REPO'
ref_name = 'refs/remotes/REMOTE/BRANCH'

repo = Rugged::Repository.new(repo_path)

get '*' do |path|                     # Sinatra GET method
  commit = repo.ref(ref_name).target
  path.slice!(0)                      # strip leading slash
  path = 'index.html' if path.empty?  # Default if no path passed in.

  entry = commit.tree.path path             # entry is a Ruby hash
  puts path
  blob = repo.lookup entry[:oid]           # oid is object ID
  content = blob.content                   # return actual blob-content as string
  halt 404, "404 not found" unless content
  
  content_type MIME::Types.type_for(path).first.content_type
``content
```

This script at https://git.io/vVgJp.

There are other bindings on the same @carlosmn site.

`libgit2` includes functionality not available on command line.

Q: What can you do in a detached head? You must be in detached head to rebase, for instance.

patrickmckenna@github.com

[end]