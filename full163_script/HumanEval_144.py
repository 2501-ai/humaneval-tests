def simplify(x, n):
    """
    Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    >>> simplify("1/5", "5/1")
    True
    >>> simplify("1/6", "2/1")
    False
    >>> simplify("7/10", "10/2")
    False
    """
    # Parse the fractions
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))

    # Calculate the product of the fractions
    product_num = num1 * num2
    product_denom = denom1 * denom2

    # Check if the product is a whole number
    return product_num % product_denom == 0
