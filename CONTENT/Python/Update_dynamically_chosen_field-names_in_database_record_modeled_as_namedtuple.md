## Update dynamically chosen field-names in database record modeled as namedtuple

~~~
from collections import namedtuple                        
'''Updating dynamically chosen field-names in namedtuple. Minimal working example.'''                                                                           
                                                          
fields = ['one', 'two', 'three']                          
Record = namedtuple('Record', fields)                     
record = Record(*tuple(['empty' for i in fields]))        
while True:                                               
    print(' 0: quit')                                     
    for i in range(len(fields)):                          
        print(' {}: {}: {}'.format(i+1, fields[i], record[i]))
    to_set = int(input('Field to set: '))                 
    if not to_set:                                        
        break                                             
    else:                                                 
        new_content = input('New content: ')              
        field_to_set = {fields[to_set-1]:new_content}     
        print('Setting', field_to_set)                    
        record = record._replace(**field_to_set)          
print('\nFinished. We have:', record) 
~~~
