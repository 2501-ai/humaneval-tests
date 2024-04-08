def triples_sum_to_zero(l: list) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that 
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    l.sort()
    for i in range(len(l)-2):
        a = l[i]
        start = i+1
        end = len(l)-1
        while start < end:
            b = l[start]
            c = l[end]
            if a + b + c == 0:
                return True
            elif a + b + c < 0:
                start += 1
            else:
                end -= 1
    return False