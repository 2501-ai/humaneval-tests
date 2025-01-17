def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4])
    -9
    >>> prod_signs([0, 1])
    0
    >>> prod_signs([]) is None
    True
    """
    if not arr:
        return None
    product_of_signs = 1
    sum_of_magnitudes = 0
    for num in arr:
        if num > 0:
            sign = 1
        elif num < 0:
            sign = -1
        else:
            sign = 0
        product_of_signs *= sign
        sum_of_magnitudes += abs(num)
    return sum_of_magnitudes * product_of_signs

if __name__ == "__main__":
    import doctest
    doctest.testmod()
