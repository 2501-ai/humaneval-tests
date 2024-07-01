def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    >>> is_nested('[]')
    False
    >>> is_nested('[[][]]')
    True
    >>> is_nested('[[]][[')
    True
    >>> is_nested('[[[]]]')
    True
    >>> is_nested('[[[[]]]')
    True
    >>> is_nested('[][[[]]]')
    True
    >>> is_nested('[[[]]][]')
    True
    >>> is_nested('[[[[]]]')
    True
    >>> is_nested('[')
    False
    >>> is_nested(']')
    False
    >>> is_nested('')
    False
    >>> is_nested('[[[[[[[[')
    False
    >>> is_nested(']]]]]]]]')
    False
    >>> is_nested('[[]]]]]')
    True
    >>> is_nested('[[[]')
    True
    >>> is_nested('[[]][][]')
    True
    >>> is_nested('[[[][]][]]')
    True
    >>> is_nested('[[]][]')
    True
    >>> is_nested('[][[][]]')
    True
    >>> is_nested('[[[[]]]]')
    True
    >>> is_nested('[[[][]]]')
    True
    >>> is_nested('[[][[][]]]')
    True
    >>> is_nested('[[[][]]][[]][][[]]')
    True
    >>> is_nested('[[][]][[][]]')
    True
    >>> is_nested('[[]][[][]][]')
    True
    >>> is_nested('[[[]]][[][]]')
    True
    >>> is_nested('[[]][[]][][[]]')
    True
    >>> is_nested('[[][[]]][[]]')
    True
    >>> is_nested('[[[]]][[[]]]')
    True
    >>> is_nested('[][][][]')
    False
    >>> is_nested('[[]][[]][[]]')
    True
    >>> is_nested('[[][]][[[]]]')
    True
    >>> is_nested('[[[][]]][[]][][[]]')
    True
    >>> is_nested('[[][]][[][]]')
    True
    >>> is_nested('[[]][[][]][]')
    True
    >>> is_nested('[[[]]][[][]]')
    True
    >>> is_nested('[[]][[]][][[]]')
    True
    >>> is_nested('[[][[]]][[]]')
    True
    >>> is_nested('[[[]]][[[]]]')
    True
    >>> is_nested('[][][][]')
    False
    >>> is_nested('[[]][[]][[]]')
    True
    >>> is_nested('[[][]][[[]]]')
    True
    '''
    stack = []
    nested = False

    for char in string:
        if char == '[':
            stack.append(char)
            if len(stack) > 1:
                nested = True
        elif char == ']':
            if not stack:
                return False
            stack.pop()

    return nested and len(stack) == 0

# Running the doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()