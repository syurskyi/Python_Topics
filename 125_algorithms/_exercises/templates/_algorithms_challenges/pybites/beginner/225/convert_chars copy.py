PYBITES = "pybites"


___ convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    temp = ''
    ___ letter __ text:
        __ letter.upper() __ PYBITES.upper():
            __ letter.isl..
                temp += letter.upper()
            ____ letter.isupper():
                temp += letter.l..
        ____:
            temp += letter
    r..(temp)


convert_pybites_chars("PyBiTeS")