def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.

    >>> encode_cyclic('abcdef')
    'bcaefd'
    >>> encode_cyclic('abcde')
    'bcaed'
    >>> encode_cyclic('abcd')
    'bcaed'
    >>> encode_cyclic('abc')
    'bca'
    >>> encode_cyclic('ab')
    'ab'
    >>> encode_cyclic('a')
    'a'
    >>> encode_cyclic('')
    ''
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    >>> decode_cyclic('bcaefd')
    'abcdef'
    >>> decode_cyclic('bcaed')
    'abcde'
    >>> decode_cyclic('bcaed')
    'abcd'
    >>> decode_cyclic('bca')
    'abc'
    >>> decode_cyclic('ab')
    'ab'
    >>> decode_cyclic('a')
    'a'
    >>> decode_cyclic('')
    ''
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
