class Solution:
    ___ intersect(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. a o. n.. b:
            r.. ans

        freq = {}

        ___ x __ a:
            freq[x] = freq.get(x, 0) + 1

        ___ x __ b:
            __ n.. freq.get(x):
                continue

            freq[x] -= 1
            ans.a..(x)

        r.. ans


class Solution:
    ___ intersect(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. a o. n.. b:
            r.. ans

        a.sort()
        b.sort()

        m, n = l..(a), l..(b)
        i = j = 0

        while i < m and j < n:
            __ a[i] __ b[j]:
                ans.a..(a[i])
                i += 1
                j += 1
            ____ a[i] < b[j]:
                i += 1
            ____:
                j += 1

        r.. ans
