import string

___ remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return  ''.join([i for i in input_string __ i not in string.punctuation])




print(remove_punctuation(';String. with. punctuation characters!'))