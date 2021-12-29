___ extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split(' ') __ len(word) != len(word.encode())]
