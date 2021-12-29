class Solution:
    ___ strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        NOT_FOUND = -1
        __ haystack is None or needle is None:
            return NOT_FOUND
        __ haystack == needle:
            return 0

        m, n = len(haystack), len(needle)

        for i in range(m - n + 1):
            __ haystack[i:i + n] == needle:
                return i

        return NOT_FOUND
