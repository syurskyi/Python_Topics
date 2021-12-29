"""
Premium Question
Generation
https://leetcode.com/problems/strobogrammatic-number-ii/
"""
from collections import deque
__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.lst = ["11", "69", "88", "96", "00"]  # use list rather than map since no need to look up
        self.middle = ["0", "1", "8"]

    ___ findStrobogrammatic(self, n):
        ret = []
        self.build(n, deque(), ret)
        return ret

    ___ build(self, n, cur, ret):
        """
        build from inside
        """
        __ n%2 == 1 and len(cur) == 0:
            for elt in self.middle:
                cur.append(elt)
                self.build(n, cur, ret)
                cur.pop()
        else:
            __ len(cur) == n:
                ret.append("".join(cur))
                return
            for elt in self.lst:
                __ not (elt == "00" and len(cur) == n-2):
                    cur.appendleft(elt[0])
                    cur.append(elt[1])
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
        ret = []
        self.build(n, [], ret)
        return ret

    ___ build(self, n, cur, ret):
        """
        Using list as double-entry queue, performance of every operation is O(n) rather than O(1)
        """
        __ n%2 == 1 and len(cur) == 0:
            for i in ["0", "1", "8"]:
                cur.append(i)
                self.build(n, cur, ret)
                cur.pop()
            return

        __ len(cur)/2 == n/2:
            ret.append("".join(cur))
            return

        for elt in self.map1:
            __ elt != "00" or len(cur) != n-2:
                cur.insert(0, elt[0])
                cur.append(elt[1])
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
        ret = []
        self.build(0, n, [], ret)
        return ret

    ___ build(self, idx, n, cur, ret):
        __ idx == n/2:
            __ n % 2 != 0:
                for m in self.middle:
                    __ m != "0" or idx != 0:
                        temp = list(cur)
                        temp.append(m)
                        for i in xrange(idx-1, -1, -1):
                            temp.append(self.map[temp[i]])
                        ret.append("".join(temp))
            else:
                temp = list(cur)
                for i in xrange(idx-1, -1, -1):
                    temp.append(self.map[temp[i]])
                    ret.append("".join(temp))

            return

        for k in self.map.keys():
            __ k != "0" or idx != 0:
                cur.append(k)
                self.build(idx+1, n, cur, ret)
                cur.pop()


__ __name__ == "__main__":
    assert Solution().findStrobogrammatic(3) == ['101', '609', '808', '906', '111', '619', '818', '916', '181', '689', '888', '986']