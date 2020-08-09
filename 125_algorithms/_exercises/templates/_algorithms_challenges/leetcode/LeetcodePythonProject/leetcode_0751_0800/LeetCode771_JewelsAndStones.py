'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object
    ___ numJewelsInStones(self, J, S
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j, s = J, S
        jset = set(list(j))
        res = 0
        ___ c in s:
            __ c in jset:
                res += 1
        r_ res
    
    ___ test(self
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
        ___ j, s in testCases:
            print('j: %s' % j)
            print('s: %s' % s)
            result = self.numJewelsInStones(j, s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
