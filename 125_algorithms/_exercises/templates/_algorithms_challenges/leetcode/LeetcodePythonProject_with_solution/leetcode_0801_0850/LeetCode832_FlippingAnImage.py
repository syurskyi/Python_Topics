'''
Created on Jun 9, 2018

@author: tongq
'''
c_ Solution(object):
    ___ flipAndInvertImage  A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        image = A
        __ n.. image o. n.. image[0]: r..
        m, n = l..(image), l..(image[0])
        ___ i __ r..(m):
            j, l = 0, n-1
            w.... j <= l:
                image[i][j], image[i][l] = image[i][l], image[i][j]
                image[i][j] = 1 __ n.. image[i][j] ____ 0
                __ j < l:
                    image[i][l] = 1 __ n.. image[i][l] ____ 0
                j += 1
                l -= 1
        r.. image
    
    ___ test
        testCases = [
            [[1,1,0],[1,0,1],[0,0,0]],
        ]
        ___ image __ testCases:
            res = flipAndInvertImage(image)
            print('res: %s' % res)

__ _____ __ _____
    Solution().test()
