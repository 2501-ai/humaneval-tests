def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count
