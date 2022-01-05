'''
Created on Jan 24, 2017

@author: MT
'''

c_ Solution(o..):
    ___ exist  board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        __ n.. board o. n.. word:
            r.. F..
        m = l..(board)
        n = l..(board[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ helper(board, word, 0, i, j):
                    r.. T..
        r.. F..
    
    ___ helper  board, word, start, i, j):
        __ i < 0 o. j < 0 o. i >= l..(board) o. j >= l..(board[0]):
            r.. F..
        __ word[start] __ board[i][j]:
            __ start __ l..(word)-1:
                r.. T..
            tmp = board[i][j]
            board[i][j] = '#'
            result = F..
            __ helper(board, word, start+1, i+1, j) o.\
                helper(board, word, start+1, i, j+1) o.\
                helper(board, word, start+1, i-1, j) o.\
                helper(board, word, start+1, i, j-1):
                result = T..
            board[i][j] = tmp
            __ result:
                r.. T..
        r.. F..
    
    ___ test
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E'],
        ]
        words = [
            'ABCCED',
            'SEE',
            'ABCB',
        ]
#         board = [
#             ['a'],
#         ]
#         words = [
#             'a',
#         ]
        ___ word __ words:
            print('word: %s' % (word))
            result = exist(board, word)
            print('result: %s' % (result))
            print('-='*15+'-')
        

__ _____ __ _____
    Solution().test()
