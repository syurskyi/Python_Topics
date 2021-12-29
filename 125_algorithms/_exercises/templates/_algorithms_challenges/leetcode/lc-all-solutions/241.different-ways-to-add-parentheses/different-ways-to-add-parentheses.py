____ operator _______ *


class Solution(object):
  ___ diffWaysToCompute(self, input):
    """
    :type input: str
    :rtype: List[int]
    """
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    ans    # list
    ___ i, c __ e..(input):
      __ c __ ops:
        left = self.diffWaysToCompute(input[:i])
        right = self.diffWaysToCompute(input[i + 1:])
        ans.extend([ops[c](a, b) ___ a __ left ___ b __ right])
    r.. ans __ ans ____ [int(input)]
