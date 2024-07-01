def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    
    # Define the vowels and their replacements
    vowels = 'aeiouAEIOU'
    replacements = 'CGKQWcgkqw'
    
    # Swap case and replace vowels
    result = []
    for char in message:
        if char in vowels:
            result.append(replacements[vowels.index(char)])
        else:
            result.append(char.swapcase())
    
    return ''.join(result)
