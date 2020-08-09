'''
Created on Apr 15, 2018

@author: tongq
'''
class Solution(object
    ___ customSortString(self, S, T
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s, t = S, T
        count = [0]*26
        ___ c in t:
            count[ord(c)-ord('a')] += 1
        res = ''
        ___ c in s:
            w___ count[ord(c)-ord('a')] > 0:
                res += c
                count[ord(c)-ord('a')] -= 1
        ___ i in range(26
            w___ count[i] > 0:
                res += chr(i+ord('a'))
                count[i] -= 1
        r_ res
    
    ___ test(self
        testCases = [
            ['cba', 'abcd'],
            ["kqep", "pekeq"],
            ["exv", "xwvee"],
        ]
        ___ s, t in testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result = self.customSortString(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
