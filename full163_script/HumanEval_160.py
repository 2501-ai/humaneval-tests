def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    >>> do_algebra(['+', '*', '-'], [2, 3, 4, 5])
    9
    >>> do_algebra(['-', '//'], [10, 2, 2])
    4
    >>> do_algebra(['**', '+'], [2, 3, 4])
    12
    >>> do_algebra(['*', '+', '//'], [2, 3, 4, 2])
    8
    """
    expression = str(operand[0])
    for op, num in zip(operator, operand[1:]):
        expression += f' {op} {num}'
    return eval(expression)
