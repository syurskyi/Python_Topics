class Solution:
    ___ longestCommonPrefix(self, strs
        """
        :type strs: List[str]
        :rtype: str
        """
        __ not strs or not strs[0]:
            r_ ''

        t = strs[0]
        ___ i in range(le.(t)):
            ___ s in strs:
                __ i >= le.(s) or s[i] != t[i]:
                    r_ t[:i]

        r_ t
