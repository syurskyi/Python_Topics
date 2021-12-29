"""
Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.x = None

    ___ isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        d = defaultdict(list)
        for x, y in points:
            d[y].append(x)

        for v in d.values():
            __ not self.check(v):
                return False

        return True

    ___ check(self, lst):
        lst.sort()
        i = 0
        j = len(lst) - 1
        while i < j:
            x = (lst[i] + lst[j]) / float(2)
            __ not self.x:
                self.x = x
            elif self.x != x:
                return False

            i += 1
            j -= 1

        __ i == j:
            __ not self.x:
                self.x = lst[i]
            elif self.x != lst[i]:
                return False

        return True

__ __name__ == "__main__":
    assert Solution().isReflected([[1,1],[-1,-1]]) == False
