def is_sorted(lst):
    """
    Check if the list is sorted in non-decreasing order.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    bool: True if the list is sorted in non-decreasing order, False otherwise.
    
    Examples:
    >>> is_sorted([1, 2, 3, 4, 5])
    True
    >>> is_sorted([1, 3, 2, 4, 5])
    False
    >>> is_sorted([5, 4, 3, 2, 1])
    False
    >>> is_sorted([1, 1, 1, 1, 1])
    True
    >>> is_sorted([])
    True
    >>> is_sorted([1])
    True
    >>> is_sorted([1, 2])
    True
    >>> is_sorted([2, 1])
    False
    >>> is_sorted([-3, -2, -1, 0, 1])
    True
    >>> is_sorted([1, 2, 2, 3, 2])
    False
    >>> is_sorted([-1, 0, 1, 2, -2])
    False
    >>> is_sorted([1, 1, 1, 1, 2])
    True
    >>> is_sorted([1, 2, 3, 4, 3, 5])
    False
    >>> is_sorted([1, 2, 3, 4, 5, 5])
    True
    >>> is_sorted([1, 2, 3, 4, 5, 4])
    False
    >>> is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    True
    >>> is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    False
    >>> is_sorted([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    True
    >>> is_sorted([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    True
    >>> is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9])
    False
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

if __name__ == "__main__":
    import doctest
    doctest.testmod()