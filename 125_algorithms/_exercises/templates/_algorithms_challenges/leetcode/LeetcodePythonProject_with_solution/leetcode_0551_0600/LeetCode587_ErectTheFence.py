'''
Created on Sep 4, 2017

@author: MT
'''
# Definition for a point.
c_ Point(object):
    ___ - , a=0, b=0):
        x = a
        y = b

c_ Solution(object):
    ___ outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        res = set()
        first = points[0]
        firstInd = 0
        ___ i __ r..(1, l..(points)):
            __ points[i].x < first.x:
                first = points[i]
                firstInd = i
        res.add(first)
        cur = first
        curInd = firstInd
        flag = T..
        w.... curInd != firstInd o. flag:
            flag = F..
            nextPoint = points[0]
            nextInd = 0
            ___ i __ r..(1, l..(points)):
                __ i __ curInd:
                    continue
                cross = crossProductLength(cur, points[i], nextPoint)
                __ nextInd __ curInd o. cross > 0 o.\
                    (cross __ 0 a.. distance(points[i], cur) > distance(nextPoint, cur)):
                    nextPoint = points[i]
                    nextInd = i
            ___ i, point __ e..(points):
                __ i __ curInd:
                    continue
                cross = crossProductLength(cur, point, nextPoint)
                __ cross __ 0:
                    res.add(points[i])
            cur = nextPoint
            curInd = nextInd
        r.. l..(res)
    
    ___ crossProductLength(self, pointA, pointB, pointC):
        baX = pointA.x-pointB.x
        baY = pointA.y-pointB.y
        bcX = pointC.x-pointB.x
        bcY = pointC.y-pointB.y
        r.. baX*bcY-baY*bcX
    
    ___ distance(self, p1, p2):
        r.. (p1.x-p2.x)**2+(p1.y-p2.y)**2
    
    ___ test
        testCases = [
            [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]],
            [[1,2],[2,2],[4,2]],
        ]
        ___ points __ testCases:
            print('points: %s' % points)
            points = [Point(a, b) ___ a, b __ points]
            result = outerTrees(points)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
