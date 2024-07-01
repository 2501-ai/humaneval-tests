def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    
    For example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """
    result = []
    for char in s:
        new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
        result.append(new_char)
    return ''.join(result)

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
