def pluck(arr: list) -> list:
    """
    Finds and returns the node with the smallest even value from the array.
    If multiple nodes have the same smallest even value, returns the one with the smallest index.
    Returns an empty list if no even values are found, or the array is empty.

    >>> pluck([4,2,3])
    [2, 1]
    >>> pluck([1,2,3])
    [2, 1]
    >>> pluck([])
    []
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    """
    if not arr:
        return []
    
    min_even_val = float('inf')
    min_even_idx = -1
    
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < min_even_val:
            min_even_val = num
            min_even_idx = i
    
    if min_even_idx == -1:
        return []
    else:
        return [min_even_val, min_even_idx]