def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two strings contain the same set of unique characters.
    
    Args:
        s0 (str): The first string to compare.
        s1 (str): The second string to compare.
        
    Returns:
        bool: True if s0 and s1 contain the same set of characters, False otherwise.
        
    Examples:
        >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
        True
        >>> same_chars('abcd', 'dddddddabc') 
        True
        >>> same_chars('dddddddabc', 'abcd')
        True
        >>> same_chars('eabcd', 'dddddddabc')
        False
        >>> same_chars('abcd', 'dddddddabce') 
        False
        >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
        False
    """
    # Convert strings to sets to get unique characters 
    set0 = set(s0)
    set1 = set(s1)
    
    # Check if the sets are equal
    return set0 == set1