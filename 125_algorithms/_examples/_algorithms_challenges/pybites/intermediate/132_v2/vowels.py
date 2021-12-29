VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
        
    top_vowel_count = float("-inf")
    top_word = None
        
    for word in text.lower().split():
        vowel_count = 0
        for character in word:
            if character in VOWELS:
                vowel_count += 1

        if vowel_count > top_vowel_count:
            top_vowel_count = vowel_count
            top_word = word


    return top_word,top_vowel_count









