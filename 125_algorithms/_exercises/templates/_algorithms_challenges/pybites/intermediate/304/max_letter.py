____ t___ _______ Tuple
____ c.. _______ C..
_______ s__
_______ __



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
    __ n.. isi..(text,s..
        r.. V...("Strings only")

    
    max_count 0
    max_word max_letter =  ''

    words text.s..

    ___ word __ words:
        counts C..()
        ___ letter __ word.c..
            __ letter.i..
                counts[letter] += 1

        __ counts:
            most_common_letter,most_common_count ?.m..(1)[0]
            __ most_common_count > max_count:

                max_count most_common_count
                max_word word.s..(s__.punctuation + s__.d.. + '«¿')
                max_letter most_common_letter


    r.. max_word,max_letter,max_count
