#preloaded variable: "dictionary"

___ make_backronym(acronym):
    return ' '.join([dictionary[c.upper()] for c in acronym])