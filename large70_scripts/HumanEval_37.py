def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal 
    to the values of the even indices of l, but sorted.
    >>> sort_even([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> sort_even([5, 6, 3, 4, 1, 2])
    [1, 6, 3, 4, 5, 2]
    """
    even_elems = sorted(l[::2])
    odd_elems = l[1::2]
    
    result = [None]*(len(even_elems)+len(odd_elems))
    result[::2] = even_elems
    result[1::2] = odd_elems
    
    return result