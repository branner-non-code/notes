## Python: better solution for sys.path.append 

On office machine (2014 December), Pytest tests of `thin_dict` do not find the module in question, even though on Ubuntu Mint and home OS X installations there is no such problem. Test file had included line
 
    sys.path.append('..')
 
 which should have been sufficient to locate the module. Following http://stackoverflow.com/a/10253916/4363116, replaced that line with:
 
    import sys, os
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')
 
and all was well.

[end]
