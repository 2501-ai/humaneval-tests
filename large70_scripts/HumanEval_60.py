def sum_to_n(n: int) -> int:
    """
    Computes the sum of numbers from 1 to n.
    
    Args:
        n (int): The number to sum up to.
    
    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n(5) 
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(100)
        5050
    """
    return sum(range(1, n+1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()