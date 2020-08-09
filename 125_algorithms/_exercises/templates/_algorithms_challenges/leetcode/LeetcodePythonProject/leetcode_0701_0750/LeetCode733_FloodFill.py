'''
Created on Mar 7, 2018

@author: tongq
'''
class Solution(object
    ___ floodFill(self, image, sr, sc, newColor
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        __ oldColor __ newColor:
            r_ image
        self.helper(image, sr, sc, oldColor, newColor)
        r_ image
    
    ___ helper(self, image, i, j, oldColor, newColor
        m, n = le.(image), le.(image[0])
        image[i][j] = newColor
        ___ x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1
            __ 0 <= x < m and 0 <= y < n and image[x][y] __ oldColor:
                self.helper(image, x, y, oldColor, newColor)
    
    ___ test(self
        testCases = [
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
        ___ image, sr, sc, newColor in testCases:
            result = self.floodFill(image, sr, sc, newColor)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
