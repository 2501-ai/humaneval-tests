def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for x in l:
        if x >= t:
            return False
    return True