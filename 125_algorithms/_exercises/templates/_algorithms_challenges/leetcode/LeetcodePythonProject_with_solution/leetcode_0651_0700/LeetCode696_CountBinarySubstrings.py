'''
Created on Oct 25, 2017

@author: MT
'''
class Solution(object):
    ___ countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s: r.. 0
        res = 0
        i = 0
        ind = i
        while i+1 < l..(s) and s[i+1] __ s[ind]:
            i += 1
        prev = i+1-ind
        i += 1
        while i < l..(s):
            ind = i
            while i+1 < l..(s) and s[i+1] __ s[ind]:
                i += 1
            curr = i+1-ind
            res += m..(curr, prev)
            prev = curr
            i += 1
        r.. res
    
    ___ test(self):
        testCases = [
#             '00110011',
#             '10101',
            "00100",
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.countBinarySubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
