c_ Solution o..
    ___ generateMatrix  n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n ___ _ __ r.. n)]
        pos = [0, 0]
        move = (0, 1)
        ___ index __ r.. 1, n * n + 1):
            res[pos[0]][pos[1]] = index
            __ res[(pos[0] + move[0]) % n][(pos[1] + move[1]) % n] > 0:
                # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
                move = (move[1], -1 * move[0])
            pos[0] = pos[0] + move[0]
            pos[1] = pos[1] + move[1]
        r_ res

__ ____ __ ____
    # begin
    s  ?
    print s.generateMatrix(2)