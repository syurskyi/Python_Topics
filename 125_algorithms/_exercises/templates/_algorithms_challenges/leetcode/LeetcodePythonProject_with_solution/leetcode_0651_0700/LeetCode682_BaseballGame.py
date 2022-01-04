'''
Created on Oct 21, 2017

@author: MT
'''
c_ Solution(object):
    ___ calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valids    # list
        res = 0
        ___ c __ ops:
            __ c __ '+':
                res += valids[-1]+valids[-2]
                valids.a..(valids[-1]+valids[-2])
            ____ c __ 'D':
                res += valids[-1]*2
                valids.a..(valids[-1]*2)
            ____ c __ 'C':
                d = valids.pop()
                res -= d
            ____:
                res += i..(c)
                valids.a..(i..(c))
        r.. res
    
    ___ test
        testCases = [
#             ["5","2","C","D","+"],
            ["5","-2","4","C","D","9","+","+"],
        ]
        ___ ops __ testCases:
            print('ops: %s' % ops)
            result = calPoints(ops)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
