"""
Functions for helping with English vocabulary homework.
"""


def add_prefix_un(word):
    """Add the prefix 'un' to the given word.

    :param word: str - the original word
    :return: str - word with 'un' prefix
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Create word groups with a prefix.

    :param vocab_words: list - words with prefix as first item
    :return: str - grouped words
    """
    prefix = vocab_words[0]
    words = vocab_words[1:]

    return prefix + " :: " + " :: ".join(prefix + word for word in words)


def remove_suffix_ness(word):
    """Remove the suffix 'ness' and adjust spelling if needed.

    :param word: str - word ending with 'ness'
    :return: str - word without 'ness'
    """
    if word.endswith("iness"):
        return word[:-5] + "y"
    else:
        return word[:-4]


def adjective_to_verb(sentence, index):
    """Convert an adjective in a sentence to a verb.

    :param sentence: str - sentence containing an adjective
    :param index: int - index of adjective
    :return: str - verb form of adjective
    """
    word = sentence.split()[index]

    # Remove punctuation if present
    word = word.strip(".,!?")

    return word + "en"
