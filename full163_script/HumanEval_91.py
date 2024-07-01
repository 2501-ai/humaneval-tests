def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    >>> is_bored("I am happy. Are you? I am excited!")
    2
    >>> is_bored("I. I? I!")
    3
    >>> is_bored("This is a test. I am testing.")
    1
    >>> is_bored("No boredom here!")
    0
    >>> is_bored("I am here. I am there. I am everywhere.")
    3
    """
    import re
    sentences = re.split(r'[.?!]', S)
    return sum(1 for sentence in sentences if sentence.strip().startswith('I'))
