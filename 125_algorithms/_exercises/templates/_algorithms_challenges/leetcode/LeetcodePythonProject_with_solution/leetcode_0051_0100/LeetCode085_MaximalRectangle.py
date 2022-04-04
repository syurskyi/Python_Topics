'''
Created on Jan 25, 2017

@author: MT
'''
c_ Solution(o..
    ___ maximalRectangle  matrix
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        area = 0
        __ n.. matrix o. n.. matrix[0]: r.. area
        m, n = l..(matrix), l..(matrix[0])
        heights = [[0]*(n+1) ___ _ __ r..(m+1)]
        ___ i __ r..(m
            ___ j __ r..(n
                __ matrix[i][j] __ '0':
                    heights[i+1][j] = 0
                ____
                    heights[i+1][j] = heights[i][j]+1
        ___ i __ r..(m
            area = m..(area, getArea(heights[i+1]
        r.. area
    
    ___ getArea  heights
        area = 0
        __ n.. heights: r.. area
        stack    # list
        i = 0
        w.... i < l..(heights
            __ n.. stack o. heights[i] >= heights[stack[-1]]:
                stack.a..(i)
                i += 1
            ____
                h = heights[stack.p.. )]
                w = i __ n.. stack ____ i-stack[-1]-1
                area = m..(area, h*w)
        r.. area
    
    ___ test
        testCases = [
            [
                ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]
            ],
        ]
        ___ matrix __ testCases:
            result = maximalRectangle(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
