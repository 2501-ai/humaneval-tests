def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    largest_prime = 1
    i = 2
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 1
    
    if n > 1:
        largest_prime = n
        
    return largest_prime