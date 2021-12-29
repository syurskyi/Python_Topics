'''
Created on Sep 16, 2019

@author: tongq
'''
class Solution(object):
    ___ buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ l..(a) != l..(b): r.. False
        __ a __ b and l..(set(a)) < l..(a): r.. True
        dif = [(c1, c2) ___ c1, c2 __ zip(a, b) __ c1 != c2]
        r.. l..(dif) __ 2 and dif[0] __ dif[1][::-1]
    
    ___ buddyStrings_own(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ l..(a) != l..(b):
            r.. False
        c01, c02 = '', ''
        times = 0
        ___ c1, c2 __ zip(a, b):
            __ c1 != c2:
                __ times > 1:
                    r.. False
                ____ times __ 1:
                    __ c01 __ c2 and c02 __ c1:
                        times += 1
                    ____:
                        r.. False
                ____:
                    c01, c02 = c1, c2
                    times += 1
        __ times __ 0:
            r.. l..(set(a)) < l..(a)
        r.. times __ 2
    
    ___ test(self):
        testCase = [
            ['ab', 'ba'],
            ['ab', 'ab'],
            ['aa', 'aa'],
            ['aaaaaabc', 'aaaaaacb'],
            ['', 'aa'],
        ]
        ___ a, b __ testCase:
            res = self.buddyStrings(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
