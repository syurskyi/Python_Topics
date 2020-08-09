from operator ______ *


class Solution(object
  ___ diffWaysToCompute(self, input
    """
    :type input: str
    :rtype: List[int]
    """
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    ans = []
    ___ i, c in enumerate(input
      __ c in ops:
        left = self.diffWaysToCompute(input[:i])
        right = self.diffWaysToCompute(input[i + 1:])
        ans.extend([ops[c](a, b) ___ a in left ___ b in right])
    r_ ans __ ans else [int(input)]
