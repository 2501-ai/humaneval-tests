def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [5, -3, -4]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    >>> maximum([-3, -4, 5], 3)
    [-4, -3, 5]
    >>> maximum([4, -4, 4], 2)
    [4, 4]
    >>> maximum([-3, 2, 1, 2, -1, -2, 1], 1)
    [2]
    """
    return sorted(sorted(arr, reverse=True)[:k])
