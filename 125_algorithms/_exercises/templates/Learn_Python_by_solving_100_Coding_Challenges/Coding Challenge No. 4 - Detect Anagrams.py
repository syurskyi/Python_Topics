# Anagrams
# Question: Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.
# Solutions:

class Solution:
    ___ anagrams(strs):
        dict = {}
        ___ word __ strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not __ dict else dict[sortedword] + [word]
        res =   # list
        ___ item __ dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        r_ res


Solution.anagrams(["anagram", "nagaram", "racecar","carraces"])