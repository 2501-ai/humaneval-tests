def search(lst: list) -> int:
    '''
    Finds the greatest integer in the list whose frequency is greater than or equal to the value itself.

    Args:
        lst (list): A non-empty list of positive integers.

    Returns:
        int: The greatest integer meeting the criteria, or -1 if no such integer exists.

    Examples:
        >>> search([4, 1, 2, 2, 3, 1])
        2
        >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
        3
        >>> search([5, 5, 4, 4, 4])
        -1
    '''
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    
    candidates = [num for num, freq in counts.items() if freq >= num]
    
    if not candidates:
        return -1
    else:
        return max(candidates)