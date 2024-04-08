def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 2)
    '0'
    >>> change_base(0, 3)
    '0'
    """
    if x == 0:
        return '0'
    
    if base < 2 or base >= 10:
        raise ValueError(f"Invalid base: {base}. Base must be between 2 and 9.")
    
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    
    return ''.join(reversed(digits))