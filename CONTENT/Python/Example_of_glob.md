## Example of glob module

~~~
# delete_goangyunn_line_in_file.py
# David Prager Branenr
# 20130603, works                                                               
''' Open files and if first line starts with 廣韻 then delete first line and
then save.'''    
                 
import os, glob  
import re        
                 
def main():      
    for filename in glob.iglob('*.wenlin'):
        print('  trying', filename, end='')
        with open(filename, 'r', encoding="utf-16") as f:
            content = f.read()
        if '廣韻' in content:
            content = re.sub('^廣韻.+?\n', '', content)
            with open(filename, 'w', encoding="utf-16") as f:
                f.write(content)
            print('  found in', filename)
~~~

[end]
