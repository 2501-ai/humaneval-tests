def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('abc', 'abc') 
    1
    >>> how_many_times('abaabaca', 'aba')
    2
    """
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start) 
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count