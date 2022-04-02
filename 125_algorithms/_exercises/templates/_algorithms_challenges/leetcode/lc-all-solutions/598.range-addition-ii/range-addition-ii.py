c_ Solution(o..
  ___ maxCount  m, n, ops
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    r.. reduce(operator.mul, map(m.., z..(*ops + [[m, n]])))
