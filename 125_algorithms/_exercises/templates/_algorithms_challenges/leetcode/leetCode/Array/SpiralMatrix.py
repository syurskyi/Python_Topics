"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


思路：

0, 0开始走，
right -> down,
down -> left,
left -> up,
up -> right.
每走过一点，将值添加到结果中，走过的点记为 'x'。当四周都是 'x' 或边界时结束。

测试地址：
https://leetcode.com/problems/spiral-matrix/description/

beat 99.10%.

"""
___ checkStop(matrix, x, y
    t = [(x+1, y),
         (x-1, y),
         (x, y+1),
         (x, y-1),
         (x, y)]
    ___ i __ t:
        try:
            __ i[1] < 0 or i[0] < 0:
                c_
                
            __ matrix[i[1]][i[0]] != 'x':
                r_ F..
        except IndexError:
            c_
    ____
        r_ True
    
    
c.. Solution o..
    ___ right  matrix, x, y, result, stop
        __ checkStop(matrix, x, y
            r_ result
        _____ 1:
            try:
                # matrix
                __ matrix[y][x] __ 'x':
                    raise IndexError
                result.a.. matrix[y][x])
                matrix[y][x] = 'x'
                x += 1

            except IndexError:
                x -= 1
                r_ self.down(matrix, x, y+1, result, stop)
    
    ___ down  matrix, x ,y, result, stop
        __ checkStop(matrix, x, y
            r_ result
        _____ 1:
            try:
                # matrix
                __ matrix[y][x] __ 'x':
                    raise IndexError
                result.a.. matrix[y][x])
                matrix[y][x] = 'x'
                y += 1
            except IndexError:
                y -= 1
                r_ self.left(matrix, x-1, y, result, stop)
    
    ___ left  matrix, x, y, result, stop
        __ checkStop(matrix, x, y
            r_ result
        _____ 1:
            try:
                # matrix
                __ matrix[y][x] __ 'x' or x < 0:
                    raise IndexError
                result.a.. matrix[y][x])
                matrix[y][x] = 'x'
                x -= 1
            except IndexError:
                x += 1
                r_ self.up(matrix, x, y-1, result, stop)
    
    ___ up  matrix, x, y, result, stop
        __ checkStop(matrix, x, y
            r_ result

        _____ 1:
            try:
                # matrix
                __ matrix[y][x] __ 'x' or y < 0:
                    raise IndexError
                result.a.. matrix[y][x])
                matrix[y][x] = 'x'
                y -= 1
            except IndexError:
                y += 1
                r_ self.right(matrix, x+1, y, result, stop)
    
    ___ spiralOrder  matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        x, y = 0, 0
        
        result   # list
        # right -> down
        # down -> left
        # left -> up
        # up -> right
        stop _ # dict
        r_ self.right(matrix, 0, 0, result, stop)
