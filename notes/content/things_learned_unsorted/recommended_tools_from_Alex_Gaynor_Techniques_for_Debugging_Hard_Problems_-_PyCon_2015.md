## Alex Gaynor - Techniques for Debugging Hard Problems - PyCon 2015

https://www.youtube.com/watch?v=ij99SGGEX34

### Recommended tools

 * lab notebook (DPB already uses in the form of Markdown notes)
 * observe sys calls: `strace` (Linux), `dtrace` (OS X)
 * debugger: `pdbpp`
 * other tools

   * `lsof`: list open files, show file descriptors
   * `netstat`: show what different network sockets are pointing to ("show network status")
   * `htop`, `iotop`: CPU, disk, and RAM usage; ("display top disk I/O events by process")
   * `proc`
   * `osquery` (due to Facebook)
   * `fork`: "create a new process"
   * `exec`
   * `posix-spawn`

 * pair debugging: discuss what you each think; often reconciliation is needed
 * minimization: dpb: like MWE; as few moving parts as possible; reduce number of interactions between elements.
 * `git bisect`: narrow down which commit introduced a bug
 * "When you're not engaged in one of these hideously complex debugging sessions, you should always be doing constant clean-up of your code-base. When you're actually in the thick of it, you don't don't want to be distracted by random broken things that are not the broken thing you're looking for. Complex system failures are almost never caused by a single thing being broken. They're caused by a series of smaller, interconnected failures. If you fix the small failures early, you can avoid [their interactions] with other things being large and complex."
 

[end]
