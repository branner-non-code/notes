## Find User Name within Python

    import pwd, os
    pwd.getpwuid(os.getuid())[0]

This returns the actual user name. If run with root privleges, returns `root`.

[end]
