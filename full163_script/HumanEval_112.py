def reverse_delete(s, c):
    """
    Task
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)

    >>> reverse_delete("abcde", "ae")
    ('bcd', False)
    >>> reverse_delete("abcdef", "b")
    ('acdef', False)
    >>> reverse_delete("abcdedcba", "ab")
    ('cdedc', True)
    """
    # Remove characters from s that are in c
    result = ''.join([char for char in s if char not in c])
    # Check if the result is a palindrome
    is_palindrome = result == result[::-1]
    return (result, is_palindrome)
