c_ Solution(o..):
    ___ snakesAndLadders  board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = l..(board)
        newboard    # list
        ___ i __ r..(n):
            newboard.extend(board[n-i-1] __ i % 2 __ 0 ____ board[n-i-1][::-1])
        board = newboard
        n = l..(board)
        queue = [(0, 0)]
        visited = set([0])
        w.... queue:
            i, d = queue.pop(0)
            ___ j __ r..(i+1, i+7):
                __ j __ n-1:
                    r.. d+1
                __ j n.. __ visited:
                    visited.add(j)
                    __ board[j] __ -1:
                        queue.a..((j, d+1))
                    ____:
                        __ board[j] __ n:
                            r.. d+1
                        __ board[board[j]-1] __ -1:
                            visited.add(board[j]-1)
                            # if not, later moves can visit it again?
                        queue.a..((board[j]-1, d+1))
        r.. -1

    ___ test
        testCases = [
            [[-1, 1, 2,-1],
             [2, 13,15,-1],
             [-1,10,-1,-1],
             [-1, 6, 2,8]],

            [[-1,7,-1],
             [-1,6,9],
             [-1,-1,2]],

            [[-1,-1,-1],
             [-1,9,8],
             [-1,8,9]],

            [[-1,4,-1],
             [6,2,6],
             [-1,3,-1]],

            [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]],

            [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]],
        ]
        ___ board __ testCases:
            res = snakesAndLadders(board)
            print('res: %s' % res)
            print('-='*30+'-')


__ _____ __ _____
    Solution().test()
