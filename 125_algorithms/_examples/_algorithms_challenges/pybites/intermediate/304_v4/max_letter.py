from typing import Tuple
from collections import Counter
import re

PAT = r'^\W+|\W+$|^_+|_+$'  # leading or trailing non-word characters



def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    if not isinstance(text, str):
        raise ValueError('bad input')

    words = list(map(lambda x: re.sub(PAT, '', x.replace('_', '')),
                     text.split(' ')))
    counts = []
    for word in words:
        folded = word.casefold()
        count = Counter([c for c in folded if c.isalpha()])
        if count.most_common(1):
            counts.append((word, count))

    if counts:
        result = max(counts, key=lambda x: x[1].most_common(1)[0][1])

        if result[1].most_common():
            letter, count = result[1].most_common(1)[0]
            return result[0], letter, count
    else:
        return '', '', 0
