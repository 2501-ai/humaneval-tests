def remove_vowels(s: str) -> str:
    """
    Remove all vowels from the input string.

    Parameters:
        s (str): The input string from which vowels are to be removed.

    Returns:
        str: A string with all vowels removed.

    Examples:
    >>> remove_vowels('')
    ''
    >>> remove_vowels('abcdef\\nghijklm')
    'bcdf\\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = 'aeiouAEIOU'
    return ''.join(c for c in s if c not in vowels)