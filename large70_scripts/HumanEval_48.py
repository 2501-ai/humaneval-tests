def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    A palindrome is a string that reads the same forward and backward.
    This function compares the original string to its reverse and returns 
    True if they are equal, False otherwise.

    Parameters:
    text (str): The input string to check 

    Returns:
    bool: True if the string is a palindrome, False otherwise

    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba') 
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Compare the original string to its reverse 
    return text == text[::-1]