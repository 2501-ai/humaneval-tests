def median(l: list) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    8.0
    >>> median([1, 2, 3, 4])
    2.5
    """
    l_sorted = sorted(l)
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return (l_sorted[mid - 1] + l_sorted[mid]) / 2
    else:
        return l_sorted[mid]