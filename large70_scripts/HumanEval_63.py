def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0 
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(0)
    0
    >>> fibfib(1) 
    0
    >>> fibfib(2)
    1
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1: 
        return 0
    if n == 2:
        return 1
    
    # Initialize first three FibFib numbers
    fibfib_nums = [0, 0, 1] 
    
    # Compute remaining FibFib numbers up to n
    for i in range(3, n+1):
        next_fibfib = fibfib_nums[i-1] + fibfib_nums[i-2] + fibfib_nums[i-3]
        fibfib_nums.append(next_fibfib)

    return fibfib_nums[n]