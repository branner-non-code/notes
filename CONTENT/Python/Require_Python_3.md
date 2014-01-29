## Require Python 3

At file start, use:

    import sys         
    if sys.version_info[0] < 3:                     
        sys.stdout.write('Python 3 required; exiting.')
        sys.exit(1)    

[end]
