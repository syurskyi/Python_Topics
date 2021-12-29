'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object):
    ___ numberOfBoomerangs(self, points):
        n = l..(points)
        res = 0
        ___ i __ r..(n):
            hashmap = {}
            point1 = points[i]
            ___ j __ r..(n):
                point2 = points[j]
                diff = (point2[1]-point1[1])**2+(point2[0]-point1[0])**2
                hashmap[diff] = hashmap.get(diff, 0)+1
            ___ val __ hashmap.values():
                res += val*(val-1)
        r.. res
    
    ___ test(self):
        testCases = [
            [[0,0],[1,0],[2,0]],
        ]
        ___ points __ testCases:
            print('points: %s' % points)
            result = self.numberOfBoomerangs(points)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
