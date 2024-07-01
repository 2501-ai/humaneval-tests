def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Examples:
    >>> starts_one_ends(1)
    1
    >>> starts_one_ends(2)
    18
    >>> starts_one_ends(3)
    180
    >>> starts_one_ends(4)
    1800
    """
    if n == 1:
        return 1
    return 18 * 10**(n-2)
