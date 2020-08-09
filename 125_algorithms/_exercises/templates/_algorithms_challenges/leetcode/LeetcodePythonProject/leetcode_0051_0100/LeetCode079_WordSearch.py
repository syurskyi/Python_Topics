'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object
    ___ exist(self, board, word
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        __ not board or not word:
            r_ False
        m = le.(board)
        n = le.(board[0])
        ___ i in range(m
            ___ j in range(n
                __ self.helper(board, word, 0, i, j
                    r_ True
        r_ False
    
    ___ helper(self, board, word, start, i, j
        __ i < 0 or j < 0 or i >= le.(board) or j >= le.(board[0]
            r_ False
        __ word[start] __ board[i][j]:
            __ start __ le.(word)-1:
                r_ True
            tmp = board[i][j]
            board[i][j] = '#'
            result = False
            __ self.helper(board, word, start+1, i+1, j) or\
                self.helper(board, word, start+1, i, j+1) or\
                self.helper(board, word, start+1, i-1, j) or\
                self.helper(board, word, start+1, i, j-1
                result = True
            board[i][j] = tmp
            __ result:
                r_ True
        r_ False
    
    ___ test(self
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
        ___ word in words:
            print('word: %s' % (word))
            result = self.exist(board, word)
            print('result: %s' % (result))
            print('-='*15+'-')
        

__ __name__ __ '__main__':
    Solution().test()
