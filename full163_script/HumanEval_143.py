def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters

    >>> words_in_sentence("This is a test")
    'is'
    >>> words_in_sentence("lets go for swimming")
    'go for'
    >>> words_in_sentence("I love programming")
    'programming'
    >>> words_in_sentence("a ab abc abcd abcde")
    'ab abc abcde'
    """
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_length_words)
