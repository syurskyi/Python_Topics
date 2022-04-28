c_ Solution o..
    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     dmap = [[0] * n for _ in range(m)]
    #     for i in range(m):
    #         if obstacleGrid[i][0] != 1:
    #             dmap[i][0] = 1
    #         else:
    #             break
    #     for j in range(n):
    #         if obstacleGrid[0][j] != 1:
    #             dmap[0][j] = 1
    #         else:
    #             break
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if obstacleGrid[i][j] == 1:
    #                 continue
    #             l = u = 0
    #             if i - 1 >= 0:
    #                 u = dmap[i - 1][j]
    #             if j - 1 >= 0:
    #                 l = dmap[i][j - 1]
    #             dmap[i][j] = l + u
    #     return dmap[m - 1][n - 1]

    ___ uniquePathsWithObstacles  obstacleGrid):
        m, n = l.. obstacleGrid), l.. obstacleGrid[0])
        __ m __ 0:
            r_ 0
        dmap = [[0] * (n + 1) ___ _ __ r.. m + 1)]
        dmap[m - 1][n] = 1
        ___ i __ r.. m - 1, -1, -1):
            ___ j __  r.. n - 1, -1, -1):
                __ obstacleGrid[i][j] __ 1:
                    dmap[i][j] = 0
                ____
                    dmap[i][j] = dmap[i][j + 1] + dmap[i + 1][j]
        r_ dmap[0][0]