# Converting list to set

If the list contains sublists, Python3 will raise `TypeError: unhashable type: 'list'`. 

Convert the sublists to tuples (they can be converted back after the use of `set`).

A list of lists can be converted to a tuple of tuples with

    tuple(tuple(a_list) for a_list in list_of_lists)

[end]
