'''
Created on Jun 9, 2018

@author: tongq
'''
class Solution(object
    ___ flipAndInvertImage(self, A
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        image = A
        __ not image or not image[0]: r_
        m, n = le.(image), le.(image[0])
        ___ i in range(m
            j, l = 0, n-1
            w___ j <= l:
                image[i][j], image[i][l] = image[i][l], image[i][j]
                image[i][j] = 1 __ not image[i][j] else 0
                __ j < l:
                    image[i][l] = 1 __ not image[i][l] else 0
                j += 1
                l -= 1
        r_ image
    
    ___ test(self
        testCases = [
            [[1,1,0],[1,0,1],[0,0,0]],
        ]
        ___ image in testCases:
            res = self.flipAndInvertImage(image)
            print('res: %s' % res)

__ __name__ __ '__main__':
    Solution().test()
