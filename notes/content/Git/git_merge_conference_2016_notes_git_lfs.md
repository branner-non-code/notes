## Git Merge 2016 — Git LFS — Allen Smith loranallensmith@github.com

https://github.com/loranallensmith/manhattan-project

Every time you make a change to a large file, Git stores the change to a new object.

Git LFS doesn't write the files into repo history, but replaces them with text files that are pointers to a server containing the actual file.

```git
git lefs track <glob>
```

But you still have history that contains the huge files.

### Git internals

A series of "snapshots". 

When you `add` a file, Git creates a blob, an object written into `.git`.

On Commit, a tree object is created pointing to the blob and a commit object is created, pointing to the tree object. So to deal with big objects, we have to deal with the blobs.

Git LFS uses `clean` and `smudge` filters (preprocessors, that choose files to act on based on `.gitattributes` file) alter files on `commit` and `checkout`, respectively.

Now when you uadd a file, the blog is created but LFS creates an LFS object, storing the content locally in a special cache in `.git/lfs/objects/` and creating a text pointer that goes in the actual `.git/objects/` directory. When you push things to the remote, you are only pushing the text pointers in `.git/objects/`; you don't actually deal with the blobs unless you check out a particular commit. You don't have to grab everyting by default.

What do we do with the old objects already in the history? How do we replace them with text pointers? We use `git filter-branch` to rewrite history in a scriptable way. ("The nuclear option".) A commit re-creation automation tool.

Plan:

 1. Go back to start of project history, then for every single commit:

    2. tell Git LFS to track the correct files
    2. stage the updated `.gitattributes` file
    2. get a list of all the paths that Git LFS shold manage
    2. for each of those paths

       3. stop tracking the non-LFS version
       3. start tracking the LFS version — restage it

    2. ...

Instead of doing this manually, use the BFG repo cleaner — an alternative to git-filter-branchfocused on cleansing bad data from your repository. There is a feature to allow you to convert your repo to Git LFS.

How to use:

 1. Download BGF from https://rtyley.github.io/bfg-repo-cleaner/
 1. `git clone --mirror <url>`
 1. `cd your-repo.git`
 1. `java -jar bfg.jar --convert-to-lfs '*.psd, mp4, <etc>'`
 1. `git reflog expire --expire=now --all` # expire related trash
 1. `git gc --prune=now --aggressive`      # prune related trash
 1. `du-sh *`                              # check repo size

Beware: rewriting history affects other people who are using the same repository — use another repo, or do shallow clones of a totally revised new commit.



[end]