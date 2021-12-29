VOWELS = list('aeiou')

___ get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    text = text.lower().split()
    dict = {word: sum(letter in VOWELS for letter in word) for word in text}
    return max(dict.items(), key=lambda x: x[1])