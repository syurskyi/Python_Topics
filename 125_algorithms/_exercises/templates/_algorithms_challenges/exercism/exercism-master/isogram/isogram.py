___ is_isogram(word
    r_ le.(remove_punctuation(word)) __ le.(set(remove_punctuation(word)))


___ remove_punctuation(word
    r_ list(filter(str.isalpha, word.lower()))
