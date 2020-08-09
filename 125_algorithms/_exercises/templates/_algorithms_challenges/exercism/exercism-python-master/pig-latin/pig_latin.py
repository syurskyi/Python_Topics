from re ______ search

___ translate(phrase
    """translate converts a phrase to piglatin"""
    r_ ' '.join(translate_word(word) for word in phrase.split())

CASES = ( r'(.*?[^q])(u.*)', # q case
         r'(^y[^aeiou].*)()', # y case
         r'(.*?)([aeoi].*)' ) # default case

___ translate_word(word
    """translate_word converts a word to piglatin"""
    for case in CASES:
        match = search(case, word)
        __ match and match.group(1) + "ay" != word:
            r_ match.group(2) + match.group(1) + "ay"
    r_ word + "ay"
