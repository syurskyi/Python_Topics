"""
Premium Question
Generation
https://leetcode.com/problems/strobogrammatic-number-iii/
"""
____ c.. _______ d..

__author__ 'Daniel'


c_ Solution(o..
    ___ -
        lst ["11", "69", "88", "96", "00"]
        middle ["0", "1", "8"]

    ___ strobogrammaticInRange  low, high
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        cnt 0
        ___ l __ x..(l..(low), l..(high)+1
            cnt += l..(f.. l.... x: i..(low) <_ i..(x) <_ i..(high), strobogrammatic(l)))

        r.. cnt

    # below methods from strobogrammatic number ii
    ___ strobogrammatic  n
        ret    # list
        build(n, d..(), ret)
        r.. ret

    ___ build  n, cur, ret
        """
        build from inside
        """
        __ n%2 __ 1 a.. l..(cur) __ 0:
            ___ elt __ middle:
                cur.a..(elt)
                build(n, cur, ret)
                cur.p.. )
        ____
            __ l..(cur) __ n:
                ret.a..("".j..(cur
                r..
            ___ elt __ lst:
                __ n.. (elt __ "00" a.. l..(cur) __ n-2
                    cur.appendleft(elt[0])
                    cur.a..(elt[1])
                    build(n, cur, ret)
                    cur.p.. )
                    cur.popleft()