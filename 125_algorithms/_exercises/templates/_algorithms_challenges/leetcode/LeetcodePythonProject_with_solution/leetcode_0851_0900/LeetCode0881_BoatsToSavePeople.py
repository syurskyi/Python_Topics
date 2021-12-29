'''
Created on Oct 15, 2019

@author: tongq
'''
class Solution(object):
    ___ numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l, r = 0, l..(people)-1
        res = 0
        while l <= r:
            w = people[r]
            __ l < r and w + people[l] <= limit:
                l += 1
            res += 1
            r -= 1
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [3,2,3,2,2],
                6,
            ],
            [
                [1,2], 3,
            ],
            [
                [3,2,2,1], 3,
            ],
            [
                [3,5,3,4], 5,
            ],
        ]
        ___ people, limit __ testCases:
            res = self.numRescueBoats(people, limit)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
