def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    >>> right_angle_triangle(3, 4, 5)
    True
    >>> right_angle_triangle(1, 2, 3)
    False
    >>> right_angle_triangle(5, 12, 13)
    True
    >>> right_angle_triangle(6, 8, 10)
    True
    >>> right_angle_triangle(7, 24, 25)
    True
    >>> right_angle_triangle(10, 6, 8)
    True
    >>> right_angle_triangle(1, 1, 1)
    False
    '''
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
