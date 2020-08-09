'''
Created on Jan 25, 2017

@author: MT
'''
class Solution(object
    ___ maximalRectangle(self, matrix
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        area = 0
        __ not matrix or not matrix[0]: r_ area
        m, n = le.(matrix), le.(matrix[0])
        heights = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m
            for j in range(n
                __ matrix[i][j] __ '0':
                    heights[i+1][j] = 0
                ____
                    heights[i+1][j] = heights[i][j]+1
        for i in range(m
            area = max(area, self.getArea(heights[i+1]))
        r_ area
    
    ___ getArea(self, heights
        area = 0
        __ not heights: r_ area
        stack = []
        i = 0
        w___ i < le.(heights
            __ not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            ____
                h = heights[stack.pop()]
                w = i __ not stack else i-stack[-1]-1
                area = max(area, h*w)
        r_ area
    
    ___ test(self
        testCases = [
            [
                ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]
            ],
        ]
        for matrix in testCases:
            result = self.maximalRectangle(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
