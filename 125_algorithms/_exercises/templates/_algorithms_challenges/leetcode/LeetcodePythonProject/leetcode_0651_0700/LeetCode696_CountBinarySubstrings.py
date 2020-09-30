'''
Created on Oct 25, 2017

@author: MT
'''
class Solution(object
    ___ countBinarySubstrings(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s: r_ 0
        res = 0
        i = 0
        ind = i
        w___ i+1 < le.(s) and s[i+1] __ s[ind]:
            i += 1
        prev = i+1-ind
        i += 1
        w___ i < le.(s
            ind = i
            w___ i+1 < le.(s) and s[i+1] __ s[ind]:
                i += 1
            curr = i+1-ind
            res += min(curr, prev)
            prev = curr
            i += 1
        r_ res
    
    ___ test(self
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

__  -n __ '__main__':
    Solution().test()
