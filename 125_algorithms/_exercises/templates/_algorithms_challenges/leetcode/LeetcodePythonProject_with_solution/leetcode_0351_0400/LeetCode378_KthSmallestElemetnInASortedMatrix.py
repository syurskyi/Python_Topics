'''
Created on Apr 1, 2017

@author: MT
'''

c_ Solution(o..
    ___ kthSmallest  matrix, k
        lower, upper = matrix[0][0], matrix[-1][-1]
        w.... lower < upper:
            mid = (lower+upper)//2
            __ c.. matrix, mid) < k:
                lower = mid+1
            ____:
                upper = mid
        r.. upper
    
    ___ c.. self, matrix, target
        m, n = l..(matrix), l..(matrix[0])
        i, j = m-1, 0
        count = 0
        w.... i >= 0 a.. j < n:
            __ matrix[i][j] <= target:
                count += i+1
                j += 1
            ____:
                i -= 1
        r.. count
    
    ___ test
        matrix = [
            [ 1,  5,  9],
            [10, 11, 13],
            [12, 13, 15],
        ]
        nums = [1, 5, 9, 10, 13]
        ___ num __ nums:
            print('num: %s' % num)
            print('count: %s' % c.. matrix, num))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
