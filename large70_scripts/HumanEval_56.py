def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    count = 0
    for char in brackets:
        if char == '<':
            count += 1
        elif char == '>':
            if count == 0:
                return False
            count -= 1
    return count == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()