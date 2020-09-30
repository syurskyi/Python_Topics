'''
Created on Nov 12, 2017

@author: MT
'''
class Solution(object
    ___ findMinStep(self, board, hand
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        self.MAXCOUNT = 6
        handCount = [0]*26
        ___ c __ hand:
            handCount[ord(c)-ord('A')] += 1
        res = self.helper(board+'#', handCount)
        r_ res __ res != float('inf') else -1
    
    ___ helper(self, s, h
        s = self.removeConsecutive(s)
        __ s __ '#': r_ 0
        res = float('inf')
        i, j = 0, 0
        w___ j < le.(s
            __ s[j] __ s[i]:
                j += 1
                continue
            need = 3-(j-i)
            __ h[ord(s[i])-ord('A')] >= need:
                h[ord(s[i])-ord('A')] -= need
                res = min(res, need+self.helper(s[:i]+s[j:], h))
                h[ord(s[i])-ord('A')] += need
            i = j
            j += 1
        r_ res
    
    ___ removeConsecutive(self, board
        i, j = 0, 0
        w___ j < le.(board
            __ board[j] __ board[i]:
                j += 1
                continue
            __ j-i >= 3:
                r_ self.removeConsecutive(board[:i]+board[j:])
            ____
                i = j
            j += 1
        r_ board
    
    ___ test(self
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
        ___ board, hand __ testCases:
            print('board: %s' % board)
            print('hand: %s' % hand)
            result = self.findMinStep(board, hand)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
