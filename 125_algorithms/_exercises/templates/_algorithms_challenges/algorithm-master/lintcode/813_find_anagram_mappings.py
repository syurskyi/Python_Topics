"""
Find last pos
"""
class Solution:
    ___ anagramMappings(self, a, b):
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        __ not a or not b or len(a) != len(b):
            return []

        n = len(a)
        ans = [-1] * n
        b2i = {}

        for i in range(n):
            b2i[b[i]] = i

        for i in range(n):
            __ a[i] not in b2i:
                return []

            ans[i] = b2i[a[i]]

        return ans


"""
Strict
"""
class Solution:
    ___ anagramMappings(self, a, b):
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        __ not a or not b or len(a) != len(b):
            return []

        n = len(a)
        ans = [-1] * n
        b2i = {}

        for i in range(n):
            __ b[i] not in b2i:
                b2i[b[i]] = []

            b2i[b[i]].append(i)

        for i in range(n):
            __ not b2i.get(a[i]):
                # a[i] not in b2i
                # b2i[a[i]] is empty list
                return []

            ans[i] = b2i[a[i]].pop()

        return ans
