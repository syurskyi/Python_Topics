import unicodedata as ud

def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return ''.join([c.lower() for c in text
                    if 'WITH' in ud.name(c)])
