"""This module supports searching"""


def find_indicies(content: str, pattern: str) -> list:
    """Return the indicies of words that contains the pattern."""
    input_words = content.split()

    indicies = [idx for idx, word in enumerate(input_words) if pattern in word]

    return indicies


def search(pattern: str, content: str, ignore_case: bool = False) -> list:
    """Return the original words that contains the pattern.
    If `ignore_case` is `True` then capital letters are ignored."""
    words = content.split()

    if ignore_case:
        content = content.lower()
        pattern = pattern.lower()

    indicies = find_indicies(content, pattern)
    found_words = [words[index] for index in indicies]

    return found_words
