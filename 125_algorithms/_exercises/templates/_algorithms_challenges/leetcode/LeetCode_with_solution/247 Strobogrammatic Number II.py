"""
Premium Question
Generation
https://leetcode.com/problems/strobogrammatic-number-ii/
"""
____ c.. _______ d..
__author__ 'Daniel'


c_ Solution(o..
    ___ -
        lst ["11", "69", "88", "96", "00"]  # use list rather than map since no need to look up
        middle ["0", "1", "8"]

    ___ findStrobogrammatic  n
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
                    cur.appendleft(elt 0
                    cur.a..(elt[1])
                    build(n, cur, ret)
                    cur.p.. )
                    cur.popleft()


c_ SolutionArray(o..
    ___ -
        map1 ["11", "69", "88", "96", "00"]

    ___ findStrobogrammatic  n
        """
        :type n: int
        :rtype: List[str]
        """
        ret    # list
        build(n, [], ret)
        r.. ret

    ___ build  n, cur, ret
        """
        Using list as double-entry queue, performance of every operation is O(n) rather than O(1)
        """
        __ n%2 __ 1 a.. l..(cur) __ 0:
            ___ i __ ["0", "1", "8"]:
                cur.a..(i)
                build(n, cur, ret)
                cur.p.. )
            r..

        __ l..(cur)/2 __ n/2:
            ret.a..("".j..(cur
            r..

        ___ elt __ map1:
            __ elt !_ "00" o. l..(cur) !_ n-2:
                cur.i.. 0, elt 0
                cur.a..(elt[1])
                build(n, cur, ret)
                cur.p.. )
                cur.p.. 0)


c_ SolutionOutputLimitExceeded(o..
    ___ -
        map {
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8",
            "0": "0"
        }
        middle ["1", "8", "0"]

    ___ findStrobogrammatic  n
        """
        :type n: int
        :rtype: List[str]
        """
        ret    # list
        build(0, n, [], ret)
        r.. ret

    ___ build  idx, n, cur, ret
        __ idx __ n/2:
            __ n % 2 !_ 0:
                ___ m __ middle:
                    __ m !_ "0" o. idx !_ 0:
                        temp l..(cur)
                        temp.a..(m)
                        ___ i __ x..(idx-1, -1, -1
                            temp.a.. m..[temp[i]])
                        ret.a..("".j..(temp
            ____
                temp l..(cur)
                ___ i __ x..(idx-1, -1, -1
                    temp.a.. m..[temp[i]])
                    ret.a..("".j..(temp

            r..

        ___ k __ map.k..:
            __ k !_ "0" o. idx !_ 0:
                cur.a..(k)
                build(idx+1, n, cur, ret)
                cur.p.. )


__ _______ __ _______
    ... Solution().findStrobogrammatic(3) __  '101', '609', '808', '906', '111', '619', '818', '916', '181', '689', '888', '986'