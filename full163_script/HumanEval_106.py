def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]

    >>> f(5)
    [1, 3, 6, 24, 15]
    >>> f(3)
    [1, 3, 6]
    >>> f(0)
    []
    >>> f(1)
    [1]
    """
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def sum_to(x):
        return x * (x + 1) // 2

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:  # even index
            result.append(factorial(i))
        else:  # odd index
            result.append(sum_to(i))
    return result
