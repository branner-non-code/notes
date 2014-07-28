## Matplotlib installation

 1. 20140125: Installation with pip fails when some `freetype` contents are not found.

    Solution Create symbolic link to freetype2 (following http://stackoverflow.com/a/20576003/621762 on 20140125): 
    
        sudo ln -s /usr/local/opt/freetype/include/freetype2 /usr/local/include/freetype

[end]
