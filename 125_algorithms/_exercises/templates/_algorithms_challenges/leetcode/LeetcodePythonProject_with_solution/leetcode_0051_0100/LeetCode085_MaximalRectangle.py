'''
Created on Jan 25, 2017

@author: MT
'''
class Solution(object):
    ___ maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        area = 0
        __ n.. matrix o. n.. matrix[0]: r.. area
        m, n = l..(matrix), l..(matrix[0])
        heights = [[0]*(n+1) ___ _ __ r..(m+1)]
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ matrix[i][j] __ '0':
                    heights[i+1][j] = 0
                ____:
                    heights[i+1][j] = heights[i][j]+1
        ___ i __ r..(m):
            area = max(area, self.getArea(heights[i+1]))
        r.. area
    
    ___ getArea(self, heights):
        area = 0
        __ n.. heights: r.. area
        stack    # list
        i = 0
        while i < l..(heights):
            __ n.. stack o. heights[i] >= heights[stack[-1]]:
                stack.a..(i)
                i += 1
            ____:
                h = heights[stack.pop()]
                w = i __ n.. stack ____ i-stack[-1]-1
                area = max(area, h*w)
        r.. area
    
    ___ test(self):
        testCases = [
            [
                ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]
            ],
        ]
        ___ matrix __ testCases:
            result = self.maximalRectangle(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
