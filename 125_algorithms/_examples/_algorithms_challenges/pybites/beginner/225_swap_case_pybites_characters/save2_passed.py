def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    PYBITES = "pybites"
    new_str = []
    for t in text:
        if t.lower() in list(PYBITES):
            new_str.append(t.swapcase())
        else:
            new_str.append(t)
    return "".join(new_str)