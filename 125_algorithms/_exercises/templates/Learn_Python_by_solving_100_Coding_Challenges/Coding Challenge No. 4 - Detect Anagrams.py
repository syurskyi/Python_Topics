# Anagrams
# Question: Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.
# Solutions:

c_ Solution:
    ___ anagrams(strs):
        di.. _ {}
        ___ word __ strs:
            sortedword _ ''.join(sorted(word))
            di..[sortedword] _ [word] __ sortedword no. __ di.. ____ di..[sortedword] + [word]
        res _   # list
        ___ item __ di..:
            __ le.(di..[item]) >_ 2:
                res +_ di..[item]
        r_ res


Solution.anagrams(["anagram", "nagaram", "racecar","carraces"])