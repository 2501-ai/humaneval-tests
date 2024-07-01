def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    >>> flip_case('Hello')
    'hELLO'
    >>> flip_case('WORLD')
    'world'
    >>> flip_case('Python3.8')
    'pYTHON3.8'
    >>> flip_case('')
    ''
    """
    return string.swapcase()
