'''
Created on Mar 7, 2018

@author: tongq
'''
c_ Solution(o..
    ___ floodFill  image, sr, sc, newColor
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor image[sr][sc]
        __ oldColor __ newColor:
            r.. image
        helper(image, sr, sc, oldColor, newColor)
        r.. image
    
    ___ helper  image, i, j, oldColor, newColor
        m, n l..(image), l..(image 0
        image[i][j] newColor
        ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1
            __ 0 <_ x < m a.. 0 <_ y < n a.. image[x][y] __ oldColor:
                helper(image, x, y, oldColor, newColor)
    
    ___ test
        testCases [
            [
                [
                    [1,1,1],
                    [1,1,0],
                    [1,0,1],
                ],
                1,
                1,
                2
            ],
        ]
        ___ image, sr, sc, newColor __ testCases:
            result floodFill(image, sr, sc, newColor)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
