'''
Created on Apr 5, 2018

@author: tongq
'''
c_ Solution(object):
    ___ numJewelsInStones  J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j, s = J, S
        jset = set(l..(j))
        res = 0
        ___ c __ s:
            __ c __ jset:
                res += 1
        r.. res
    
    ___ test
        testCases = [
            [
                'aA',
                'aAAbbbb',
            ],
            [
                'z',
                'ZZ',
            ],
        ]
        ___ j, s __ testCases:
            print('j: %s' % j)
            print('s: %s' % s)
            result = numJewelsInStones(j, s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
