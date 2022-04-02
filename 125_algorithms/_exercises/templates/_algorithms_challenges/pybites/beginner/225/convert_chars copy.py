PYBITES = "pybites"


___ convert_pybites_chars(text
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    temp = ''
    ___ letter __ text:
        __ letter.u.. __ PYBITES.u..:
            __ letter.isl..
                temp += letter.u..
            ____ letter.isupper
                temp += letter.l..
        ____:
            temp += letter
    r..(temp)


convert_pybites_chars("PyBiTeS")