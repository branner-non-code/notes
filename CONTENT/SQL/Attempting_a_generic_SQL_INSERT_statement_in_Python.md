## Attempting a generic SQL INSERT statement in Python

I am working with SQLite3 in Python but am not yet at the stage of using an ORM such as SQLAlchemy. But I had the idea that I could save trouble by writing a function to produce INSERT statements generically — without having to write them out manually.

Below is what I came up with.

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
    # field_ordereddict is ordered dictionary of 'fieldname':fieldname
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
