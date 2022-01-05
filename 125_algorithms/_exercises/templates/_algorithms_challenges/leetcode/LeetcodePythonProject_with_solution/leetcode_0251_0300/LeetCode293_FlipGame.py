'''
Created on Mar 8, 2017

@author: MT
'''

c_ Solution(o..):
    ___ generatePossibleNextMoves  s):
        result    # list
        ___ i __ r..(1, l..(s)):
            __ s[i-1] __ '+' a.. s[i] __ '+':
                result.a..(s[:i-1]+'--'+s[i+1:])
        r.. result
    
    ___ test
        testCases = [
            '++++',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = generatePossibleNextMoves(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
