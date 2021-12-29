"""
Premium Question
Generation
https://leetcode.com/problems/strobogrammatic-number-iii/
"""
____ collections _______ deque

__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.lst = ["11", "69", "88", "96", "00"]
        self.middle = ["0", "1", "8"]

    ___ strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        cnt = 0
        ___ l __ xrange(l..(low), l..(high)+1):
            cnt += l..(filter(l.... x: int(low) <= int(x) <= int(high), self.strobogrammatic(l)))

        r.. cnt

    # below methods from strobogrammatic number ii
    ___ strobogrammatic(self, n):
        ret    # list
        self.build(n, deque(), ret)
        r.. ret

    ___ build(self, n, cur, ret):
        """
        build from inside
        """
        __ n%2 __ 1 a.. l..(cur) __ 0:
            ___ elt __ self.middle:
                cur.a..(elt)
                self.build(n, cur, ret)
                cur.pop()
        ____:
            __ l..(cur) __ n:
                ret.a..("".join(cur))
                r..
            ___ elt __ self.lst:
                __ n.. (elt __ "00" a.. l..(cur) __ n-2):
                    cur.appendleft(elt[0])
                    cur.a..(elt[1])
                    self.build(n, cur, ret)
                    cur.pop()
                    cur.popleft()