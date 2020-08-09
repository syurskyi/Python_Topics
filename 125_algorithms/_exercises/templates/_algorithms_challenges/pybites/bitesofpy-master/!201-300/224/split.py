______ re


___ get_sentences(text
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    r_ re.findall(r'\b[A-Z].+?[.?!](?= +[A-Z]|$)', text.replace('\n', ' ').strip(), re.DOTALL)
