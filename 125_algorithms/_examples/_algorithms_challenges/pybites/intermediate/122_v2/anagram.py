from collections import defaultdict
def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""

    word1 = word1.lower()
    word2 = word2.lower()

    word_2_counts = defaultdict(int)


    for character in word2:
        if character != ' ':
            word_2_counts[character] += 1


    for character in word1:
        if character == ' ':
            continue
        word_2_counts[character]  -= 1
        if word_2_counts[character] == 0:
            del word_2_counts[character]
        


    return not word_2_counts
