def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('Abba')
    False
    """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ 
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''
        
    if is_palindrome(string):
        return string
    else:
        index = 0
        while not is_palindrome(string[index:]):
            index += 1
        return string + string[:index][::-1]