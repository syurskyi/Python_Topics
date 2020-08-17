'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object
    ___ calPoints(self, ops
        """
        :type ops: List[str]
        :rtype: int
        """
        valids = []
        res = 0
        ___ c in ops:
            __ c __ '+':
                res += valids[-1]+valids[-2]
                valids.append(valids[-1]+valids[-2])
            ____ c __ 'D':
                res += valids[-1]*2
                valids.append(valids[-1]*2)
            ____ c __ 'C':
                d = valids.p..
                res -= d
            ____
                res += int(c)
                valids.append(int(c))
        r_ res
    
    ___ test(self
        testCases = [
#             ["5","2","C","D","+"],
            ["5","-2","4","C","D","9","+","+"],
        ]
        ___ ops in testCases:
            print('ops: %s' % ops)
            result = self.calPoints(ops)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
