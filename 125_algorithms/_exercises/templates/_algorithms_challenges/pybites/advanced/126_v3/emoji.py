_______ ___
_______ unicodedata

START_EMOJI_RANGE 100000  # estimate


___ what_means_emoji(emoji
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    ___
        r.. unicodedata.name(emoji)
    ______ T..
        r.. 'Not found'


___ _make_emoji_mapping
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    __ _make_emoji_mapping.MAPPING:
        res _make_emoji_mapping.MAPPING
    ____
        res d..()
        ___ em __ r..(START_EMOJI_RANGE, ___.maxunicode + 1
            emoji chr(em)
            ___
                desc what_means_emoji(emoji)
                __ desc !_ 'Not found':
                    res[emoji] desc.l..
            ______ V..
                p..
        _make_emoji_mapping.MAPPING res
    r.. res


_make_emoji_mapping.MAPPING N..


___ find_emoji(term
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term term.l..
    emoji_mapping _make_emoji_mapping()
    ___ em, desc __ emoji_mapping.i..
        __ term __ desc:
            print _*{desc:40} | {em}')
