"""
Premium Question
Generation
https://leetcode.com/problems/strobogrammatic-number-iii/
"""
from collections ______ deque

__author__ = 'Daniel'


class Solution(object
    ___ __init__(self
        self.lst = ["11", "69", "88", "96", "00"]
        self.middle = ["0", "1", "8"]

    ___ strobogrammaticInRange(self, low, high
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        cnt = 0
        for l in xrange(le.(low), le.(high)+1
            cnt += le.(filter(lambda x: int(low) <= int(x) <= int(high), self.strobogrammatic(l)))

        r_ cnt

    # below methods from strobogrammatic number ii
    ___ strobogrammatic(self, n
        ret = []
        self.build(n, deque(), ret)
        r_ ret

    ___ build(self, n, cur, ret
        """
        build from inside
        """
        __ n%2 __ 1 and le.(cur) __ 0:
            for elt in self.middle:
                cur.append(elt)
                self.build(n, cur, ret)
                cur.pop()
        ____
            __ le.(cur) __ n:
                ret.append("".join(cur))
                r_
            for elt in self.lst:
                __ not (elt __ "00" and le.(cur) __ n-2
                    cur.appendleft(elt[0])
                    cur.append(elt[1])
                    self.build(n, cur, ret)
                    cur.pop()
                    cur.popleft()