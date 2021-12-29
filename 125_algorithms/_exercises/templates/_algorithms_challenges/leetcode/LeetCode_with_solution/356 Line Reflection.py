"""
Premium Question
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.x = N..

    ___ isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        d = defaultdict(l..)
        ___ x, y __ points:
            d[y].a..(x)

        ___ v __ d.values():
            __ n.. self.check(v):
                r.. False

        r.. True

    ___ check(self, lst):
        lst.sort()
        i = 0
        j = l..(lst) - 1
        while i < j:
            x = (lst[i] + lst[j]) / float(2)
            __ n.. self.x:
                self.x = x
            ____ self.x != x:
                r.. False

            i += 1
            j -= 1

        __ i __ j:
            __ n.. self.x:
                self.x = lst[i]
            ____ self.x != lst[i]:
                r.. False

        r.. True

__ __name__ __ "__main__":
    ... Solution().isReflected([[1,1],[-1,-1]]) __ False
