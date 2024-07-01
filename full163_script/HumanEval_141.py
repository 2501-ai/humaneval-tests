def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    
    Examples:
    >>> file_name_check("example.txt")
    'Yes'
    >>> file_name_check("1example.dll")
    'No'
    >>> file_name_check("example1.exe")
    'Yes'
    >>> file_name_check("example1234.txt")
    'No'
    >>> file_name_check(".txt")
    'No'
    >>> file_name_check("example.")
    'No'
    >>> file_name_check("example.doc")
    'No'
    >>> file_name_check("ex.ample.txt")
    'No'
    """
    if file_name.count('.') != 1:
        return 'No'
    
    name, ext = file_name.split('.')
    
    if not name or not name[0].isalpha():
        return 'No'
    
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    digit_count = sum(c.isdigit() for c in file_name)
    
    if digit_count > 3:
        return 'No'
    
    return 'Yes'