'''
Created on Sep 4, 2017

@author: MT
'''
# Definition for a point.
class Point(object):
    ___ __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    ___ outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        res = set()
        first = points[0]
        firstInd = 0
        for i in range(1, len(points)):
            __ points[i].x < first.x:
                first = points[i]
                firstInd = i
        res.add(first)
        cur = first
        curInd = firstInd
        flag = True
        while curInd != firstInd or flag:
            flag = False
            nextPoint = points[0]
            nextInd = 0
            for i in range(1, len(points)):
                __ i == curInd:
                    continue
                cross = self.crossProductLength(cur, points[i], nextPoint)
                __ nextInd == curInd or cross > 0 or\
                    (cross == 0 and self.distance(points[i], cur) > self.distance(nextPoint, cur)):
                    nextPoint = points[i]
                    nextInd = i
            for i, point in enumerate(points):
                __ i == curInd:
                    continue
                cross = self.crossProductLength(cur, point, nextPoint)
                __ cross == 0:
                    res.add(points[i])
            cur = nextPoint
            curInd = nextInd
        return list(res)
    
    ___ crossProductLength(self, pointA, pointB, pointC):
        baX = pointA.x-pointB.x
        baY = pointA.y-pointB.y
        bcX = pointC.x-pointB.x
        bcY = pointC.y-pointB.y
        return baX*bcY-baY*bcX
    
    ___ distance(self, p1, p2):
        return (p1.x-p2.x)**2+(p1.y-p2.y)**2
    
    ___ test(self):
        testCases = [
            [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]],
            [[1,2],[2,2],[4,2]],
        ]
        for points in testCases:
            print('points: %s' % points)
            points = [Point(a, b) for a, b in points]
            result = self.outerTrees(points)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
