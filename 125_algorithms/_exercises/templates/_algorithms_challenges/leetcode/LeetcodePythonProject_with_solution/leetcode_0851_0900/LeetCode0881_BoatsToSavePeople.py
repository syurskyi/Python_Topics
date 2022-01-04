'''
Created on Oct 15, 2019

@author: tongq
'''
c_ Solution(object):
    ___ numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.s..()
        l, r = 0, l..(people)-1
        res = 0
        w.... l <= r:
            w = people[r]
            __ l < r a.. w + people[l] <= limit:
                l += 1
            res += 1
            r -= 1
        r.. res
    
    ___ test
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
            res = numRescueBoats(people, limit)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
