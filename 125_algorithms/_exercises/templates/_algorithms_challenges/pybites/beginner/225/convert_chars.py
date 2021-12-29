PYBITES = "pybiteS"


___ convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    return ''.join(c.swapcase() __ c.lower() in PYBITES else c
                   for c in text)

print(convert_pybites_chars('pybites'))


