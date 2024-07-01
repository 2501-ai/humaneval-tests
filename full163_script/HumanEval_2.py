def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(4.123)
    0.123
    >>> truncate_number(10.999)
    0.999
    >>> truncate_number(0.456)
    0.456
    >>> truncate_number(100.0)
    0.0
    """
    return round(number - int(number), 10)
