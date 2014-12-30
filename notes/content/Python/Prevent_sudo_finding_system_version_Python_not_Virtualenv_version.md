## Prevent `sudo` from finding system version of Python rather than Virtualenv version

Comment out `secure_path` in the `sudoers` file in Ubuntu, to prevent `sudo` from finding the system version of Python rather than the one in the virtualenv.

[end]
