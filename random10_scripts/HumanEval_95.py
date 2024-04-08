def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty or contains any non-string keys.
    
    Examples:
    >>> check_dict_case({"a":"apple", "b":"banana"})
    True
    >>> check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) 
    False
    >>> check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
    False
    >>> check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
    False
    >>> check_dict_case({"STATE":"NC", "ZIP":"12345" })
    True
    >>> check_dict_case({})
    False
    >>> check_dict_case({"a":1, "b":2})
    True
    >>> check_dict_case({1:1, 2:2})
    False
    """
    if not dict:
        return False
    
    keys = dict.keys()
    
    if not all(isinstance(k, str) for k in keys):
        return False
    
    all_lower = all(k.islower() for k in keys)
    all_upper = all(k.isupper() for k in keys)
    
    return all_lower or all_upper

if __name__ == "__main__":
    import doctest
    doctest.testmod()