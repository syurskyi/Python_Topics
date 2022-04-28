c_ Solution o..
    ___ setZeroes  matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        __ not matrix:
            r_
        m = l.. matrix)
        __ m __ 0:
            r_
        r = []
        c = []
        n = l.. matrix[0])
        ___ i __ r.. m):
            ___ j __ r.. n):
                __ matrix[i][j] __ 0:
                    r.append(i)
                    c.append(j)
        # row with zero
        r = set(r)
        # column with zero
        c = set(c)
        ___ i __ r:
            ___ j __ r.. n):
                matrix[i][j] = 0
        ___ i __ r.. m):
            ___ j __ c:
                matrix[i][j] = 0
