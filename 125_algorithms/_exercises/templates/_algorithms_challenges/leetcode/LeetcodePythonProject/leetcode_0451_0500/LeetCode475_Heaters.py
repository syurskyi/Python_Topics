'''
Created on Apr 27, 2017

@author: MT
'''

class Solution(object
    ___ findRadius(self, houses, heaters
        houses.sort()
        heaters.sort()
        i = 0
        radius = 0
        ___ house in houses:
            w___ i+1 < le.(heaters) and heaters[i+1] < house:
                i += 1
            __ heaters[i] > house:
                tmp = heaters[i]-house
            ____
                tmp = house-heaters[i]
                __ i+1 < le.(heaters
                    tmp = min(tmp, heaters[i+1]-house)
            radius = max(radius, tmp)
        r_ radius
    
    ___ test(self
        testCases = [
            [
                [1, 2, 3],
                [2],
            ],
            [
                [1, 2, 3, 4],
                [1, 4],
            ],
        ]
        ___ houses, heaters in testCases:
            print('houses: %s' % houses)
            print('heaters: %s' % heaters)
            result = self.findRadius(houses, heaters)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
