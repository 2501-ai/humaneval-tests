def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    largest_factor = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            largest_factor = factor
        else:
            factor += 1
    if n > 1:
        largest_factor = n
    return largest_factor
