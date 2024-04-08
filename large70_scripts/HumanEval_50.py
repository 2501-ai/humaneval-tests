def encode_shift(s: str) -> str:
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    encoded = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                encoded += chr(((ord(ch) + 5 - ord('A')) % 26) + ord('A'))
            else:
                encoded += chr(((ord(ch) + 5 - ord('a')) % 26) + ord('a'))
        else:
            encoded += ch
    return encoded


def decode_shift(s: str) -> str:
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    decoded = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                decoded += chr(((ord(ch) - 5 - ord('A')) % 26) + ord('A'))
            else:
                decoded += chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a'))
        else:
            decoded += ch
    return decoded