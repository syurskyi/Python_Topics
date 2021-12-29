class Solution(object):
  ___ validSquare(self, p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    dist = l.... a, b: ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    sideLens = set([dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)])
    __ l..(sideLens) != 2 o. 0 __ sideLens:
      r.. False
    r.. True
