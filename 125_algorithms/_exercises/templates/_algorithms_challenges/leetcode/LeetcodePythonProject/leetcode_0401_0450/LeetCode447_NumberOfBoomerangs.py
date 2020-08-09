'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object
    ___ numberOfBoomerangs(self, points
        n = le.(points)
        res = 0
        ___ i in range(n
            hashmap = {}
            point1 = points[i]
            ___ j in range(n
                point2 = points[j]
                diff = (point2[1]-point1[1])**2+(point2[0]-point1[0])**2
                hashmap[diff] = hashmap.get(diff, 0)+1
            ___ val in hashmap.values(
                res += val*(val-1)
        r_ res
    
    ___ test(self
        testCases = [
            [[0,0],[1,0],[2,0]],
        ]
        ___ points in testCases:
            print('points: %s' % points)
            result = self.numberOfBoomerangs(points)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
