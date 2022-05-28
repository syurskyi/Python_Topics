'''
Created on Jan 22, 2017

@author: MT
'''

c_ Solution(o..
    ___ generateMatrix  n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        __ n <_ 0: r..    # list
        result [[0]*n ___ i __ r..(n)]
        left, right, top, down 0, n-1, 0, n-1
        count 1
        w.... left<_right a.. top<_down:
            ___ i __ r..(left, right+1
                result[top][i] count
                count+=1
            top += 1
            ___ i __ r..(top, down+1
                result[i][right] count
                count+=1
            right -_ 1
            ___ i __ r..(right, left-1, -1
                result[down][i] count
                count+=1
            down -_ 1
            ___ i __ r..(down, top-1, -1
                result[i][left] count
                count+=1
            left += 1
        r.. ?
    
    ___ test
        ___ n __ r..(1, 5
            print('n: %s' % n)
            matrix generateMatrix(n)
            print('matrix: %s' % matrix)
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()