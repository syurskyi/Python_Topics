import string

___ remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    
    table = input_string.maketrans('','',string.punctuation)
    return input_string.translate(table)
