"""
与今日头条秋招第一题最相似的一道题，只是方向少了四个。

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

passed:
beat 54%.

测试地址：
https://leetcode.com/problems/max-area-of-island/description/

"""

c.. Solution o..
    ___ makeAroundXY  x, y
        r_ ((x, y-1),
                (x, y+1),
                (x-1, y),
                (x+1, y))
    
    ___ maxAreaOfIsland  court
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        fans_groups   # list
        x = 0
        y = 0
        __ n.. court:
            r_ 0
        
        x_length = l..(court[0])
        y_length = l..(court)

        ___ helper(x, y, result=0
            Xy = self.makeAroundXY(x, y)
            ___ i __ Xy:
                try:
                    __ i[0] < 0 or i[1] < 0:
                        c_

                    __ court[i[1]][i[0]] __ 1:
                        court[i[1]][i[0]] = 0
                        result += 1
                        t = helper(i[0], i[1], 0)
                        result += t
                except IndexError:
                    c_
            ____
                r_ result


        ___ y __ r..(y_length
            ___ x __ r..(x_length
                __ court[y][x] __ 1:
                    court[y][x] = 0
                    fans_groups.a.. helper(x, y, 1))

        __ n.. fans_groups:
            r_ 0

        r_ m..(fans_groups)
