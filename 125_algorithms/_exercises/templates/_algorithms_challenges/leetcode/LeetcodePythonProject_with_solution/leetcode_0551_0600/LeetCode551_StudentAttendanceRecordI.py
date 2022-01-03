'''
Created on Aug 22, 2017

@author: MT
'''

c_ Solution(object):
    ___ checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = F..
        ___ i, c __ e..(s):
            __ c __ 'A':
                __ n.. absent:
                    absent = T..
                ____:
                    r.. F..
            ____ c __ 'L':
                __ i > 1 a.. s[i-1] __ 'L' a.. s[i-2] __ 'L':
                    r.. F..
        r.. T..
    
    ___ test
        testCases = [
            'PPALLP',
            'PPALLL',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = checkRecord(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
