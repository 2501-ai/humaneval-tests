from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    a and b will be of the same length.

    >>> string_xor('010', '110')
    '100'
    >>> string_xor('1010101', '0101010')
    '1111111'
    >>> string_xor('1111111', '1111111')
    '0000000'
    """
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result
