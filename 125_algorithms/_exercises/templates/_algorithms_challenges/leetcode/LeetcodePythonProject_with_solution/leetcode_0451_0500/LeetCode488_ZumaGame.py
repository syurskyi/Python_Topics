'''
Created on Nov 12, 2017

@author: MT
'''
class Solution(object):
    ___ findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        self.MAXCOUNT = 6
        handCount = [0]*26
        for c in hand:
            handCount[ord(c)-ord('A')] += 1
        res = self.helper(board+'#', handCount)
        return res __ res != float('inf') else -1
    
    ___ helper(self, s, h):
        s = self.removeConsecutive(s)
        __ s == '#': return 0
        res = float('inf')
        i, j = 0, 0
        while j < len(s):
            __ s[j] == s[i]:
                j += 1
                continue
            need = 3-(j-i)
            __ h[ord(s[i])-ord('A')] >= need:
                h[ord(s[i])-ord('A')] -= need
                res = min(res, need+self.helper(s[:i]+s[j:], h))
                h[ord(s[i])-ord('A')] += need
            i = j
            j += 1
        return res
    
    ___ removeConsecutive(self, board):
        i, j = 0, 0
        while j < len(board):
            __ board[j] == board[i]:
                j += 1
                continue
            __ j-i >= 3:
                return self.removeConsecutive(board[:i]+board[j:])
            else:
                i = j
            j += 1
        return board
    
    ___ test(self):
        testCases = [
            [
                "WRRBBW",
                "RB",
            ],
            [
                "WWRRBBWW",
                "WRBRW",
            ],
            [
                "G",
                "GGGGG",
            ],
            [
                "RBYYBBRRB",
                "YRBGB",
            ],
        ]
        for board, hand in testCases:
            print('board: %s' % board)
            print('hand: %s' % hand)
            result = self.findMinStep(board, hand)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
