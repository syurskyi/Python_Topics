'''
Created on Apr 27, 2017

@author: MT
'''

c_ Solution(o..
    ___ findRadius  houses, heaters
        houses.s..()
        heaters.s..()
        i 0
        radius 0
        ___ house __ houses:
            w.... i+1 < l..(heaters) a.. heaters[i+1] < house:
                i += 1
            __ heaters[i] > house:
                tmp  heaters[i]-house
            ____
                tmp  house-heaters[i]
                __ i+1 < l..(heaters
                    tmp  m.. ? heaters[i+1]-house)
            radius m..(radius, tmp)
        r.. radius
    
    ___ test
        testCases [
            [
                [1, 2, 3],
                [2],
            ],
            [
                [1, 2, 3, 4],
                [1, 4],
            ],
        ]
        ___ houses, heaters __ testCases:
            print('houses: %s' % houses)
            print('heaters: %s' % heaters)
            result findRadius(houses, heaters)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
