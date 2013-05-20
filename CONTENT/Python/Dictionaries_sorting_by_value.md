## Sort Python dictionary by value

### Program to count the Chinese characters (only) in a file and return their overall percentages

~~~
import os
import re  
import operator                                                 
import math
  
# Hanzi only 
to_delete = ('''[^\u3300-\u9fff\uf900-\ufaff\U00020000-\U0002fa1f]''')
  
def main(filename):
   '''count the Chinese characters (only) in a file and return their overall percentages'''
    with open(os.path.join('DATA', filename), 'r') as f:        
        content = f.read()                                      
    content = re.sub(to_delete, '', content)                    
    number_characters = len(content)                            
    character_count = {i:0 for i in set(content)}               
    for i in content:                                           
        character_count[i] += 1                                 
    character_percents = {i:(math.trunc(10000 * character_count[i] / 
            number_characters) / 100) for i in set(content)}    
    content = (''.join('{}\t{}\n'.format(key, val) for key, val in 
            sorted(character_percents.items(), key=operator.itemgetter(1), 
            reverse=True)))
    with open(os.path.join('DATA', filename.replace('.txt', '_percents.txt')),
            'w') as f:
        f.write(content)

~~~
