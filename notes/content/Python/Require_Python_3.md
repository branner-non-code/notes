## Require Python Version 3

At file start, use:

    import sys
    if sys.version_info[0] < 3:
        sys.stdout.write('Python 3 required; exiting.')
        sys.exit()

[end]
