class Solution:
    ___ intersection(self, a, b
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans = []

        __ not a or not b:
            r_ ans

        s = set(a)
        t = set(b)

        ___ x in s:
            __ x in t:
                ans.append(x)

        r_ ans


class Solution:
    ___ intersection(self, a, b
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans = []

        __ not a or not b:
            r_ ans

        a.sort()
        b.sort()

        m, n = le.(a), le.(b)
        i = j = 0

        w___ i < m and j < n:
            __ a[i] __ b[j]:
                __ not ans or a[i] != ans[-1]:
                    ans.append(a[i])
                i += 1
                j += 1
            ____ a[i] < b[j]:
                i += 1
            ____
                j += 1

        r_ ans
