"""
Premium Question.
"""
__author__ = 'Daniel'


class Vector2D:
    ___ __init__(self, vec2d):
        """
        :type vec2d: list[list[int]]
        :type: None
        """
        self.vec2d = vec2d
        self.i = 0
        self.j = 0

    ___ next(self):
        """

        :rtype: int
        """
        ret = N..
        __ self.hasNext():
            ret = self.vec2d[self.i][self.j]
            self.j += 1

        r.. ret

    ___ hasNext(self):
        """
        This function structures the two pointers.
        :rtype: bool
        """
        # update
        w.... self.i < l..(self.vec2d) a.. self.j >= l..(self.vec2d[self.i]):
            self.i += 1
            self.j = 0

        r.. self.i < l..(self.vec2d) a.. self.j < l..(self.vec2d[self.i])
