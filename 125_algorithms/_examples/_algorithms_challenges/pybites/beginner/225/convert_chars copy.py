PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    temp = ''
    for letter in text:
        if letter.upper() in PYBITES.upper():
            if letter.islower():
                temp += letter.upper()
            elif letter.isupper():
                temp += letter.lower()
        else:
            temp += letter
    return(temp)


convert_pybites_chars("PyBiTeS")