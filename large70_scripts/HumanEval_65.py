def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer to circular shift
        shift (int): The number of positions to shift the digits right
        
    Returns:
        str: The circular shifted integer as a string
        
    Examples:
        >>> circular_shift(12345, 1) 
        '51234'
        >>> circular_shift(12345, 2)
        '45123'
        >>> circular_shift(12345, 3)
        '34512'
        >>> circular_shift(12345, 4)  
        '23451'
        >>> circular_shift(12345, 5)
        '12345'
        >>> circular_shift(12345, 6) 
        '54321'
    """
    x_str = str(x)
    n = len(x_str)
    
    if shift > n:
        return x_str[::-1]
    else:
        shift = shift % n
        return x_str[-shift:] + x_str[:-shift]


if __name__ == '__main__':
    import doctest
    doctest.testmod()