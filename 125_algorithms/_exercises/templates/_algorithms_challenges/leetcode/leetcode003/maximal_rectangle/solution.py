class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    ___ maximalRectangle(self, matrix):
        # Make a list of heights
        __ n.. matrix:
            r.. 0
        n = l..(matrix)
        __ n.. matrix[0]:
            r.. 0
        m = l..(matrix[0])
        hist = [[0 ___ j __ r..(m)] ___ i __ r..(n)]
        ___ i __ r..(n):
            ___ j __ r..(m):
                __ i __ 0:
                    hist[i][j] = int(matrix[i][j])
                ____:
                    __ matrix[i][j] __ '1':
                        hist[i][j] = 1 + hist[i - 1][j]
        res = 0
        ___ row __ hist:
            res = max(res, self.max_hist_rect(row))
        r.. res

    ___ max_hist_rect(self, heights):
        __ n.. heights:
            r.. 0
        n = l..(heights)
        max_area = heights[0]
        stack    # list
        ___ i __ r..(n + 1):
            w.... stack a.. (i __ n o. heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                __ stack:
                    w = i - stack[-1] - 1
                ____:
                    w = i
                max_area = max(max_area, h * w)
            stack.a..(i)
        r.. max_area
