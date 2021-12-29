"""
Premium Question
Generation
https://leetcode.com/problems/strobogrammatic-number-ii/
"""
____ collections _______ deque
__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.lst = ["11", "69", "88", "96", "00"]  # use list rather than map since no need to look up
        self.middle = ["0", "1", "8"]

    ___ findStrobogrammatic(self, n):
        ret    # list
        self.build(n, deque(), ret)
        r.. ret

    ___ build(self, n, cur, ret):
        """
        build from inside
        """
        __ n%2 __ 1 and l..(cur) __ 0:
            ___ elt __ self.middle:
                cur.a..(elt)
                self.build(n, cur, ret)
                cur.pop()
        ____:
            __ l..(cur) __ n:
                ret.a..("".join(cur))
                r..
            ___ elt __ self.lst:
                __ n.. (elt __ "00" and l..(cur) __ n-2):
                    cur.appendleft(elt[0])
                    cur.a..(elt[1])
                    self.build(n, cur, ret)
                    cur.pop()
                    cur.popleft()


class SolutionArray(object):
    ___ __init__(self):
        self.map1 = ["11", "69", "88", "96", "00"]

    ___ findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret    # list
        self.build(n, [], ret)
        r.. ret

    ___ build(self, n, cur, ret):
        """
        Using list as double-entry queue, performance of every operation is O(n) rather than O(1)
        """
        __ n%2 __ 1 and l..(cur) __ 0:
            ___ i __ ["0", "1", "8"]:
                cur.a..(i)
                self.build(n, cur, ret)
                cur.pop()
            r..

        __ l..(cur)/2 __ n/2:
            ret.a..("".join(cur))
            r..

        ___ elt __ self.map1:
            __ elt != "00" o. l..(cur) != n-2:
                cur.insert(0, elt[0])
                cur.a..(elt[1])
                self.build(n, cur, ret)
                cur.pop()
                cur.pop(0)


class SolutionOutputLimitExceeded(object):
    ___ __init__(self):
        self.map = {
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8",
            "0": "0"
        }
        self.middle = ["1", "8", "0"]

    ___ findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret    # list
        self.build(0, n, [], ret)
        r.. ret

    ___ build(self, idx, n, cur, ret):
        __ idx __ n/2:
            __ n % 2 != 0:
                ___ m __ self.middle:
                    __ m != "0" o. idx != 0:
                        temp = l..(cur)
                        temp.a..(m)
                        ___ i __ xrange(idx-1, -1, -1):
                            temp.a..(self.map[temp[i]])
                        ret.a..("".join(temp))
            ____:
                temp = l..(cur)
                ___ i __ xrange(idx-1, -1, -1):
                    temp.a..(self.map[temp[i]])
                    ret.a..("".join(temp))

            r..

        ___ k __ self.map.keys():
            __ k != "0" o. idx != 0:
                cur.a..(k)
                self.build(idx+1, n, cur, ret)
                cur.pop()


__ __name__ __ "__main__":
    ... Solution().findStrobogrammatic(3) __ ['101', '609', '808', '906', '111', '619', '818', '916', '181', '689', '888', '986']