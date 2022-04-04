____ c.. _______ d..
___ is_anagram(word1, word2
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""

    word1 = word1.l..
    word2 = word2.l..

    word_2_counts = d..(i..)


    ___ character __ word2:
        __ character != ' ':
            word_2_counts[character] += 1


    ___ character __ word1:
        __ character __ ' ':
            _____
        word_2_counts[character]  -= 1
        __ word_2_counts[character] __ 0:
            del word_2_counts[character]
        


    r.. n.. word_2_counts
