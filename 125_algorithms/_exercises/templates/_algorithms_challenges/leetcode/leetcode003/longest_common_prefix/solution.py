"""
Write a function to find the longest common prefix string amongst an array of
strings.
"""


class Solution(object):
    ___ longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        __ not strs:
            return ""
        res = strs[0]
        for s in strs[1:]:
            n = len(s)
            for i, c in enumerate(res):
                __ i >= n or res[i] != s[i]:
                    res = res[:i]
                    break
        return res
