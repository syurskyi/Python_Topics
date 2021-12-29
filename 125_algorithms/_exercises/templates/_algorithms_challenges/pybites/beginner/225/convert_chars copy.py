PYBITES = "pybites"


___ convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    temp = ''
    for letter in text:
        __ letter.upper() in PYBITES.upper():
            __ letter.islower():
                temp += letter.upper()
            elif letter.isupper():
                temp += letter.lower()
        else:
            temp += letter
    return(temp)


convert_pybites_chars("PyBiTeS")