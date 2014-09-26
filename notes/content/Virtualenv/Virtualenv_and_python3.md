## Virtualenv and Python3

[20140926: There is useful information at http://hackercodex.com/guide/python-development-environment-on-mac-osx/.]

 1. To install for use with Python3:
 
   2. Make sure there is a current version of Python3 available on the computer. If this is being done after OS re-installation, Python3 may not be available; use `brew install python3` in that case.
   2. That version will supply `pip3`. Use regular `pip` to uninstall any previous versions of `virtualenv`, then use

        ```
pip3 install -U virtualenv
        ```

     to be sure of getting a version fully compatible with Python3.

 1. To ensure Python3 support, use

        virtualenv v_env3 --python=python3

   or 

        virtualenv v_env3 --python=python3.4

[end]
