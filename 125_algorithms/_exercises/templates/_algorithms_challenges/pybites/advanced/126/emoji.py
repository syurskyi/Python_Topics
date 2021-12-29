_______ sys
_______ unicodedata


START_EMOJI_RANGE = 100000  # estimate


___ what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        r.. unicodedata.name(emoji)
    except TypeError:
        r.. 'Not found'


___ _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""


    mapping = {}


    ___ i __ r..(START_EMOJI_RANGE,sys.maxunicode + 1):
        try:
            meaning = what_means_emoji(chr(i))
            mapping[chr(i)] = meaning
        except:
            pass

    r.. mapping



___ find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()

    emoji_mapping = _make_emoji_mapping()

    # ... your turn ...

    ___ emoji,meaning __ emoji_mapping.items():
        __ term __ meaning.lower():
            print(meaning,emoji)



