# Implementation of the add_elements function

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        >>> add_elements([111,21,3,4000,5,6,7,8,9], k=4)
        24
        >>> add_elements([1,2,3,4,5], k=3)
        6
        >>> add_elements([100,200,300], k=2)
        0
        >>> add_elements([10,20,30,40,50], k=5)
        150
        >>> add_elements([99,100,101], k=1)
        99

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(x for x in arr[:k] if -99 <= x <= 99)
