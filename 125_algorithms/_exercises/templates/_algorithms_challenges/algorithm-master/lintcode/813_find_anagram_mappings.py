"""
Find last pos
"""
class Solution:
    ___ anagramMappings(self, a, b
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        __ not a or not b or le.(a) != le.(b
            r_ []

        n = le.(a)
        ans = [-1] * n
        b2i = {}

        ___ i in range(n
            b2i[b[i]] = i

        ___ i in range(n
            __ a[i] not in b2i:
                r_ []

            ans[i] = b2i[a[i]]

        r_ ans


"""
Strict
"""
class Solution:
    ___ anagramMappings(self, a, b
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        __ not a or not b or le.(a) != le.(b
            r_ []

        n = le.(a)
        ans = [-1] * n
        b2i = {}

        ___ i in range(n
            __ b[i] not in b2i:
                b2i[b[i]] = []

            b2i[b[i]].append(i)

        ___ i in range(n
            __ not b2i.get(a[i]
                # a[i] not in b2i
                # b2i[a[i]] is empty list
                r_ []

            ans[i] = b2i[a[i]].pop()

        r_ ans
