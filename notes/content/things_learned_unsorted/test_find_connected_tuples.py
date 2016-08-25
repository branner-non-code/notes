#! /usr/bin/env python
# test_find_connected_tuples.py
# David Branner
# 20150611

import itertools
import os
import pytest
import random
import uuid
import sys

import find_connected_tuples

RANGE = 100

################################################
# Parametrize test_resolve_pairs_into_sets_01
argvalues = [random.randint(1, RANGE) for _ in range(RANGE)]
################################################

@ pytest.mark.parametrize('number_of_sets', argvalues=argvalues,
        ids=['number_of_sets: {}'.format(item) for item in argvalues])
def test_resolve_pairs_into_sets_01(number_of_sets):
    """Test: fn reassembles sets of linked items from collection of tuples."""
    # Use `while True` to ensure all items are unique.
    while True:
        # Generate list of lists of different cardinality.
        # Start with sets to eliminate duplicates.
        list_of_sets = [set([str(uuid.uuid4())
                for _ in range(number_of_sets)])
                for member in range(number_of_sets)]
        list_of_lists = sorted([sorted(list(item)) for item in list_of_sets])

        # Combine these sublists into one list and ensure that all are unique.
        all_in_one_list = list(itertools.
                chain.from_iterable(list_of_lists))
        if len(set(all_in_one_list)) == len(all_in_one_list):
            break

    # Make separate list of 2-tuples for each set.
    list_of_pair_tuples = []
    for member in list_of_lists:
        list_of_pair_tuples.extend(itertools.combinations(member, 2))
    random.shuffle(list_of_pair_tuples)

    assert (find_connected_tuples.find_connected_tuples(list_of_pair_tuples) ==
            list_of_lists)
