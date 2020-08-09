'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object
    ___ slidingPuzzle(self, board
        """
        :type board: List[List[int]]
        :rtype: int
        """
        s = ''.join([str(n) ___ n in board[0]])+''.join([str(n) ___ n in board[1]])
        visited = set([s])
        target = '123450'
        queue = [s]
        res = 0
        w___ queue:
            size = le.(queue)
            ___ _ in range(size
                s = queue.pop(0)
                __ s __ target:
                    r_ res
                i = s.index('0')
                ___ j in [i+1, i-1, i+3, i-3]:
                    __ j < 0 or j > 5 or\
                        (i __ 2 and j __ 3) or\
                        (i __ 3 and j __ 2
                        continue
                    arr = list(s)
                    arr[i], arr[j] = arr[j], arr[i]
                    newS = ''.join(arr)
                    __ newS not in visited:
                        visited.add(newS)
                        queue.append(newS)
            res += 1
        r_ -1
    
    ___ getZero(self, board
        ___ i in range(2
            ___ j in range(3
                __ board[i][j] __ 0:
                    r_ i, j
    
    ___ test(self
        testCases = [
            [[1,2,3],[4,0,5]],
            [[1,2,3],[5,4,0]],
            [[4,1,2],[5,0,3]],
            [[3,2,4],[1,5,0]],
        ]
        ___ board in testCases:
            print('board')
            print('\n'.join([str(row) ___ row in board]))
            result = self.slidingPuzzle(board)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
