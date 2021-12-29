'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object):
    ___ rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        s1, s2 = A, B
        __ l..(s1) != l..(s2):
            r.. False
        __ s1 __ s2: r.. True
        ___ i __ r..(l..(s1)):
            __ s1[i:] + s1[:i] __ s2:
                r.. True
        r.. False
    
    ___ test(self):
        testCases = [
            ['abcde', 'cdeab'],
            ['abcde', 'abced'],
        ]
        ___ s1, s2 __ testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = self.rotateString(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
