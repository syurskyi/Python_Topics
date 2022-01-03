'''
Created on Apr 5, 2018

@author: tongq
'''
c_ Solution(object):
    ___ slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        s = ''.j..([s..(n) ___ n __ board[0]])+''.j..([s..(n) ___ n __ board[1]])
        visited = set([s])
        target = '123450'
        queue = [s]
        res = 0
        w.... queue:
            size = l..(queue)
            ___ _ __ r..(size):
                s = queue.pop(0)
                __ s __ target:
                    r.. res
                i = s.index('0')
                ___ j __ [i+1, i-1, i+3, i-3]:
                    __ j < 0 o. j > 5 o.\
                        (i __ 2 a.. j __ 3) o.\
                        (i __ 3 a.. j __ 2):
                        continue
                    arr = l..(s)
                    arr[i], arr[j] = arr[j], arr[i]
                    newS = ''.j..(arr)
                    __ newS n.. __ visited:
                        visited.add(newS)
                        queue.a..(newS)
            res += 1
        r.. -1
    
    ___ getZero(self, board):
        ___ i __ r..(2):
            ___ j __ r..(3):
                __ board[i][j] __ 0:
                    r.. i, j
    
    ___ test
        testCases = [
            [[1,2,3],[4,0,5]],
            [[1,2,3],[5,4,0]],
            [[4,1,2],[5,0,3]],
            [[3,2,4],[1,5,0]],
        ]
        ___ board __ testCases:
            print('board')
            print('\n'.j..([s..(row) ___ row __ board]))
            result = slidingPuzzle(board)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
