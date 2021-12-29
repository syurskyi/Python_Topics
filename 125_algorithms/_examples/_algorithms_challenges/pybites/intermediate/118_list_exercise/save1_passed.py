from collections import Counter

def get_duplicate_indices(words):
    '''Loop through a list of words and check if each word occurs more than once.
       If so, return the index of its first occurrence.'''
    word_count = Counter(words)
    common_words = [k for k, v in word_count.items() if v > 1]
    return [words.index(word) for word in common_words]
