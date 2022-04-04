'''
Created on Nov 12, 2017

@author: MT
'''
c_ Solution(o..
    ___ findMinStep  board, hand
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        MAXCOUNT = 6
        handCount = [0]*26
        ___ c __ hand:
            handCount[o..(c)-o..('A')] += 1
        res = helper(board+'#', handCount)
        r.. res __ res != f__('inf') ____ -1
    
    ___ helper  s, h
        s = removeConsecutive(s)
        __ s __ '#': r.. 0
        res = f__('inf')
        i, j = 0, 0
        w.... j < l..(s
            __ s[j] __ s[i]:
                j += 1
                _____
            need = 3-(j-i)
            __ h[o..(s[i])-o..('A')] >= need:
                h[o..(s[i])-o..('A')] -= need
                res = m..(res, need+helper(s[:i]+s[j:], h
                h[o..(s[i])-o..('A')] += need
            i = j
            j += 1
        r.. res
    
    ___ removeConsecutive  board
        i, j = 0, 0
        w.... j < l..(board
            __ board[j] __ board[i]:
                j += 1
                _____
            __ j-i >= 3:
                r.. removeConsecutive(board[:i]+board[j:])
            ____
                i = j
            j += 1
        r.. board
    
    ___ test
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
            result = findMinStep(board, hand)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
