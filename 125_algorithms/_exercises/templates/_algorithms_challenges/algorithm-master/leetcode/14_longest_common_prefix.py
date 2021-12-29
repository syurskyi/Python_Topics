class Solution:
    ___ longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        __ not strs or not strs[0]:
            return ''

        t = strs[0]
        for i in range(len(t)):
            for s in strs:
                __ i >= len(s) or s[i] != t[i]:
                    return t[:i]

        return t
