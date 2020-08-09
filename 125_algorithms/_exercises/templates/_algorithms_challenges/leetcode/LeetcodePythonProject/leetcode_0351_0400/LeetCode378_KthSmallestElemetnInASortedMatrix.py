'''
Created on Apr 1, 2017

@author: MT
'''

class Solution(object
    ___ kthSmallest(self, matrix, k
        lower, upper = matrix[0][0], matrix[-1][-1]
        w___ lower < upper:
            mid = (lower+upper)//2
            __ self.count(matrix, mid) < k:
                lower = mid+1
            ____
                upper = mid
        r_ upper
    
    ___ count(self, matrix, target
        m, n = le.(matrix), le.(matrix[0])
        i, j = m-1, 0
        count = 0
        w___ i >= 0 and j < n:
            __ matrix[i][j] <= target:
                count += i+1
                j += 1
            ____
                i -= 1
        r_ count
    
    ___ test(self
        matrix = [
            [ 1,  5,  9],
            [10, 11, 13],
            [12, 13, 15],
        ]
        nums = [1, 5, 9, 10, 13]
        ___ num in nums:
            print('num: %s' % num)
            print('count: %s' % self.count(matrix, num))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
