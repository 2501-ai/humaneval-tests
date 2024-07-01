def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>>")
    False
    """
    balance = 0
    for bracket in brackets:
        if bracket == '<':
            balance += 1
        elif bracket == '>':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0
