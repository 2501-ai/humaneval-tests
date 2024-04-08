def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists.
    
    Args:
        l1 (list): First input list.
        l2 (list): Second input list.
        
    Returns:
        list: Sorted list of unique common elements.
        
    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2]) 
        [2, 3]
    """
    # Find the intersection of two lists using set intersection
    common_elements = list(set(l1) & set(l2))
    
    # Return the sorted list of common elements
    return sorted(common_elements)


if __name__ == "__main__":
    # Run doctest
    import doctest
    doctest.testmod()