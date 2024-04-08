import math

def triangle_area(a: float, b: float, c: float) -> float:
    '''
    Calculates the area of a triangle from side lengths using Heron's formula.

    Args:
        a (float): Length of side a.
        b (float): Length of side b. 
        c (float): Length of side c.

    Returns:
        float: Area of the triangle rounded to 2 decimal points, or -1 if invalid.

    Examples:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # Check if the sides form a valid triangle
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Calculate semi-perimeter
        s = (a + b + c) / 2
        
        # Calculate area using Heron's formula 
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        return round(area, 2)
    else:
        return -1