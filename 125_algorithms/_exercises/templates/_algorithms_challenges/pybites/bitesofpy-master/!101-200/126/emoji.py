______ sys
______ unicodedata

START_EMOJI_RANGE = 100000  # estimate


___ what_means_emoji(emoji
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        r_ unicodedata.name(emoji)
    except TypeError:
        r_ 'Not found'


___ _make_emoji_mapping(
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    __ _make_emoji_mapping.MAPPING:
        res = _make_emoji_mapping.MAPPING
    ____
        res = dict()
        for em in range(START_EMOJI_RANGE, sys.maxunicode + 1
            emoji = chr(em)
            try:
                desc = what_means_emoji(emoji)
                __ desc != 'Not found':
                    res[emoji] = desc.lower()
            except ValueError:
                pass
        _make_emoji_mapping.MAPPING = res
    r_ res


_make_emoji_mapping.MAPPING = None


___ find_emoji(term
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()
    emoji_mapping = _make_emoji_mapping()
    for em, desc in emoji_mapping.items(
        __ term in desc:
            print(f'{desc:40} | {em}')
