c_ Solution o..
    ___ computeArea  A, B, C, D, E, F, G, H):
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
        # sum of areas of two rectangles
        result = (C - A) * (D - B) + (G - E) * (H - F)
        # no overlap
        __ (C <= E or G <= A or H <= B or D <= F):
            r_ result
        # overlap length on x
        dx = min(C, G) - max(A, E)
        # overlap length on y
        dy = min(D, H) - max(B, F)
        r_ result - dx * dy
