____ operator _______ *


c_ Solution(object):
  ___ diffWaysToCompute  input):
    """
    :type input: str
    :rtype: List[int]
    """
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    ans    # list
    ___ i, c __ e..(input):
      __ c __ ops:
        left = diffWaysToCompute(input[:i])
        right = diffWaysToCompute(input[i + 1:])
        ans.extend([ops[c](a, b) ___ a __ left ___ b __ right])
    r.. ans __ ans ____ [i..(input)]
