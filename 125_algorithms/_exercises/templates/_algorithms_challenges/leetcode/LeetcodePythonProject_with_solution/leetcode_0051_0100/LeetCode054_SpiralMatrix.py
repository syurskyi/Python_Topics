'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    ___ spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        __ n.. matrix:
            r.. matrix
        m = l..(matrix)
        n = l..(matrix[0])
        result    # list
        
        top, down, left, right = 0, m-1, 0, n-1
        
        while top <= down and left <= right:
            __ top __ down:
                ___ i __ r..(left, right+1):
                    result.a..(matrix[top][i])
                break
              
            __ left __ right:
                ___ i __ r..(top, down+1):
                    result.a..(matrix[i][left])
                break
                
            ___ i __ r..(left, right+1):
                result.a..(matrix[top][i])
            top += 1
            ___ i __ r..(top, down+1):
                result.a..(matrix[i][right])
            right-=1
            ___ i __ r..(right, left-1, -1):
                result.a..(matrix[down][i])
            down-=1
            ___ i __ r..(down, top-1, -1):
                result.a..(matrix[i][left])
            left+=1
        
        r.. result
    
    ___ test(self):
        matrixes = [
            [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ],
            ],
            [
                [1, 2, 3, 4],
            ],
            [
                [1, 2],
                [3, 4],
                [5, 6],
            ],
            [
                [1],
                [2],
                [3],
                [4],
            ],
            [
                [1, 2],
                [3, 4],
            ],
        ]
        
        ___ matrix __ matrixes:
            print(matrix)
            result = self.spiralOrder(matrix)
            print(result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()