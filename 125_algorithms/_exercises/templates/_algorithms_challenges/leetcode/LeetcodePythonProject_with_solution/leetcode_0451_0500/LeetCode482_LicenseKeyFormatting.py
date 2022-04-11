'''
Created on May 3, 2017

@author: MT
'''

c_ Solution(o..
    ___ licenseKeyFormatting  S, K
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res ''
        count 0
        ___ i __ r..(l..(S)-1, -1, -1
            __ S[i] != '-':
                res S[i].u.. + res
                count += 1
                __ count > 0 a.. count % K __ 0:
                    res '-' + res
        r.. res.l..('-')
    
    ___ test
        testCases [
            ('abc-abc', 3),
        ]
        ___ s, k __ testCases:
            result licenseKeyFormatting(s, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
