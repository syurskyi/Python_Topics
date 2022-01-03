c_ Solution(object):
  ___ computeArea(self, A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    area = (C - A) * (D - B) + (G - E) * (H - F)
    overlap = max(m..(C, G) - max(A, E), 0) * max(m..(D, H) - max(B, F), 0)
    r.. area - overlap
