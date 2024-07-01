def encode_shift(s: str) -> str:
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    >>> encode_shift("abc")
    'fgh'
    >>> encode_shift("xyz")
    'cde'
    >>> encode_shift("hello")
    'mjqqt'
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str) -> str:
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    >>> decode_shift("fgh")
    'abc'
    >>> decode_shift("cde")
    'xyz'
    >>> decode_shift("mjqqt")
    'hello'
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
