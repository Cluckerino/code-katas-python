"""
Array folding kata.
https://www.codewars.com/kata/fold-an-array/python
"""

import itertools
import math


def fold_array_once(array):
    """Fold an array once"""
    # Left bound
    l_bound = math.ceil(len(array) / 2)
    l_array = array[0:l_bound]
    r_array = array[-1:l_bound-1:-1]
    return [sum(t) for t in itertools.zip_longest(l_array, r_array, fillvalue=0)]


def fold_array(array, runs):
    """Fold an array for the given number of runs."""
    output = list(array)
    for _ in range(0, runs):
        output = fold_array_once(output)
    return output
