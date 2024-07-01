def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    8.0
    >>> median([1, 2, 3, 4])
    2.5
    >>> median([1, 2, 3])
    2
    >>> median([1])
    1
    >>> median([1, 2])
    1.5
    """
    l = sorted(l)
    n = len(l)
    mid = n // 2
    if n % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2
    else:
        return l[mid]
