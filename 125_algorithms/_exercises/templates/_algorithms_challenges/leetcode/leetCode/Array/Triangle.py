"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

从底到顶，min(self+right)。

O(1) 空间。

beat
99%

测试地址：
https://leetcode.com/problems/triangle/description/



"""
c.. Solution o..
    ___ minimumTotal  triangle
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        ___ i __ r..(l..(triangle)-2, -1, -1
            length = l..(triangle[i])
            ___ j __ r..(length

                _right = triangle[i+1][j+1] 
                _self = triangle[i+1][j]
                mins = min(_right, _self)
                triangle[i][j] += mins
        r_ min(triangle[0])
