_______ unicodedata as ud

___ filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    r.. ''.join([c.lower() ___ c __ text
                    __ 'WITH' __ ud.name(c)])
