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

**Output**

~~~
In [1]: run test_setattr_namedtuple
Editing... done. Executing edited code...
 0: quit
 1: one: empty
 2: two: empty
 3: three: empty
Field to change: 2
New content: qwer
Setting {'two': 'qwer'}
 0: quit
 1: one: empty
 2: two: qwer
 3: three: empty
Field to change: 3
New content: sjkfdgj;fdgs
Setting {'three': 'sjkfdgj;fdgs'}
 0: quit
 1: one: empty
 2: two: qwer
 3: three: sjkfdgj;fdgs
Field to change: 0

Finished. We have: Record(one='empty', two='qwer', three='sjkfdgj;fdgs')

In [2]: 
~~~
