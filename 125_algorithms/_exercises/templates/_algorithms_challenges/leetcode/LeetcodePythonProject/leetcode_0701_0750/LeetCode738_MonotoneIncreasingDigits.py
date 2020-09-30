'''
Created on Mar 14, 2018

@author: tongq
'''
class Solution(object
    ___ monotoneIncreasingDigits(self, N
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        i = 0
        w___ i < le.(s)-1 and s[i] <= s[i+1]:
            i += 1
        __ i __ le.(s)-1:
            r_ N
        w___ i > 0 and s[i-1] __ s[i]:
            i -= 1
        res = s[:i]
        res += str(int(s[i])-1)
        res += '9'*(le.(s)-i-1)
        res = res.lstrip('0')
        r_ int(res) __ res != '' else 0
    
    ___ test(self
        testCases = [
            10,
            1111,
            1234,
            332,
            1234502468,
            989998,
        ]
        ___ N __ testCases:
            print('N: %s' % N)
            result = self.monotoneIncreasingDigits(N)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
