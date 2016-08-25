## Things Learned, Python (running list)

### Python

 1. To list all available modules:

        help('modules')

 1. Recommended directory structure for a Python project by [Jean-Paul Calderone ](http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html).

 1. `pyvenv` replaces `virtualenv`. https://docs.python.org/3/library/venv.html

 1. To test `ipython` run `iptest`.

---

### Already moved to Notes on line.


 1. To display the "caller" of function or method, use `inspect.stack()[1][3]`.

 1. To get the currently logged-in user, use:
         
        import subprocess
        subprocess.check_output(['who', '-m']).split()[0]

 1. In Python `subprocess`, don't use `Popen.check_output` if there are pipes; intead use `Popen.communicate`.
 1. Comment out `secure_path` in the `sudoers` file in Ubuntu, to prevent `sudo` from finding the system version of Python rather than the one in the virtualenv.


 1. On office machine, Pytest tests of `thin_dict` do not find the module in question, even though on Ubuntu Mint and home OS X installations there is no such problem. Test file had included line

        sys.path.append('..')

   which should have been sufficient to locate the module. Following http://stackoverflow.com/a/10253916/4363116, replaced that line with

        import sys, os
        myPath = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, myPath + '/../')

   and all was well.

[end]
