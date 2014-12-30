## Python: find currently logged-in user

To get the currently logged-in user, use:

    import subprocess
    subprocess.check_output(['who', '-m']).split()[0]

[end]
