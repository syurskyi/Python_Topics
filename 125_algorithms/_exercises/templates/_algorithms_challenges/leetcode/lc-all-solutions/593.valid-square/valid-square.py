class Solution(object
  ___ validSquare(self, p1, p2, p3, p4
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    dist = lambda a, b: ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    sideLens = set([dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)])
    __ le.(sideLens) != 2 or 0 in sideLens:
      r_ False
    r_ True
