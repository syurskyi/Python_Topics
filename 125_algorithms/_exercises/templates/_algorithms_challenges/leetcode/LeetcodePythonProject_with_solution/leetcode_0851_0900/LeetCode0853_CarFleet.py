'''
Created on Sep 10, 2019

@author: tongq
'''
class Solution(object):
    ___ carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [float(target-p)/s ___ p, s __ s..(zip(position, speed))]
        res = cur = 0
        ___ t __ time[::-1]:
            __ t > cur:
                res += 1
                cur = t
        r.. res
    
    ___ test(self):
        testCases = [
            [
                12,
                [10, 8, 0, 5, 3],
                [2, 4, 1, 1, 3],
            ],
        ]
        ___ target, position, speed __ testCases:
            res = self.carFleet(target, position, speed)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
