# Profanity Filter Solution
#
# My regex is pretty simple:
#
#     \bfrack\w*\b
#
# It looks for a word boundary and then the letters "frack" and then optionally more word characters afterwards,
# and then a word boundary again.  I used the word boundaries to prevent false positives if the "frack" occurs in
# the middle of another word.s
#
# Here's the complete solution.  Notice I used the re.IGNORECASE flag:

import re


def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)
