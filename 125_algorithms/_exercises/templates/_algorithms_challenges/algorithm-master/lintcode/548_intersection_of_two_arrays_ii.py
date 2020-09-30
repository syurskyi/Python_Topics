class Solution:
    ___ intersect(self, a, b
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans =   # list

        __ not a or not b:
            r_ ans

        freq = {}

        ___ x __ a:
            freq[x] = freq.get(x, 0) + 1

        ___ x __ b:
            __ not freq.get(x
                continue

            freq[x] -= 1
            ans.append(x)

        r_ ans


class Solution:
    ___ intersect(self, a, b
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans =   # list

        __ not a or not b:
            r_ ans

        a.sort()
        b.sort()

        m, n = le.(a), le.(b)
        i = j = 0

        w___ i < m and j < n:
            __ a[i] __ b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            ____ a[i] < b[j]:
                i += 1
            ____
                j += 1

        r_ ans
