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

[end]
