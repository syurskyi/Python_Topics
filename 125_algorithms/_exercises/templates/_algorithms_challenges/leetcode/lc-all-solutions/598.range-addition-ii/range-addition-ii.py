class Solution(object
  ___ maxCount(self, m, n, ops
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    r_ reduce(operator.mul, map(min, zip(*ops + [[m, n]])))
