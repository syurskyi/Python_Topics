"""
与今日头条的秋招第一题差不多的题：
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

分析看 FootbalFans.py

passed.

测试地址：
https://leetcode.com/problems/number-of-islands/description/

"""
c.. Solution o..
    ___ makeXY  x, y
        r_ ((x, y-1),
                (x, y+1),
                (x-1, y),
                (x+1, y))
    
    ___ numIslands  court
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

        ___ helper(x, y
            Xy = self.makeXY(x, y)
            ___ i __ Xy:
                try:
                    __ i[1] < 0 or i[0] < 0:
                        c_
                        
                    __ court[i[1]][i[0]] __ '1':
                        court[i[1]][i[0]] = '0'
                        t = helper(i[0], i[1])
                except IndexError:
                    c_
            ____
                r_ 1


        ___ y __ r..(y_length
            ___ x __ r..(x_length
                __ court[y][x] __ '1':
                    court[y][x] = '0'
                    fans_groups.append(helper(x, y))



        __ n.. fans_groups:
            r_ 0

        r_ l..(fans_groups)

