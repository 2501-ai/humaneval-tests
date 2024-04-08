import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ 
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(xs, x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x 
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    a, b = -1e9, 1e9
    fa, fb = poly(xs, a), poly(xs, b)
    
    while (b-a) > 1e-9:
        m = (a+b)/2
        fm = poly(xs, m)
        
        if fm == 0:
            return m
        if fa*fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
            
    return (a+b)/2