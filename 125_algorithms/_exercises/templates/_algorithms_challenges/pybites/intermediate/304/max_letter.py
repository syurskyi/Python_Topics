from typing import Tuple
from collections import Counter
import string
import re 



___ max_letter_word(text: str) -> Tuple[str, str, int]:
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
    __ not isinstance(text,str):
        raise ValueError("Strings only")

    
    max_count = 0
    max_word = max_letter =  ''

    words = text.split()

    for word in words:
        counts = Counter()
        for letter in word.casefold():
            __ letter.isalpha():
                counts[letter] += 1

        __ counts:
            most_common_letter,most_common_count = counts.most_common(1)[0]
            __ most_common_count > max_count:

                max_count = most_common_count
                max_word = word.strip(string.punctuation + string.digits + '«¿')
                max_letter = most_common_letter


    return max_word,max_letter,max_count
