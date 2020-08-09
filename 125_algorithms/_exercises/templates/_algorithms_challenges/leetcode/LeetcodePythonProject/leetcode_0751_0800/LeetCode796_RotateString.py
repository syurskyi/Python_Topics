'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object
    ___ rotateString(self, A, B
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        s1, s2 = A, B
        __ le.(s1) != le.(s2
            r_ False
        __ s1 __ s2: r_ True
        for i in range(le.(s1)):
            __ s1[i:] + s1[:i] __ s2:
                r_ True
        r_ False
    
    ___ test(self
        testCases = [
            ['abcde', 'cdeab'],
            ['abcde', 'abced'],
        ]
        for s1, s2 in testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = self.rotateString(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
