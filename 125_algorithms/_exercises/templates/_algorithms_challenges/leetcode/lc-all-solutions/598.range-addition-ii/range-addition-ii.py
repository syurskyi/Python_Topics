class Solution(object):
  ___ maxCount(self, m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    r.. reduce(operator.mul, map(m.., zip(*ops + [[m, n]])))
