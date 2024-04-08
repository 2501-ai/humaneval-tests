def digitSum(s: str) -> int:
    """
    Computes the sum of the ASCII codes of uppercase characters in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of uppercase characters in s.
    
    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    uppercase_sum = 0
    for char in s:
        if char.isupper():
            uppercase_sum += ord(char)
    return uppercase_sum