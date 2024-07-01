def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    >>> order_by_points([123, 234, 345, 456])
    [123, 234, 345, 456]
    >>> order_by_points([10, 20, 30, 40])
    [10, 20, 30, 40]
    >>> order_by_points([5, 15, 25, 35])
    [5, 15, 25, 35]
    >>> order_by_points([-5, -15, -25, -35])
    [-5, -15, -25, -35]
    >>> order_by_points([0, 0, 0, 0])
    [0, 0, 0, 0]
    >>> order_by_points([111, 222, 333, 444])
    [111, 222, 333, 444]
    >>> order_by_points([10, 2, 30, 4])
    [2, 10, 4, 30]
    >>> order_by_points([102, 21, 13, 31])
    [21, 102, 13, 31]
    """
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    # Create a list of tuples (digit_sum, original_index, number)
    indexed_nums = [(digit_sum(num), idx, num) for idx, num in enumerate(nums)]
    
    # Sort based on digit sum first, then by original index if digit sums are equal
    sorted_nums = sorted(indexed_nums, key=lambda x: (x[0], x[1]))
    
    # Extract only the numbers from the sorted list
    return [num for _, _, num in sorted_nums]

# Additional doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()