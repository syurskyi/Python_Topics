class Solution:
    ___ intersect(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans = []

        __ not a or not b:
            return ans

        freq = {}

        for x in a:
            freq[x] = freq.get(x, 0) + 1

        for x in b:
            __ not freq.get(x):
                continue

            freq[x] -= 1
            ans.append(x)

        return ans


class Solution:
    ___ intersect(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans = []

        __ not a or not b:
            return ans

        a.sort()
        b.sort()

        m, n = len(a), len(b)
        i = j = 0

        while i < m and j < n:
            __ a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return ans
