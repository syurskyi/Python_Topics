'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object
    ___ spiralOrder(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        __ not matrix:
            r_ matrix
        m = le.(matrix)
        n = le.(matrix[0])
        result = []
        
        top, down, left, right = 0, m-1, 0, n-1
        
        w___ top <= down and left <= right:
            __ top __ down:
                ___ i in range(left, right+1
                    result.append(matrix[top][i])
                break
              
            __ left __ right:
                ___ i in range(top, down+1
                    result.append(matrix[i][left])
                break
                
            ___ i in range(left, right+1
                result.append(matrix[top][i])
            top += 1
            ___ i in range(top, down+1
                result.append(matrix[i][right])
            right-=1
            ___ i in range(right, left-1, -1
                result.append(matrix[down][i])
            down-=1
            ___ i in range(down, top-1, -1
                result.append(matrix[i][left])
            left+=1
        
        r_ result
    
    ___ test(self
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
        
        ___ matrix in matrixes:
            print(matrix)
            result = self.spiralOrder(matrix)
            print(result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()