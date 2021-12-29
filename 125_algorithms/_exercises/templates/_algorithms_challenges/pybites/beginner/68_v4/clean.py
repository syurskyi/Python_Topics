___ remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return "".join([x for x in input_string __ x not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'])
