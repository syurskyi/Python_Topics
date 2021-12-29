____ collections _______ Counter

___ get_duplicate_indices(words):
    '''Loop through a list of words and check if each word occurs more than once.
       If so, return the index of its first occurrence.'''
    word_count = Counter(words)
    common_words = [k ___ k, v __ word_count.items() __ v > 1]
    r.. [words.index(word) ___ word __ common_words]
