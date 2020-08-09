___ is_anagram(word1, word2
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    w1 = word1.lower().replace(' ', '')
    w2 = word2.lower().replace(' ', '')
    __ le.(w1) != le.(w2
        r_ False
    r_ all(x __ y ___ x, y in zip(sorted(w1.lower()), sorted(w2.lower())))
