____ typing _______ Tuple
____ c.. _______ Counter
_______ __

PAT = r'^\W+|\W+$|^_+|_+$'  # leading or trailing non-word characters



___ max_letter_word(text: s..) __ Tuple[s.., s.., i..]:
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
    __ n.. isi..(text, s..):
        r.. ValueError('bad input')

    words = l..(map(l.... x: __.sub(PAT, '', x.r..('_', '')),
                     text.s..(' ')))
    counts    # list
    ___ word __ words:
        folded = word.c..()
        count = Counter([c ___ c __ folded __ c.isalpha()])
        __ count.most_common(1):
            counts.a..((word, count))

    __ counts:
        result = m..(counts, key=l.... x: x[1].most_common(1)[0][1])

        __ result[1].most_common
            letter, count = result[1].most_common(1)[0]
            r.. result[0], letter, count
    ____:
        r.. '', '', 0
