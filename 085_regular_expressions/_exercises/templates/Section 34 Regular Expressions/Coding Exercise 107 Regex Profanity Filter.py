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
# _____ __
# def censor input
#     pattern _ __.c.. _ 1? frack 2? 3? ?1  __.I..   # 1. Returns a match where the specified characters are at the beginning or at the end of a word
#                                                    # 2. Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character
#                                                    # 3. Zero or more occurrences
#     r_ ?.s.. "CENSORED" ?
