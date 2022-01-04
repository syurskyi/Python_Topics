'''
Created on May 3, 2017

@author: MT
'''

c_ Solution(object):
    ___ licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ''
        count = 0
        ___ i __ r..(l..(S)-1, -1, -1):
            __ S[i] != '-':
                res = S[i].u.. + res
                count += 1
                __ count > 0 a.. count % K __ 0:
                    res = '-' + res
        r.. res.lstrip('-')
    
    ___ test
        testCases = [
            ('abc-abc', 3),
        ]
        ___ s, k __ testCases:
            result = licenseKeyFormatting(s, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
