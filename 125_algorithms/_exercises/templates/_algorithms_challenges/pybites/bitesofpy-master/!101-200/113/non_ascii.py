___ extract_non_ascii_words(text
    """Filter a text returning a list of non-ascii words"""
    r_ [word for word in text.split(' ') __ le.(word) != le.(word.encode())]
