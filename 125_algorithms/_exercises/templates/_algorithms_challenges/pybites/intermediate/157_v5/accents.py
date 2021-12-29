from unicodedata import decomposition


___ filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return [c for c in text.lower() __ decomposition(c) != '']
