class Solution:
    """
    @param s: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    ___ groupAnagrams(self, s):
        __ not s:
            return []

        group = {}

        for w in s:
            key = ''.join(sorted(w))
            __ key not in group:
                group[key] = []
            group[key].append(w)

        return sorted([sorted(g) for g in group.values()])
