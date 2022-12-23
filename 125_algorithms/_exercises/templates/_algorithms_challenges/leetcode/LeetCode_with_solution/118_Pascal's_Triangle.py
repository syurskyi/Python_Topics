c_ Solution:
    ___ generate  numRows
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result =    # list
        ___ i __ r.. numRows
            result.a.. [0] * (i + 1))
        ___ i __ r.. numRows
            ___ j __ r.. i + 1
                __ j __ 0 or j __ i:
                    result[i][j] = 1
                ____
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        r_ result
