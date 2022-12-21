"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


想清楚在写。

beat 94%

测试地址：
https://leetcode.com/problems/spiral-matrix-ii/description/

"""
c.. Solution o..
        
    ___ generateMatrix  n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        maps = [[0 ___ i __ r..(n)] ___ j __ r..(n)]
        
        current_value = [i ___ i __ r..(1, n*n+1)]
        current_value.reverse()
        
        ___ makeXY(x, y
            # up
            # down
            # right
            # left
            r_ [(x, y-1),
                    (x, y+1),
                    (x+1, y),
                    (x-1, y)]

        ___ right(x, y

            _____ 1:
                __ n.. current_value:
                    r_ maps
                xy = makeXY(x, y)
                __ (y > -1 a.. x > -1) a.. (y < n a.. x < n
                    __ maps[y][x] __ 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[2][1], xy[2][0] 
                    ____
                        # down
                        r_ down(x-1, y+1)
                ____
                    # down
                    r_ down(x-1, y+1)

        ___ down(x, y

            _____ 1:
                __ n.. current_value:
                    r_ maps
                xy = makeXY(x, y)
                __ (y > -1 a.. x > -1) a.. (y < n a.. x < n
                    __ maps[y][x] __ 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[1][1], xy[1][0] 

                    ____
                        # left
                        r_ left(x-1, y-1)
                ____
                    # left
                    r_ left(x-1, y-1)
        ___ left(x, y

            _____ 1:
                __ n.. current_value:
                    r_ maps
                xy = makeXY(x, y)

                __ y > -1 a.. x > -1 a.. y < n a.. x < n:
                    __ maps[y][x] __ 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[3][1], xy[3][0] 
                    ____
                        # up
                        r_ up(x+1, y-1)
                ____
                    # up
                    r_ up(x+1, y-1)
        ___ up(x, y

            _____ 1:
                __ n.. current_value:
                    r_ maps
                xy = makeXY(x, y)
                
                __ y > -1 a.. x > -1 a.. y < n a.. x < n:
                    __ maps[y][x] __ 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[0][1], xy[0][0] 
                    ____
                        # right
                        r_ right(x+1, y+1)
                ____
                    # right
                    r_ right(x+1, y+1)
                
        r_ right(0, 0)
