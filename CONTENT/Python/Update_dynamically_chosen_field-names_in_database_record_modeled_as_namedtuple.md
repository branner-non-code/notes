## Update dynamically chosen field-names in database record modeled as namedtuple

~~~
from collections import namedtuple          
'''Updating dynamically chosen field-names in database record modeled as namedtuple. Minimal working example.'''
                                            
fields = ['one', 'two', 'three']            
Record = namedtuple('Record', fields)       
record = Record(*tuple(['empty' for i in fields]))       
while True:                                 
    print(' 0: quit')                       
    for i in range(len(fields)):            
        print(' {}: {}: {}'.format(i+1, fields[i], record[i]))
    to_change = int(input('Field to change: '))
    if not to_change:                       
        break                               
    else:                                   
        new_content = input('New content: ')
        field_to_change = {fields[to_change-1]:new_content}
        print('Setting', field_to_change)   
        record = record._replace(**field_to_change)                             
print('\nFinished. We have:', record)       
~~~
