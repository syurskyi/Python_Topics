'''
Created on Apr 18, 2017

@author: MT
'''

c_ Solution(o..
    ___ numberOfBoomerangs  points
        n l..(points)
        res 0
        ___ i __ r..(n
            hashmap    # dict
            point1 points[i]
            ___ j __ r..(n
                point2 points[j]
                diff (point2[1]-point1[1])**2+(point2[0]-point1[0])**2
                hashmap[diff] hashmap.g.. diff, 0)+1
            ___ val __ hashmap.v..
                res += val*(val-1)
        r.. res
    
    ___ test
        testCases [
            [[0,0],[1,0],[2,0]],
        ]
        ___ points __ testCases:
            print('points: %s' % points)
            result numberOfBoomerangs(points)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
