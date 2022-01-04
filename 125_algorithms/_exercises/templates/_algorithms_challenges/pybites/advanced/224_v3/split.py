_______ __


___ get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    r.. __.f..(r'\b[A-Z].+?[.?!](?= +[A-Z]|$)', text.r..('\n', ' ').s.., __.DOTALL)
