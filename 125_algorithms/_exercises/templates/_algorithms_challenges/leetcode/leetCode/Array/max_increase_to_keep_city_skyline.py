"""
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

测试用例：
https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

整体思路：
获取出x和y轴的最大值，然后逐个遍历。

时间复杂度 O(mn)。

"""

c.. Solution o..
    ___ maxIncreaseKeepingSkyline  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = l..(grid[0])
        
        # Get line max.
        line_dict = {str(indexmax(data) ___ index, data __ enumerate(grid)}
        # Get column max.
        column_dict = {str(indexmax((grid[index2][index] ___ index2 __ r..(l..(grid)))) ___ index __ r..(length)}
        
        total_increases = 0
        
        ___ index, line __ enumerate(grid
            ___ index2, cell __ enumerate(line
                total_increases += min([line_dict[str(index)], column_dict[str(index2)]]) - cell
        
        r_ total_increases