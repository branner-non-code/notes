## Git Merge — Dissecting Git's Guts — Emily Xie

### What makes a Git repo?

No git commands can be executed until Git has been initialized.

Content-addressable file system. 

```bash
# Simple "Hello World" in file
git hash-object -w <filename>                       # generate hash
printf "blob 13\000Hello World\041\n" | openssl sha # should give same hash

find .git/objects -type f                           # show hashes in objects/
git cat-file p <hash>                               # cats file with this hash

# A revision of the first file is the whole revision, not just a diff.

git cat-file -t <hash>                             # tells type of file (blob)
```

How does Git associate blobs with filenames, and snapshots of groups of files? With tree objects.

"Staging area" is the index of blobs to filenames.

```bash
# Plumbing commands for "add" porcelain command:
git update-index --add <filename>    # hashes will be created automatically
git ls-files --stage                 # outputs index
```

To show current tree hash: `git write-tree`. That returns a hash, and `git cat-file -p <hash>` will return the same as the `ls-files` command above.

### Commit objects

Mimic `commit` command:

```bash
# Add hash of some commit message to commit-tree.
echo "some commit message" | git commit-tree <hash>
```
# revise file
git update-index --add <file>
git write-tree # returns hash
echo "commit text" | git commit tree <hash> -p <hash2>
git cat-file -p <hash3>
# We now have tree, parent, author, and committer.

### DAG

Parents do not know their children, so there are no cycles in the Git graph. 

Also a Merkle Tree (i.e., a Merkle DAG).

### Heads

Branches are stored in `.git/refs/heads`
`git update-ref refs/heads/master <hash>` will create a text file "master" containing <hash>. This is a reference to the commit identified by <hash>.

`checkout -b <branch>` will have the same effect, adding a text file <branch>.

### How does Git know what branch we're working on?

`.git/HEAD` contains the path of the commit-file for the branch.

Detached head means the head points to a commit that is not currently pointed to by a branch.

### Git Packfiles

"Loose objects" are visible at at .git/objects. These may be packed up into a "packfile", composed of a series of deltas. We can do this manually using `git gc`.

```bash
git count-objects -H # count how many objects we have
git gc
git count-objects -H # perhaps fewer objects and smaller total now
```

Packfiles are vibisle at `.git/objects//pack/`.

### Resources

(See slides.)

[end]