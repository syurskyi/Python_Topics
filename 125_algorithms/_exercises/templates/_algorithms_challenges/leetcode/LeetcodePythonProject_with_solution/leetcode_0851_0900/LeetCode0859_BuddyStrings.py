'''
Created on Sep 16, 2019

@author: tongq
'''
c_ Solution(object):
    ___ buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ l..(a) != l..(b): r.. F..
        __ a __ b a.. l..(set(a)) < l..(a): r.. T..
        dif = [(c1, c2) ___ c1, c2 __ z..(a, b) __ c1 != c2]
        r.. l..(dif) __ 2 a.. dif[0] __ dif[1][::-1]
    
    ___ buddyStrings_own(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ l..(a) != l..(b):
            r.. F..
        c01, c02 = '', ''
        times = 0
        ___ c1, c2 __ z..(a, b):
            __ c1 != c2:
                __ times > 1:
                    r.. F..
                ____ times __ 1:
                    __ c01 __ c2 a.. c02 __ c1:
                        times += 1
                    ____:
                        r.. F..
                ____:
                    c01, c02 = c1, c2
                    times += 1
        __ times __ 0:
            r.. l..(set(a)) < l..(a)
        r.. times __ 2
    
    ___ test
        testCase = [
            ['ab', 'ba'],
            ['ab', 'ab'],
            ['aa', 'aa'],
            ['aaaaaabc', 'aaaaaacb'],
            ['', 'aa'],
        ]
        ___ a, b __ testCase:
            res = buddyStrings(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
