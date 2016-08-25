#! /usr/bin/env python
# find_connected_tuples.py
# David Branner
# 20150611

def find_connected_tuples(tuples):
    """Take a list of 2-tuples; return list of lists of connected items.
    
    Being "connected" means tuples share at least one item.
    
    Return value is sorted lists of sorted lists, for easy comparison.
    """
    # Use a dictionary to assemble all in-tuple contacts of each element.
    # This dictionary's many redundancies to be eliminated in the second part.
    redundant_keys = dict()
    for t in tuples:
        first = t[0]
        second = t[1]
        
        # Construct set of all linked elements, for each element.
        if first in redundant_keys:
            redundant_keys[first].add(second)
        else:
            redundant_keys[first] = {first, second}
        if second in redundant_keys:
            redundant_keys[second].add(first)
        else:
            redundant_keys[second] = {first, second}
    
    # Eliminate redundancies.
    # Merge ("compact") any sets that have any shared items.
    compacted_sets = []
    while redundant_keys:
        # Remove kv_pair one by one from redundant_keys
        kv_pair = redundant_keys.popitem()
        value = set(kv_pair[1])

        # We keep the whole value portion to return later.
        compacted_sets.append(value)

        # Examine each element of that value portion;
        #  union that element's own value-set to our current value set
        #  and then remove that element as a key from redundant_keys
        #  so it isn't dealt with again; its values are all now in our
        #  current value portion, which will be returned.
        for item in value:
            if item in redundant_keys:
                kv_pair[1].update(redundant_keys[item])
                del redundant_keys[item]
        compacted_sets[-1].update(kv_pair[1])

    # Convert the whole to a sorted list of sorted lists, for easy comparison.
    return sorted([sorted(list(item)) for item in compacted_sets])

