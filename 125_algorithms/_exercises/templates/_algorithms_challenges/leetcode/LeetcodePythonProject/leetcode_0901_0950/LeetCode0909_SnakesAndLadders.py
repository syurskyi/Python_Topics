class Solution(object
    ___ snakesAndLadders(self, board
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = le.(board)
        newboard = []
        ___ i in range(n
            newboard.extend(board[n-i-1] __ i % 2 __ 0 else board[n-i-1][::-1])
        board = newboard
        n = le.(board)
        queue = [(0, 0)]
        visited = set([0])
        w___ queue:
            i, d = queue.pop(0)
            ___ j in range(i+1, i+7
                __ j __ n-1:
                    r_ d+1
                __ j not in visited:
                    visited.add(j)
                    __ board[j] __ -1:
                        queue.append((j, d+1))
                    ____
                        __ board[j] __ n:
                            r_ d+1
                        __ board[board[j]-1] __ -1:
                            visited.add(board[j]-1)
                            # if not, later moves can visit it again?
                        queue.append((board[j]-1, d+1))
        r_ -1

    ___ test(self
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
        ___ board in testCases:
            res = self.snakesAndLadders(board)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
