Directory navigation
--------------------

​20130220. Use `os.path.join` to ensure that the code works on all
operating systems.

    with open(os.path.join('CODE', 'file_end.tex'), 'r') as f:                  
            running_tex_str += f.read()

[end]
