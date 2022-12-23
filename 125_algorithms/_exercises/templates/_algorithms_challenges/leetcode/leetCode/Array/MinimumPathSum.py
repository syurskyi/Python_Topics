"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum

给一个二维数组，里面全是非负整数，找到一条左上到右下花费最小的路线。

思路：
当前点只要加 up 和 left 中较小的一个即可。

效率 O(n)

为了判断边界直接顺着思路写了。优化的话可以先把最上面的一排按其左的数相加，最左边的一列按其上面的数相加。
然后从 [1,1] 开始，这样不需要判断边界，写法上可以少点判断效率能提高10+ms。

测试地址：
https://leetcode.com/problems/minimum-path-sum/description/

"""
c.. Solution o..
    ___ get_up_left  x, y
        __ y-1 < 0:
            up = False
        ____
            up = (x, y-1)
        __ x-1 < 0:
            left = False
        ____
            left = (x-1,y)
            
        # up and left
        r_ (up, left)
    
    ___ minPathSum  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        ___ i __ r..(l..(grid)):
            ___ j __ r..(l..(grid[0])):
                xy = self.get_up_left(j, i)
                up = grid[xy[0][1]][xy[0][0]] __ xy[0] else float('inf')
                left = grid[xy[1][1]][xy[1][0]] __ xy[1] else float('inf')
                
                __ up __ float('inf') a.. left __ float('inf'
                    c_
                grid[i][j] = grid[i][j] + m.. up, left)
                
                
        r_ grid[-1][-1]