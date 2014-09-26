## Encrypting files in a Git repo

 1. Use [`git blur`](https://github.com/acasajus/git-blur). 
   2. Initialize with `git blur init`, which solicits a password, which it stores in the configuration file `.git/blur.conf`
   2. Accepts globbed names of files to be encrypted in `.gitattributes`.
 
 1. See also `[git crypt](https://github.com/AGWA/git-crypt)`, which is more straitforwardly GPG based. (See docs at https://www.agwa.name/projects/git-crypt/.)

[end]
