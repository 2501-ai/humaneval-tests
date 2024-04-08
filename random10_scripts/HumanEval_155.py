def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)

    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """
    num = abs(num)  # Handle negative numbers
    num_str = str(num)
    evens = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odds = len(num_str) - evens
    return (evens, odds)