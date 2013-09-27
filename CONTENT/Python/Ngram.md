## Python ngram module

### package 

 https://pypi.python.org/pypi/ngram

### docs 

 http://pythonhosted.org/ngram/

### discussion of faster tools

 http://stackoverflow.com/questions/7591258/fast-n-gram-calculation}

### Use in two-stage substring search

20130529: results of experiment show me that this module is much slower for two-stage substring search than ordinary `find()`.

```
# compare_find_and_ngram_search.py
# David Prager Branner
# 20130529

import timeit
import os
import random
import ngram
import time
import pprint

'''Test whether a randomly selected substring can be found using ngram.search.

It doesn't look as though this works for this purpose very well.

In [288]: C.main(5,100000)
Using ngram module
100000 successes; 0 failures
time: 63.43151116371155

Using strings only
100000 successes; 0 failures
time: 19.7869770526886

In [290]: C.main(8,100000)
Using ngram module
100000 successes; 0 failures
time: 81.43729996681213

Using strings only
100000 successes; 0 failures
time: 22.63141393661499

In [291]: C.main(2,100000)
Using ngram module
100000 successes; 0 failures
time: 44.72568202018738

Using strings only
100000 successes; 0 failures
time: 14.986773014068604

'''

filename = 'mencius_text_from_ctext.org_20130522_text_only_punctuation_simplified_one_line_per_line.txt'

with open(os.path.join('DATA', filename), 'r') as f:
    content = f.read()
phrases = content.splitlines()
M = ngram.NGram(phrases, N=2)

def get_random_string(string_len = 2):
    random_phrase = ''
    while len(random_phrase) <= string_len:
        random_phrase = phrases[random.randint(0, len(phrases)-1)]
    string_number = random.randint(0, len(random_phrase) - string_len)
    random_string = random_phrase[string_number : (string_number + string_len)]
    return random_string

def main(string_len = 2, iterations = 100):
    print('Using ngram module')
    successes = 0
    start_time = time.time()
    for i in range(iterations):
        to_find = get_random_string(string_len)
        strings_where_found = M.search(to_find)
        for j in strings_where_found:
            if to_find in j[0]:
                successes += 1
 #               print('{0}: {1:.3f}, {2}'.  format(to_find, j[1], j[0]))
                break
    end_time = time.time()
    print(successes, 'successes;', iterations-successes, 'failures')
#        string_where_found = M.find(to_find)
#        if string_where_found.find(to_find) == -1:
#            counter += 1
#            print('{0:.3f}: {1} in {2}'.
#                    format(M.compare(to_find, string_where_found), to_find,
#                    string_where_found))
    print('time:', end_time - start_time)
    print('\nUsing strings only')
    successes = 0
    start_time = time.time()
    for i in range(iterations):
        to_find = get_random_string(string_len)
        strings_where_found = phrases
        for j in strings_where_found:
            if to_find in j:
                successes += 1
                break
    end_time = time.time()
    print(successes, 'successes;', iterations-successes, 'failures')
    print('time:', end_time - start_time)


```

[end]
