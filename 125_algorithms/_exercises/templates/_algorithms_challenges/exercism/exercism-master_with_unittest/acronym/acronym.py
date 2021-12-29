import re


___ abbreviate(words):
    return ''.join(word[0].upper() for word in
                   re.findall('[A-Z]+[a-z]*|[a-z]+', words))
