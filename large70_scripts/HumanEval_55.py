def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    Args:
        n (int): The index of the Fibonacci number to return.
        
    Returns:
        int: The n-th Fibonacci number.
        
    Examples:
        >>> fib(0) 
        0
        >>> fib(1)
        1
        >>> fib(2)
        1
        >>> fib(3)
        2
        >>> fib(10) 
        55
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b