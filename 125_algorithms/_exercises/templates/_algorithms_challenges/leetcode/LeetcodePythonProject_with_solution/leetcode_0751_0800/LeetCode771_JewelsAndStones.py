'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object):
    ___ numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j, s = J, S
        jset = set(list(j))
        res = 0
        for c in s:
            __ c in jset:
                res += 1
        return res
    
    ___ test(self):
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
        for j, s in testCases:
            print('j: %s' % j)
            print('s: %s' % s)
            result = self.numJewelsInStones(j, s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
