class Solution:
    """
    @param s: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    ___ groupAnagrams(self, s):
        __ n.. s:
            r.. []

        group = {}

        ___ w __ s:
            key = ''.join(s..(w))
            __ key n.. __ group:
                group[key]    # list
            group[key].a..(w)

        r.. s..([s..(g) ___ g __ group.values()])
