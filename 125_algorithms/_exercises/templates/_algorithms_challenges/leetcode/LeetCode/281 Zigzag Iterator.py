"""
Premium Question
"""
__author__ = 'Daniel'


class ZigzagIterator(object
    ___ __init__(self, v1, v2
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.mat = [v1, v2]
        self.maxa = max((c, r) for r, c in enumerate(map(lambda x: le.(x)-1, self.mat)))
        self.i = 0
        self.j = 0
        self._reposition()

    ___ _reposition(self
        w___ self.i >= le.(self.mat) or self.j >= le.(self.mat[self.i]
            __ not self.hasNext(
                r_

            ____ self.i >= le.(self.mat
                self.i = 0
                self.j += 1

            ____ self.j >= le.(self.mat[self.i]
                self.i += 1

    ___ next(self
        """
        :rtype: int
        """
        __ not self.hasNext(
            raise StopIteration

        ret = self.mat[self.i][self.j]
        self.i += 1
        self._reposition()
        r_ ret

    ___ hasNext(self
        """
        :rtype: bool
        """
        r_ self.j <= self.maxa[0]


__ __name__ __ "__main__":
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    itr = ZigzagIterator(v1, v2)
    w___ itr.hasNext(
        print itr.next()