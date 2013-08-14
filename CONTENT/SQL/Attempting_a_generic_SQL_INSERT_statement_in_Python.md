## Attempting a generic SQL INSERT statement in Python

I am working with SQLite3 in Python but am not yet at the stage of using an ORM such as SQLAlchemy. But I had the idea that I could save trouble by writing a function to produce INSERT statements generically — without having to write them out manually.

Below is what I came up with.

### Most current version (as of 20130813)

See later sections for evolution of what I have built.

~~~
def generic_insert(table_name, list_of_fields, cursor, timestamp_id):          
    '''Inserts into a given table                                              
     * a list of tuples (field, value; not a plain list!) and                  
     * a timestamp.                                                            
    The timestamp is added to the list of tuples with field-name "timestamp_id".
    '''     
    # Note that it is not time-efficient to construct the INSERT statement     
    # without the use of format(); a limited run of 72K records was slower this
    # way by 0.8 second; a limited run of 72K records was slower this way by   
    # 10%.  
    #    the_string = ('''INSERT INTO ''' + table_name + ''' (''' +            
    #    field_names + ''') VALUES (''' + question_marks + ''');''')           
    list_of_fields.append(('timestamp_id', timestamp_id))                      
    # Since we are using a list of tuples rather than a dictionary, we need our
    # own lists of keys and values.                                            
    keys = [i[0] for i in list_of_fields]                                      
    values = [i[1] for i in list_of_fields]                                    
    # Begin constructing the SQL string as a list of integers converted to     
    # strings. This will become the core of a string.format() element.         
    the_string = [str(i) for i in range(1, len(list_of_fields)+1)]             
    # Prepare replacement fields for SQL field names, using the list of        
    # integers.                                                                
    the_string = '{' + '},{'.join(the_string) + '}'                            
    # Prepare question marks for VALUES                                        
    question_marks = '?' + ',?' * (len(list_of_fields) - 1)                    
    # Construct string                                                         
    field_names = ','.join(keys)                                               
    the_string = ('''INSERT INTO {0} (''' + the_string + ''') VALUES (''' +    
            question_marks + ''');''')                                         
    # Populate the finished string with the name of the table and the keys (=
    # fields).
    the_string = the_string.format(table_name, *tuple(keys))
    # Populate the SQL statement with the values (replacing question-marks).   
    try:
        cursor.execute(the_string, tuple(values))
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        # This error normally means duplicate entry, which can be ignored.
        # There is normally no need for action unless other unexplained
        # problems occur.
        # So instead we manually look up the desired ID number and return it.
        return generic_get_id(table_name, list_of_fields, cursor)
                           
def get_row_count(table_name, cursor): 
    '''Generic function to return row count for a given table.'''              
    row_count = cursor.execute( '''SELECT max(rowid) FROM {};'''.              
            format(table_name))
    return row_count.fetchall()[0][0]  
                               
def generic_get_id(table_name, list_of_field_value_tuples, cursor):            
    '''Returns the ID of a given record in a given table.'''                   
    keys = [i[0] for i in list_of_field_value_tuples]
    values = [i[1] for i in list_of_field_value_tuples]
    the_string = [str(i) for i in range(1, len(list_of_field_value_tuples)+1)] 
    the_string = '{' + '}=? AND {'.join(the_string) + '}=?'
    the_string = ('''SELECT id FROM {0} WHERE ''' + the_string + ';')          
    the_string = the_string.format(table_name, *tuple(keys))                   
    id = cursor.execute(the_string, tuple(values))                             
    return id.fetchall()[0][0] 
~~~

Apparently SQLite3 allows field names to be inserted using `format()`, just not values. That permits the use of generic `INSERT` and `SELECT` statements, in which the field names are added dynamically.

### An example of my original inline INSERT statements

~~~
try:
    cursor.execute('''
            INSERT INTO kanji (kanji_traditional, kanji_simplified, time_of_commit) 
            VALUES (?,?,?)''', (kanji_traditional, kanji_simplified, timestamp))
except sqlite3.IntegrityError as e:
    print(e, '\n  with {0} and {1}'.format(kanji_traditional, kanji_simplified))
    raise CustomException()
~~~

### The same insertion carried out by a generic function

~~~
kanji_fields = OrderedDict((
        ('kanji_traditional', kanji_traditional),
        ('kanji_simplified', kanji_simplified),
        ('time_of_commit', timestamp)
        ))
insert(cursor, 'kanji', kanji_fields)
~~~

### The `insert()` function called above

~~~
class CustomException(Exception):
    pass

def insert(cursor, table_name, field_ordereddict, raise_error_or_not=True):
    '''
    Constructs and executes generic INSERT function.
    
    Notes on parameters: 
    "cursor" is instantiated as:
    
        con = sqlite3.connect(<database>)
        with con:
            cursor = con.cursor()
    
    and passed to this function.
    
    "table_name" is the name of the table in <database> 
    where INSERT is to take place
    
    "field_ordereddict" is a collections.OrderedDict of 
    (field_name, field_contents) tuples. The field_name keys populate the 
    arguments of the INTO expression and the field_contents values populate the
    arguments of the VALUES expression.
    
    "raise_error_or_not" is used to decide whether or not to log details about 
    a sqlite3.IntegrityError and then raise a CustomException or not.
    '''

    the_string = [str(i) for i in range(1, len(field_ordereddict)+1)]
    # prepare replacement fields for SQL field names
    the_string = '{' + '},{'.join(the_string) + '}'
    # prepare question marks for VALUES
    question_marks = '?' + ',?' * (len(field_ordereddict) - 1)
    # construct string
    the_string = ('''INSERT INTO {0} (''' + the_string + ''') VALUES (''' + 
            question_marks + ''')''')
    the_string = the_string.format(table_name, *tuple(field_ordereddict.keys()))
    # execute as cursor.execute(the_string, *tuple(field_ordereddict.values()))
    try: 
        cursor.execute(the_string, tuple(field_ordereddict.values()))
    except sqlite3.IntegrityError as e:
        if raise_error_or_not:
            print(e, 'at {}'.format(tuple(field_ordereddict.values())))
            raise CustomException()
        else:
            pass
~~~

### Results

1. **Virtues**. Chiefly modularity and readability. This design worked, and I was able to replace a number of long, messy inline INSERT statements with neat `insert()` calls. 

   A second benefit was that my herding of field-names and their contents was made more readable through use of the `OrderedDict` data structure.

2. **Drawbacks**. However, The time required increased by a factor of 3.2, which I judge fatal to my project. 

3. **Going forward**. Using `OrderedDict` to keep field-names and their contents organized improved readability:

        kanji_fields = OrderedDict((
                ('kanji_traditional', kanji_traditional),
                ('kanji_simplified', kanji_simplified),
                ('time_of_commit', timestamp)
                ))
        try:
            cursor.execute('''
                    INSERT INTO kanji ({0},{1},{2}) VALUES (?,?,?)'''.
                    format(*tuple(kanji_fields.keys())),
                    tuple(kanji_fields.values()))
        except sqlite3.IntegrityError as e:
            print(e, '\n  with {0} and {1}'.format(kanji_traditional, kanji_simplified))
            raise CustomException()

   But this is a scant improvement in speed over the `insert()` function — 2.9 times the running time of explicit in-line INSERT statements. Probably it is the use of `str.format()` expressions that is costing some of this extra time.
   
   Test of same:

        $ python -m timeit "s = '{0} {1} {2} {3} {4} {5} {6}'.format('never', 'use', 'the', 'number', 'forty-two', 'in', 'examples')"
        1000000 loops, best of 3: 0.712 usec per loop
        $ python -m timeit -s "words = ('never', 'use', 'the', 'number', 'forty-two', 'in', 'examples')" "s = '{0} {1} {2} {3} {4} {5} {6}'.format(*words)"
        1000000 loops, best of 3: 0.667 usec per loop
        $ python -m timeit "s = 'never use the number forty-two in examples'"
        10000000 loops, best of 3: 0.0206 usec per loop
        $

    In fact, an `OrderedDict` is really an enormous luxury as compared with, say, a list of tuples:
    
        $ python -m timeit -s "from collections import OrderedDict" "s = OrderedDict((('a', 1), ('b', 'ship'), ('c', 5.11)))"
        100000 loops, best of 3: 13.5 usec per loop
        $ python -m timeit -s "from collections import OrderedDict" "s = [('a', 1), ('b', 'ship'), ('c', 5.11)]"
        10000000 loops, best of 3: 0.117 usec per loop

    Replacing `OrderedDict`s with lists of tuples was much faster — only 1.4 times the running time of explicit in-line SQL:
    
        kanji_fields = [
                ('kanji_traditional', kanji_traditional),
                ('kanji_simplified', kanji_simplified),
                ('time_of_commit', timestamp)
                ]
        try:
            cursor.execute('''
                    INSERT INTO kanji ({0},{1},{2}) VALUES (?,?,?)'''.
                    format(*tuple(i[0] for i in kanji_fields)),
                    tuple(i[1] for i in kanji_fields))
        except sqlite3.IntegrityError as e:
            print(e, '\n  with {0} and {1}'.format(kanji_traditional, kanji_simplified))
            raise CustomException()

   This may prove to be the ideal mixture of modular neatness and speed (definition adjusted for the Python environment).
