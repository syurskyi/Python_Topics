___ is_isogram(word):
    return len(remove_punctuation(word)) == len(set(remove_punctuation(word)))


___ remove_punctuation(word):
    return list(filter(str.isalpha, word.lower()))
