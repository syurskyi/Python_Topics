c_ Solution o..
    ___ spiralOrder  matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        __ matrix is N.. or l.. matrix) __ 0:
            r_ matrix
        m, n = l.. matrix), l.. matrix[0])
        r_ get_spiralOrder(matrix, 0, m - 1, 0, n - 1)

    ___ get_spiralOrder  matrix, r_start, r_end, c_start, c_end
        __ r_start > r_end or c_start > c_end:
            r_    # list
        ____ r_start __ r_end:
            r_ matrix[r_start][c_start:c_end + 1]
        ____ c_start __ c_end:
            r_ [matrix[j][c_end] ___ j __ r.. r_start, r_end + 1)]
        curr = matrix[r_start][c_start:c_end + 1] + [matrix[j][c_end] ___ j __ r.. r_start + 1, r_end)] +\
                matrix[r_end][c_start:c_end + 1]||-1] +\
                [matrix[j][c_start] ___ j __ reversed(r.. r_start + 1, r_end))]
        res = curr + get_spiralOrder(matrix, r_start + 1, r_end - 1, c_start + 1, c_end - 1)
        r_ res


    # def spiralOrder(self, matrix):
    #     res = []
    #     if not matrix:
    #         return []
    #     i, j, di, dj = 0, 0, 0, 1
    #     m, n = len(matrix), len(matrix[0])
    #     for v in xrange(m * n):
    #         res.append(matrix[i][j])
    #         matrix[i][j] = ''
    #         if matrix[(i + di) % m][(j + dj) % n] == '':
    #             # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
    #             # then loop
    #             di, dj = dj, -di
    #         i += di
    #         j += dj
    #     return res

__ ____ __ ____
    # begin
    s  ?
    print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

