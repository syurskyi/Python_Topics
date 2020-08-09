'''
Created on May 3, 2017

@author: MT
'''

class Solution(object
    ___ licenseKeyFormatting(self, S, K
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ''
        count = 0
        ___ i in range(le.(S)-1, -1, -1
            __ S[i] != '-':
                res = S[i].upper() + res
                count += 1
                __ count > 0 and count % K __ 0:
                    res = '-' + res
        r_ res.lstrip('-')
    
    ___ test(self
        testCases = [
            ('abc-abc', 3),
        ]
        ___ s, k in testCases:
            result = self.licenseKeyFormatting(s, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
