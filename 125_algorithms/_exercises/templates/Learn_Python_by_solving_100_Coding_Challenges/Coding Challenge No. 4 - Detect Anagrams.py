# Anagrams
# Question: Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.
# Solutions:

class Solution:
    def anagrams(strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res


Solution.anagrams(["anagram", "nagaram", "racecar","carraces"])