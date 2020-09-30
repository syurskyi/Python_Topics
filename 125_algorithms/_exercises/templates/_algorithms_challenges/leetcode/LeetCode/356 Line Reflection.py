"""
Premium Question
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ __init__(self
        self.x = None

    ___ isReflected(self, points
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        d = defaultdict(list)
        ___ x, y __ points:
            d[y].append(x)

        ___ v __ d.values(
            __ not self.check(v
                r_ False

        r_ True

    ___ check(self, lst
        lst.sort()
        i = 0
        j = le.(lst) - 1
        w___ i < j:
            x = (lst[i] + lst[j]) / float(2)
            __ not self.x:
                self.x = x
            ____ self.x != x:
                r_ False

            i += 1
            j -= 1

        __ i __ j:
            __ not self.x:
                self.x = lst[i]
            ____ self.x != lst[i]:
                r_ False

        r_ True

__  -n __ "__main__":
    assert Solution().isReflected([[1,1],[-1,-1]]) __ False
