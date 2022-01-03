"""
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ strStr_brute_force(self, haystack, needle):
        """
        Algorithm:
        two pointers

        :param haystack: str
        :param needle: str
        :return: str or None
        """
        l_hay = l..(haystack)
        l_ndl = l..(needle)
        ___ i __ xrange(l_hay-l_ndl+1):  # i+l_ndl <= l_hay
            __ haystack[i:i+l_ndl]__needle:
                r.. haystack[i:]
        r.. N..

    ___ strStr(self, haystack, needle):
        """
        KMP algorithm
        :type haystack: str
        :type needle: str
        :param haystack:
        :param needle:
        :return:
        """
        ln = l..(needle)
        lh = l..(haystack)
        __ ln__0:
            r.. haystack
        __ ln__1:
            try:
                index = haystack.index(needle)
                r.. haystack[index:]
            except ValueError:
                r.. N..

        # construct T
        T = [0 ___ _ __ xrange(ln)]
        T[0] = -1
        T[1] = 0
        pos = 2
        cnd = 0
        w.... pos<ln:
            __ needle[pos-1]__needle[cnd]:  # pos-1 rather than pos
                cnd += 1
                T[pos] = cnd
                pos += 1
            ____ T[cnd]!=-1:
                cnd = T[cnd]
            ____:
                cnd = 0
                T[pos] = cnd
                pos += 1

        # search
        i = 0
        m = 0
        w.... m+i<lh:
            __ needle[i]__haystack[m+i]:
                i += 1
                __ i__ln:
                    r.. haystack[m:]
            ____:
                __ T[i]!=-1:
                    m = m+i-T[i]
                    i = T[i]
                ____:
                    m += 1
                    i = 0

        r.. N..


__ __name____"__main__":
    needle = "ABCDABD"
    haystack = "ABC ABCDAB ABCDABCDABDE"
    needle = "aaa"
    haystack = "aaa"
    solution = Solution()
    ... solution.strStr_brute_force(haystack, needle)__solution.strStr(haystack, needle)

