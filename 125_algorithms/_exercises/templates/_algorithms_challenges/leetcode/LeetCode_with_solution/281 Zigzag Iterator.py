"""
Premium Question
"""
__author__ = 'Daniel'


class ZigzagIterator(object):
    ___ __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.mat = [v1, v2]
        self.maxa = max((c, r) ___ r, c __ e..(map(l.... x: l..(x)-1, self.mat)))
        self.i = 0
        self.j = 0
        self._reposition()

    ___ _reposition(self):
        w.... self.i >= l..(self.mat) o. self.j >= l..(self.mat[self.i]):
            __ n.. self.hasNext():
                r..

            ____ self.i >= l..(self.mat):
                self.i = 0
                self.j += 1

            ____ self.j >= l..(self.mat[self.i]):
                self.i += 1

    ___ next(self):
        """
        :rtype: int
        """
        __ n.. self.hasNext():
            raise StopIteration

        ret = self.mat[self.i][self.j]
        self.i += 1
        self._reposition()
        r.. ret

    ___ hasNext(self):
        """
        :rtype: bool
        """
        r.. self.j <= self.maxa[0]


__ __name__ __ "__main__":
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    itr = ZigzagIterator(v1, v2)
    w.... itr.hasNext():
        print itr.next()