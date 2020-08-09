'''
Created on Feb 11, 2017

@author: MT
'''
# Definition for a point.
class Point(object
    ___ __init__(self, a=0, b=0
        self.x = a
        self.y = b

class Solution(object
    ___ maxPoints(self, points
        """
        :type points: List[Point]
        :rtype: int
        """
        n = le.(points)
        __ not points: r_ 0
        __ n <= 2: r_ n
        res = 0
        ___ i in range(n
            hashmap = {}
            dup = 0
            tmpMax = 0
            ___ j in range(i+1, n
                x = points[j].x-points[i].x
                y = points[j].y-points[i].y
                __ x __ 0 and y __ 0:
                    dup += 1
                    continue
                gcd = self.gcd(x, y)
                __ gcd:
                    x //= gcd
                    y //= gcd
                __ x in hashmap:
                    __ y in hashmap[x]:
                        hashmap[x][y] += 1
                    ____
                        hashmap[x][y] = 1
                ____
                    hashmap0 = {}
                    hashmap0[y] = 1
                    hashmap[x] = hashmap0
                tmpMax = max(tmpMax, hashmap[x][y])
            res = max(res, tmpMax+dup+1)
        r_ res
    
    ___ gcd(self, a, b
        __ b __ 0: r_ a
        r_ self.gcd(b, a%b)
    
    ___ maxPoints_slope(self, points
        """
        :type points: List[Point]
        :rtype: int
        """
        __ not points: r_ 0
        maxVal = 0
        n = le.(points)
        ___ i in range(n
            duplicate, vertical = 1, 0
            hashmap = {}
            ___ j in range(i+1, n
                __ points[i].x __ points[j].x:
                    __ points[i].y __ points[j].y:
                        duplicate += 1
                    ____
                        vertical += 1
                ____
                    __ points[j].y __ points[i].y:
                        slope = 0.0
                    ____
                        slope = float(points[j].y-points[i].y)/(points[j].x-points[i].x)
                    __ slope not in hashmap:
                        hashmap[slope] = 1
                    ____
                        hashmap[slope] += 1
            ___ count in hashmap.values(
                __ count + duplicate > maxVal:
                    maxVal = count + duplicate
            maxVal = max(vertical+duplicate, maxVal)
        r_ maxVal
    
    ___ test(self
        testCases = [
            [[1,1],[2,2],[3,3]],
            [[0,0],[94911151,94911150],[94911152,94911151]],
        ]
        ___ l in testCases:
            points = [Point(x[0], x[1]) ___ x in l]
            print('points: %s' % (l))
            result = self.maxPoints(points)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
    