def triangle_area(base: float, height: float) -> float:
    """
    Calculates the area of a triangle given the length of the base and height.
    
    Args:
        base (float): The length of the base of the triangle
        height (float): The height of the triangle
        
    Returns:
        float: The area of the triangle
        
    Example:
        >>> triangle_area(5, 3) 
        7.5
    """
    area = (base * height) / 2
    return area