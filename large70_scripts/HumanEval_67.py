def fruit_distribution(fruits_string: str, total_fruits: int) -> int:
    """
    Calculates the number of mango fruits in a basket given the total 
    number of fruits and the number of apples and oranges.
    
    Args:
        fruits_string (str): A string expressing the number of apples and oranges, 
            e.g. "3 apples and 5 oranges".
        total_fruits (int): The total number of fruits in the basket.
    
    Returns:
        int: The number of mango fruits in the basket.
    
    Example:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 orange", 3)
        2
        >>> fruit_distribution("2 apples and 3 oranges", 100)
        95
    """
    # Extract the number of apples and oranges from the string
    fruit_counts = [int(s) for s in fruits_string.split() if s.isdigit()]
    
    # Sum up the number of apples and oranges
    apples_oranges_total = sum(fruit_counts)
    
    # Subtract from the total to get the number of mangoes
    mango_count = total_fruits - apples_oranges_total
    
    return mango_count