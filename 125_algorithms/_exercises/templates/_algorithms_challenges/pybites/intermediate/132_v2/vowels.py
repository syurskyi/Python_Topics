VOWELS l..('aeiou')


___ get_word_max_vowels(text
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
        
    top_vowel_count f__("-inf")
    top_word N..
        
    ___ word __ text.l...s.. :
        vowel_count 0
        ___ character __ word:
            __ character __ VOWELS:
                vowel_count += 1

        __ vowel_count > top_vowel_count:
            top_vowel_count vowel_count
            top_word word


    r.. top_word,top_vowel_count









