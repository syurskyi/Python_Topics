______ re


___ abbreviate(words
    regex = '[A-Z]+[a-z]*|[a-z]+'
    r_ ''.join(word[0].upper() for word in re.findall(regex, words))
