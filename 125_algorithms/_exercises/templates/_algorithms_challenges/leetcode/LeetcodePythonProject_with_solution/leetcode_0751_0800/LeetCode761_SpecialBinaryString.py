'''
Created on Mar 31, 2018

@author: tongq
'''
c_ Solution(object):
    ___ makeLargestSpecial  S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        i = 0
        res    # list
        ___ j, c __ e..(S):
            count = count+1 __ c__'1' ____ count-1
            __ count __ 0:
                res.a..('1'+makeLargestSpecial(S[i+1:j])+'0')
                i = j+1
        r.. ''.j..(s..(res, reverse=T..))
    
    ___ test
        testCases = [
            '11011000',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = makeLargestSpecial(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
