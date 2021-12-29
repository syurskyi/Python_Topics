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
        __ not board or not word:
            return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                __ self.helper(board, word, 0, i, j):
                    return True
        return False
    
    ___ helper(self, board, word, start, i, j):
        __ i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        __ word[start] == board[i][j]:
            __ start == len(word)-1:
                return True
            tmp = board[i][j]
            board[i][j] = '#'
            result = False
            __ self.helper(board, word, start+1, i+1, j) or\
                self.helper(board, word, start+1, i, j+1) or\
                self.helper(board, word, start+1, i-1, j) or\
                self.helper(board, word, start+1, i, j-1):
                result = True
            board[i][j] = tmp
            __ result:
                return True
        return False
    
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
        for word in words:
            print('word: %s' % (word))
            result = self.exist(board, word)
            print('result: %s' % (result))
            print('-='*15+'-')
        

__ __name__ == '__main__':
    Solution().test()
