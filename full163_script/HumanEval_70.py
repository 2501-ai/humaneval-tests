def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    '''
    result = []
    lst = sorted(lst)
    while lst:
        result.append(lst.pop(0))  # Append the minimum value
        if lst:
            result.append(lst.pop(-1))  # Append the maximum value
    return result
