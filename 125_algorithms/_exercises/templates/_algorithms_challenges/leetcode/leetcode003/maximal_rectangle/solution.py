class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    ___ maximalRectangle(self, matrix
        # Make a list of heights
        __ not matrix:
            r_ 0
        n = le.(matrix)
        __ not matrix[0]:
            r_ 0
        m = le.(matrix[0])
        hist = [[0 for j in range(m)] for i in range(n)]
        for i in range(n
            for j in range(m
                __ i __ 0:
                    hist[i][j] = int(matrix[i][j])
                ____
                    __ matrix[i][j] __ '1':
                        hist[i][j] = 1 + hist[i - 1][j]
        res = 0
        for row in hist:
            res = max(res, self.max_hist_rect(row))
        r_ res

    ___ max_hist_rect(self, heights
        __ not heights:
            r_ 0
        n = le.(heights)
        max_area = heights[0]
        stack = []
        for i in range(n + 1
            w___ stack and (i __ n or heights[stack[-1]] > heights[i]
                h = heights[stack.pop()]
                __ stack:
                    w = i - stack[-1] - 1
                ____
                    w = i
                max_area = max(max_area, h * w)
            stack.append(i)
        r_ max_area
