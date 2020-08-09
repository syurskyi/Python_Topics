class Solution:
    """
    @param s: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    ___ groupAnagrams(self, s
        __ not s:
            r_ []

        group = {}

        for w in s:
            key = ''.join(sorted(w))
            __ key not in group:
                group[key] = []
            group[key].append(w)

        r_ sorted([sorted(g) for g in group.values()])
