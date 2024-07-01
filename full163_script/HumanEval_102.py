# Implementation of the choose_num function

def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    >>> choose_num(12, 15)
    14
    >>> choose_num(13, 12)
    -1
    >>> choose_num(8, 10)
    10
    >>> choose_num(7, 7)
    -1
    >>> choose_num(6, 6)
    6
    """
    if x > y:
        return -1
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num
    return -1
