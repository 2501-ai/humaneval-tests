def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Examples:
        >>> even_odd_count(-12)
        (1, 1)
        >>> even_odd_count(123)
        (1, 2)
    """
    num_str = str(abs(num))  # Convert number to string and take absolute value
    evens = sum(1 for digit in num_str if int(digit) % 2 == 0)  # Count even digits
    odds = sum(1 for digit in num_str if int(digit) % 2 != 0)   # Count odd digits
    return (evens, odds)
