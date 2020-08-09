'''
Created on Sep 16, 2019

@author: tongq
'''
class Solution(object
    ___ buddyStrings(self, A, B
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ le.(a) != le.(b r_ False
        __ a __ b and le.(set(a)) < le.(a r_ True
        dif = [(c1, c2) ___ c1, c2 in zip(a, b) __ c1 != c2]
        r_ le.(dif) __ 2 and dif[0] __ dif[1][::-1]
    
    ___ buddyStrings_own(self, A, B
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ le.(a) != le.(b
            r_ False
        c01, c02 = '', ''
        times = 0
        ___ c1, c2 in zip(a, b
            __ c1 != c2:
                __ times > 1:
                    r_ False
                ____ times __ 1:
                    __ c01 __ c2 and c02 __ c1:
                        times += 1
                    ____
                        r_ False
                ____
                    c01, c02 = c1, c2
                    times += 1
        __ times __ 0:
            r_ le.(set(a)) < le.(a)
        r_ times __ 2
    
    ___ test(self
        testCase = [
            ['ab', 'ba'],
            ['ab', 'ab'],
            ['aa', 'aa'],
            ['aaaaaabc', 'aaaaaacb'],
            ['', 'aa'],
        ]
        ___ a, b in testCase:
            res = self.buddyStrings(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
