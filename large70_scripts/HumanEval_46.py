def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0 
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    
    Examples:
    >>> fib4(5)
    4
    >>> fib4(6) 
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError(f'n must be >= 0, got {n}')
    
    # Handle base cases
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2
    
    # Use dynamic programming to compute fib4(n)
    # Store previously computed values to avoid recomputation
    dp = [0] * (n+1)
    dp[2] = 2
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
    
    return dp[n]