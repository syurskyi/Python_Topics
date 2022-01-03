"""
Write a function to find the longest common prefix string amongst an array of
strings.
"""


c_ Solution(object):
    ___ longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        __ n.. strs:
            r.. ""
        res = strs[0]
        ___ s __ strs[1:]:
            n = l..(s)
            ___ i, c __ e..(res):
                __ i >= n o. res[i] != s[i]:
                    res = res[:i]
                    break
        r.. res
