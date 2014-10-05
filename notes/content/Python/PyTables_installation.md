## PyTables Installation

Using `pip`, even following many published suggestions, generated errors on Mac OS 10.9.5 with Python 3 (Python 2 also failed). The following worked:

```
brew install hdf5
virtualenv v_env3 --python=python3
. v_env3/bin/activate
pip install ipython numpy scipy matplotlib numexpr
pip install --upgrade git+git://github.com/cython/cython@master

# Downloaded from http://sourceforge.net/projects/pytables/?source=typ_redirect
# cd into directory
# following http://pytables.github.io/usersguide/installation.html
python setup.py build --hdf5=/usr/local/Cellar/HDF5/1.8.13
python setup.py install --hdf5=/usr/local/Cellar/HDF5/1.8.13
```

Then
```
ipython
Python 3.4.1 (default, Sep 26 2014, 13:38:30) 
Type "copyright", "credits" or "license" for more information.

IPython 2.3.0 -- An enhanced Interactive Python.

...

In [1]: import tables

In [2]: tables.test()

...

FAILED (errors=2)
Out[2]: 1
```

On the need for `hdf5`, see https://www.underworldproject.org/documentation/HDF5Download.html.

[end]
