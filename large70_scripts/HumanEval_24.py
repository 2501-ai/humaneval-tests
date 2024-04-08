def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    >>> largest_divisor(12) 
    6
    >>> largest_divisor(13)
    1
    """
    for i in range(n//2, 0, -1):
        if n % i == 0:
            return i
    return 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()