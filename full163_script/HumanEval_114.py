def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    
    Examples:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    >>> minSubArraySum([1, -1, -2, 1])
    -3
    >>> minSubArraySum([3, -4, 2, -3, -1, 7, -5])
    -6
    """
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return min_sum
