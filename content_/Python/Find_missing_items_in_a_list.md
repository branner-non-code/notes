Find missing items in a list
----------------------------

​20130313. Subtract the set of items from the set of expected items:

    missing = set(list_items) - set(stats_wanted)
    if missing:
        print("Cannot identify tag(s): {}".format(', '.join(missing))) 

[end]
