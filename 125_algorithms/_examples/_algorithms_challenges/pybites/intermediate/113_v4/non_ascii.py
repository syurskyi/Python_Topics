import string
import re


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    ascii = string.ascii_letters
    punctuation = string.punctuation
    digits = string.digits

    results = []

    # for word in re.findall(r'\b[^\W\d]+\b', text, flags=re.UNICODE):
    for word in text.split():
        if any([c in punctuation or c in digits for c in word]):
            continue
        if not all([c in ascii for c in word]):
            results.append(word)

    return results
