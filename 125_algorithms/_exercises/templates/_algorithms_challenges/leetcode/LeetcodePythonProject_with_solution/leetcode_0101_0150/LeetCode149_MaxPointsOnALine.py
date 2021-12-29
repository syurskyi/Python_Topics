'''
Created on Feb 11, 2017

@author: MT
'''
# Definition for a point.
class Point(object):
    ___ __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    ___ maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = l..(points)
        __ n.. points: r.. 0
        __ n <= 2: r.. n
        res = 0
        ___ i __ r..(n):
            hashmap = {}
            dup = 0
            tmpMax = 0
            ___ j __ r..(i+1, n):
                x = points[j].x-points[i].x
                y = points[j].y-points[i].y
                __ x __ 0 a.. y __ 0:
                    dup += 1
                    continue
                gcd = self.gcd(x, y)
                __ gcd:
                    x //= gcd
                    y //= gcd
                __ x __ hashmap:
                    __ y __ hashmap[x]:
                        hashmap[x][y] += 1
                    ____:
                        hashmap[x][y] = 1
                ____:
                    hashmap0 = {}
                    hashmap0[y] = 1
                    hashmap[x] = hashmap0
                tmpMax = max(tmpMax, hashmap[x][y])
            res = max(res, tmpMax+dup+1)
        r.. res
    
    ___ gcd(self, a, b):
        __ b __ 0: r.. a
        r.. self.gcd(b, a%b)
    
    ___ maxPoints_slope(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        __ n.. points: r.. 0
        maxVal = 0
        n = l..(points)
        ___ i __ r..(n):
            duplicate, vertical = 1, 0
            hashmap = {}
            ___ j __ r..(i+1, n):
                __ points[i].x __ points[j].x:
                    __ points[i].y __ points[j].y:
                        duplicate += 1
                    ____:
                        vertical += 1
                ____:
                    __ points[j].y __ points[i].y:
                        slope = 0.0
                    ____:
                        slope = float(points[j].y-points[i].y)/(points[j].x-points[i].x)
                    __ slope n.. __ hashmap:
                        hashmap[slope] = 1
                    ____:
                        hashmap[slope] += 1
            ___ count __ hashmap.values():
                __ count + duplicate > maxVal:
                    maxVal = count + duplicate
            maxVal = max(vertical+duplicate, maxVal)
        r.. maxVal
    
    ___ test(self):
        testCases = [
            [[1,1],[2,2],[3,3]],
            [[0,0],[94911151,94911150],[94911152,94911151]],
        ]
        ___ l __ testCases:
            points = [Point(x[0], x[1]) ___ x __ l]
            print('points: %s' % (l))
            result = self.maxPoints(points)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
    