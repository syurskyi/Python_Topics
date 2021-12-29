____ typing _______ Tuple
____ collections _______ Counter
_______ re

PAT = r'^\W+|\W+$|^_+|_+$'  # leading or trailing non-word characters



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
    __ n.. isi..(text, str):
        raise ValueError('bad input')

    words = l..(map(l.... x: re.sub(PAT, '', x.replace('_', '')),
                     text.split(' ')))
    counts    # list
    ___ word __ words:
        folded = word.casefold()
        count = Counter([c ___ c __ folded __ c.isalpha()])
        __ count.most_common(1):
            counts.a..((word, count))

    __ counts:
        result = max(counts, key=l.... x: x[1].most_common(1)[0][1])

        __ result[1].most_common():
            letter, count = result[1].most_common(1)[0]
            r.. result[0], letter, count
    ____:
        r.. '', '', 0
