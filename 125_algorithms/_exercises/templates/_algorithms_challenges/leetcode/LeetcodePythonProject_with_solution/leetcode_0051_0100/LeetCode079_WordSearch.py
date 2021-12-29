'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    ___ exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        __ n.. board o. n.. word:
            r.. False
        m = l..(board)
        n = l..(board[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ self.helper(board, word, 0, i, j):
                    r.. True
        r.. False
    
    ___ helper(self, board, word, start, i, j):
        __ i < 0 o. j < 0 o. i >= l..(board) o. j >= l..(board[0]):
            r.. False
        __ word[start] __ board[i][j]:
            __ start __ l..(word)-1:
                r.. True
            tmp = board[i][j]
            board[i][j] = '#'
            result = False
            __ self.helper(board, word, start+1, i+1, j) o.\
                self.helper(board, word, start+1, i, j+1) o.\
                self.helper(board, word, start+1, i-1, j) o.\
                self.helper(board, word, start+1, i, j-1):
                result = True
            board[i][j] = tmp
            __ result:
                r.. True
        r.. False
    
    ___ test(self):
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
            result = self.exist(board, word)
            print('result: %s' % (result))
            print('-='*15+'-')
        

__ __name__ __ '__main__':
    Solution().test()
