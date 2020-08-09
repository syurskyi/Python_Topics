'''
Created on Aug 22, 2017

@author: MT
'''

class Solution(object
    ___ checkRecord(self, s
        """
        :type s: str
        :rtype: bool
        """
        absent = False
        for i, c in enumerate(s
            __ c __ 'A':
                __ not absent:
                    absent = True
                ____
                    r_ False
            ____ c __ 'L':
                __ i > 1 and s[i-1] __ 'L' and s[i-2] __ 'L':
                    r_ False
        r_ True
    
    ___ test(self
        testCases = [
            'PPALLP',
            'PPALLL',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.checkRecord(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
