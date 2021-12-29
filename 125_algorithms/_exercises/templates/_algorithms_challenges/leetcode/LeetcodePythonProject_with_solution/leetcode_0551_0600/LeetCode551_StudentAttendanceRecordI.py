'''
Created on Aug 22, 2017

@author: MT
'''

class Solution(object):
    ___ checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = False
        ___ i, c __ enumerate(s):
            __ c __ 'A':
                __ n.. absent:
                    absent = True
                ____:
                    r.. False
            ____ c __ 'L':
                __ i > 1 and s[i-1] __ 'L' and s[i-2] __ 'L':
                    r.. False
        r.. True
    
    ___ test(self):
        testCases = [
            'PPALLP',
            'PPALLL',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.checkRecord(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
