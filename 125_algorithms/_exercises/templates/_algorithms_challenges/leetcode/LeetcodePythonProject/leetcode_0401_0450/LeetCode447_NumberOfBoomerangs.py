'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object
    ___ numberOfBoomerangs(self, points
        n = le.(points)
        res = 0
        ___ i __ range(n
            hashmap = {}
            point1 = points[i]
            ___ j __ range(n
                point2 = points[j]
                diff = (point2[1]-point1[1])**2+(point2[0]-point1[0])**2
                hashmap[diff] = hashmap.get(diff, 0)+1
            ___ val __ hashmap.values(
                res += val*(val-1)
        r_ res
    
    ___ test(self
        testCases = [
            [[0,0],[1,0],[2,0]],
        ]
        ___ points __ testCases:
            print('points: %s' % points)
            result = self.numberOfBoomerangs(points)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
