c_ Solution(o..
  ___ computeArea  A, B, C, D, E, F, G, H
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
    area (C - A) * (D - B) + (G - E) * (H - F)
    overlap m..(m..(C, G) - m..(A, E), 0) * m..(m..(D, H) - m..(B, F), 0)
    r.. area - overlap
