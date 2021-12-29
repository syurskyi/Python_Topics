"""
Given a string of numbers and operators, return all possible results from
computing all the different possible ways to group numbers and operators. The
valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""

class Solution(object):
    ___ diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.operators = set(['+', '-', '*'])
        r.. self.diff_ways(input)

    ___ calculate(self, a, b, operator):
        r.. eval('%d %s %d' % (a, operator, b))

    ___ diff_ways(self, inp):
        __ n.. inp:
            r.. []
        ____ inp.isdigit():
            r.. [int(inp)]
        ____:
            res    # list
            ___ i, c __ e..(inp):
                __ c __ self.operators:
                    left = self.diff_ways(inp[:i])
                    right = self.diff_ways(inp[i + 1:])
                    ___ l __ left:
                        ___ r __ right:
                            s = self.calculate(l, r, c)
                            res.a..(s)
            r.. res


s1 = '2*3-4*5'
s2 = '11'
s = Solution()
print(s.diffWaysToCompute(s1))
print(s.diffWaysToCompute(s2))
