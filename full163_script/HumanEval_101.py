def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

    >>> words_string("Hi, my name is John")
    ['Hi', 'my', 'name', 'is', 'John']
    >>> words_string("One, two, three, four, five, six")
    ['One', 'two', 'three', 'four', 'five', 'six']
    >>> words_string("apple, banana, cherry")
    ['apple', 'banana', 'cherry']
    >>> words_string("dog cat bird")
    ['dog', 'cat', 'bird']
    >>> words_string("hello,world")
    ['hello', 'world']
    >>> words_string("a,b,c,d,e")
    ['a', 'b', 'c', 'd', 'e']
    >>> words_string("one two three four")
    ['one', 'two', 'three', 'four']
    >>> words_string(" ")
    []
    >>> words_string(",,,,")
    []
    """
    import re
    return [word for word in re.split(r'[ ,]+', s.strip()) if word]
