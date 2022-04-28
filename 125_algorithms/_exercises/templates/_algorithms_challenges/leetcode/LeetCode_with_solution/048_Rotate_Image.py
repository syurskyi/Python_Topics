c_ Solution o..
    ___ rotate  matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # rotate from outside to inside
        __ matrix is N.. or l.. matrix) __ 1:
            r_
        ls = l.. matrix)
        ___ i __ r.. ls / 2):
            # border
            begin, end = i, ls - 1 - i
            ___ k __ r.. ls - 2 * i - 1):
                temp = matrix[end - k][begin]
                matrix[end - k][begin] = matrix[end][end - k]
                matrix[end][end - k] = matrix[begin + k][end]
                matrix[begin + k][end] = matrix[begin][begin + k]
                matrix[begin][begin + k] = temp
        r_

__ ____ __ ____
    # begin
    s  ?
    s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])




