import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n

    >>> poly([1, 2], 3)  # 1 + 2*3
    7.0
    >>> poly([0, 0, 1], 2)  # x^2 for x=2
    4.0
    >>> poly([1, -1, 1], 1)  # 1 - 1 + 1
    1.0
    >>> poly([1, 0, -1], 2)  # 1 - 4
    -3.0
    >>> poly([1], 5)  # Constant polynomial
    1.0
    >>> poly([], 2)  # No coefficients
    0.0
    >>> poly([1, 2, 3], 0)  # 1 + 2*0 + 3*0^2
    1.0
    >>> poly([1, 2, 3], -1)  # 1 - 2 + 3
    2.0
    >>> poly([1, 2, 3], 1.5)  # 1 + 2*1.5 + 3*1.5^2
    10.75
    >>> poly([0, 0, 0], 100)  # Zero polynomial
    0.0
    >>> poly([1, 1, 1, 1], 2)  # 1 + 2 + 4 + 8
    15.0
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)]) if xs else 0.0


def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    >>> round(find_zero([1, -3, 2]), 2)  # (x - 1)(x - 2) = x^2 - 3x + 2
    1.0
    >>> round(find_zero([2, -4, 2]), 2)  # 2(x - 1)^2 = 2x^2 - 4x + 2
    1.0
    >>> round(find_zero([1, 0, -1]), 2)  # x^2 - 1 = (x - 1)(x + 1)
    1.0
    >>> round(find_zero([1, 0, 0, -1]), 2)  # x^3 - 1 = (x - 1)(x^2 + x + 1)
    1.0
    >>> round(find_zero([0, 1]), 2)  # x = 0
    0.0
    >>> round(find_zero([1, 0, 0, 0, -1]), 2)  # x^4 - 1 = (x - 1)(x + 1)(x^2 + 1)
    1.0
    >>> round(find_zero([1, 0, 0, 0, 0, -1]), 2)  # x^5 - 1 = (x - 1)(x^4 + x^3 + x^2 + x + 1)
    1.0
    >>> round(find_zero([1, 0, 0, 0, 0, 0, -1]), 2)  # x^6 - 1 = (x - 1)(x^5 + x^4 + x^3 + x^2 + x + 1)
    1.0
    >>> round(find_zero([1, 0, 0, 0, 0, 0, 0, -1]), 2)  # x^7 - 1 = (x - 1)(x^6 + x^5 + x^4 + x^3 + x^2 + x + 1)
    1.0
    >>> round(find_zero([1, 0, 0, 0, 0, 0, 0, 0, -1]), 2)  # x^8 - 1 = (x - 1)(x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1)
    1.0
    >>> round(find_zero([1, -1]), 2)  # x = 1
    1.0
    >>> round(find_zero([1, -2, 1]), 2)  # (x - 1)^2 = x^2 - 2x + 1
    1.0
    >>> round(find_zero([1, -5, 6]), 2)  # (x - 2)(x - 3) = x^2 - 5x + 6
    2.0
    """
    def derivative(xs: list, x: float) -> float:
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

    x = 1.0  # Better initial guess
    for _ in range(100):  # Limit iterations to avoid infinite loop
        fx = poly(xs, x)
        if abs(fx) < 1e-7:  # Considered as zero
            return x
        dfx = derivative(xs, x)
        if dfx == 0:  # Avoid division by zero
            x += 1.0  # Adjust guess if derivative is zero
            continue
        x -= fx / dfx
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()