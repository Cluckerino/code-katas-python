"""
Find the n-smallest elements and spit them in original order.
http://www.codewars.com/kata/n-smallest-elements-in-original-order/python
http://www.codewars.com/kata/n-smallest-elements-in-original-order-performance-edition/python
"""


def get_val(tup):
    """Get the value from an index-value pair"""
    return tup[1]


def first_n_smallest(arr, n_count):
    """Return the n_count smallest numbers from arr in the original order they were in."""
    # Strategy:
    # 1. Iterate through the array, grabbind data as index-value pair.
    # 2. Add items to n_list until it contains n_count. Keep n_list sorted by value.
    # 3. For the rest of the values, if the new value is smaller than max value in n_list, replace
    #    it with new_value. Keep n_list sorted by value.
    # 4. Sort n_list by index and then grab the values.
    n_list = []
    if n_count == 0:
        return n_list
    for ind_val_pair in enumerate(arr):
        if len(n_list) < n_count:
            n_list.append(ind_val_pair)
            n_list.sort(key=get_val)
        else:
            if get_val(n_list[-1]) > get_val(ind_val_pair):
                n_list.pop()
                n_list.append(ind_val_pair)
                n_list.sort(key=get_val)
    n_list.sort()
    return [get_val(t) for t in n_list]


def performant_smallest(x_vals, n_count):
    """
    Return the n_count smallest numbers from arr in the original order they were in. 
    A much faster version for large inputs.
    """
    # Spoiled answer by Unnamed
    # See: https://www.codewars.com/kumite/5aef9594de4c7f11cc0002a8
    # Strategy:
    # 1. Copy input (x_vals) into a sorted list (y_vals)
    # 2. Trim y_vals to n_count items
    # 3. Memoize the max (max_val) and count how many times it appears in y_vals (k_max_val). This
    #    is done just in case the max_value appears more times in the list than is needed for the
    #    result.
    # 4. Iterate through original array, appending all values <= max_val to the list. Use
    #    k_max_val to count if value = max_val
    if n_count == 0:
        return []
    y_vals = sorted(x_vals)
    del y_vals[n_count:]
    max_val = y_vals[-1]
    k_max_val = y_vals.count(max_val)
    result = []
    for x_val in x_vals:
        if x_val <= max_val:
            if x_val < max_val:
                result.append(x_val)
            elif k_max_val > 0:
                result.append(x_val)
                k_max_val -= 1
    return result
