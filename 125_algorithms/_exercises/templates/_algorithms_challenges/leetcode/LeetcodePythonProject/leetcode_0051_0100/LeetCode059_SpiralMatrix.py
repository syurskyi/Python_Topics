'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object
    ___ generateMatrix(self, n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        __ n <= 0: r_ []
        result = [[0]*n ___ i in range(n)]
        left, right, top, down = 0, n-1, 0, n-1
        count = 1
        w___ left<=right and top<=down:
            ___ i in range(left, right+1
                result[top][i] = count
                count+=1
            top += 1
            ___ i in range(top, down+1
                result[i][right] = count
                count+=1
            right -= 1
            ___ i in range(right, left-1, -1
                result[down][i] = count
                count+=1
            down -= 1
            ___ i in range(down, top-1, -1
                result[i][left] = count
                count+=1
            left += 1
        r_ result
    
    ___ test(self
        ___ n in range(1, 5
            print('n: %s' % n)
            matrix = self.generateMatrix(n)
            print('matrix: %s' % matrix)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()