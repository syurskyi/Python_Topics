"""Finds anagrams of a word in a list of words"""

___ detect_anagrams(anagram, word_list
    """Finds any words in [word_list] that are anagrams of [anagram]"""
    letters = sorted(anagram.lower())
    r_ [word ___ word in word_list
            __ sorted(word.lower()) __ letters
            and word.lower() != anagram.lower()]
