def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello') 
    'hELLO'
    >>> flip_case('wORLD')
    'World'
    >>> flip_case('12345')
    '12345'
    >>> flip_case('')
    ''
    """
    flipped = []
    for char in string:
        if char.islower():
            flipped.append(char.upper())
        elif char.isupper():
            flipped.append(char.lower())
        else:
            flipped.append(char)
    
    return ''.join(flipped)

if __name__ == '__main__':
    import doctest
    doctest.testmod()