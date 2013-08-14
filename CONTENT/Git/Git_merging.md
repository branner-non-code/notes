## Git merging

 1. In branch `dev`
 2. Commit and push
 3. `git checkout master`: switches to `master`
 4. `git merge dev`: brings `master` parallel to `dev`
 5. `git branch -d dev`: deletes `dev` locally
 6. `git push origin :dev`: deletes `dev` at the origin
 7. `git push`: pushes all commits from the `merge` to the origin
 
 8. If a new branch is created locally, push to the remote repo with `git push -u origin dev`

[end]
