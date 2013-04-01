Python
======

Comprehensions
--------------

1.  ​20130220. Discussion with Zach: As for why comprehensions are
    favored, he says they are more declarative — closer to abstract
    statements than to procedural “constructions”. He agrees with my
    prediction that the ability to read them fluently will come with
    practice writing them.

2.  ​20130220. General format. Original:

        for item in container:
            list.append(object) # or
            set.add(object)

    Replacement:

        list/set = [object for item in container]

    where `container` is a sequence, mapping, or set and `container2` is
    a sequence or mapping. Another case:

        for key in container:
            mapping[key] = value

    Replacement:

        mapping = {key : value for for key in container}

    where `container` is a sequence, mapping, or set and `container2` is
    a sequence or mapping.

3.  First case. Original:

            for row_dict in data:
                line_for_table = []
                row_dict = format_data(row_dict)
                # create list of items to go into line of .tex table
                for item in list_items:
                    line_for_table.append(row_dict[item])
                line_for_table = [row_dict[item] for item in list_items]
                running_tex_str += ' & '.join(line_for_table) + '\\\\ \hline\n'

    Replacement:

            for row_dict in data:     
                row_dict = format_data(row_dict)                       
                # create list of items to go into line of .tex table   
                line_for_table = [row_dict[item] for item in list_items]
                running_tex_str += ' & '.join(line_for_table) + '\\\\ \hline\n'         

    The reason the second for loop can’t be removed the same way, into a
    nested comprehension, is that other statement occur than merely
    those populating the list.

4.  Second case. Original

                # Next: build dictionary for each "item"              
                #   and append to list full_data                      
                one_row_dict = {}                                                       
                for i in range(len(list_items)):
                    # Strip quotes while adding item to one_row_dict
                    one_row_dict[list_items[i]] = one_row[i].strip('"')

    Replacement:

                # Next: build dictionary for each "item"              
                #   and append to list full_data                      
                #   also, strip quotes while adding item to one_row_dict   
                one_row_dict = {list_item: row_item.strip('"')        
                        for list_item, row_item in zip(list_items, one_row)}

5.  ​20130313. Tuple by comprehension: make tuple of list comprehension:

        In [39]: listy = [i for i in range(10)]
        In [40]: tuple([i for i in listy])
        Out[40]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

Compression
-----------

​20130320. If I am compressing whole web pages, there is a significant
savings in using `bz2`. But if I am isolating the Chinese to compress,
the compressed form is actually longer (as a bytecode string) than the
original unicode string! However, the compressed form is smaller on
disk.

Directory navigation
--------------------

​20130220. Use `os.path.join` to ensure that the code works on all
operating systems.

    with open(os.path.join('CODE', 'file_end.tex'), 'r') as f:                  
            running_tex_str += f.read()

Find missing items in a list
----------------------------

​20130313. Subtract the set of items from the set of expected items:

    missing = set(list_items) - set(stats_wanted)
    if missing:
        print("Cannot identify tag(s): {}".format(', '.join(missing))) 

Name of active function
-----------------------

20130327.

    import inspect
    inspect.stack()[0][3]

Nonetype
--------

​20130313. `”` is not the same as `None`. Use the latter in `return`
statements unless an actual string is required.

Python date objects
-------------------

1.  ​20130305. Use `D.timedelta()` to calculate days between dates:

        import datetime as D
        def make_date_obj(date):
            return D.date(int(date[0:4]), int(date[5:7]), int(date[8:]))

        today = D.date.today()
        today - D.timedelta(days_back) # produces date object for a date ``days_back'' back

2.  ​20130305. Produce sequence of dates up to `days_back` days back:

        days_of_history = 7
        for days_back in range(0, days_of_history):
            the_date = today - D.timedelta(days_back)

3.  ​20130319. Time elapsed as H:MM:SS.ssssss:

        datetime.timedelta(seconds=time.time() - start_time)

Printing delays
---------------

1.  ​20130319. I found some `print` output within a `try`-`except`
    block, itself within a `for` loop, itself within a *with* block, was
    being delayed by many minutes, and I fixed it by the use of

        sys.stdout.flush()

Random lists of characters
--------------------------

1.  ​20130311. I had thought of specifying a range of codepoints and
    converting them to characters:

        chr(R.randint(32, 126))

    which works well for Chinese. But Marek changed that to this, which
    is better for ASCII:

        R.choice(string.ascii_letters)

    I wrote a piece of code to time the two:

        def both(x):
            start = T.time()
            for i in range(x):
                a = R.choice(string.ascii_letters)
            print('R.choice(string.ascii_letters)', T.time() - start)
            start = T.time()
            for i in range(x):
                a = chr(R.randint(32, 126))
            print('chr(R.randint(32, 126))', T.time() - start)

        In [21]: both(10000000)
        R.choice(string.ascii_letters) 69.98532509803772
        chr(R.randint(32, 126)) 109.04312491416931

    Marek’s is much faster.

[end]
