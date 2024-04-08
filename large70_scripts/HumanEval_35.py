def max_element(l: list) -> int:
    """Return maximum element in the list.
    
    Args:
        l (list): Input list
    
    Returns:
        int: Maximum element in the list
        
    Examples:
        >>> max_element([1, 2, 3]) 
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:
        raise ValueError("max_element() arg is an empty list")
    
    max_val = l[0]  # initialize max to first element
    for x in l:
        if x > max_val:
            max_val = x
    return max_val