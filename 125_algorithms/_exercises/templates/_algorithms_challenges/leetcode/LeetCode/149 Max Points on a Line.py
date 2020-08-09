"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
__author__ = 'Danyang'
#Definition for a point
class Point:
    ___ __init__(self, a=0, b=0
        """

        :param a: int
        :param b: int
        :return:
        """
        self.x = a
        self.y = b

class Solution:
    ___ maxPoints_complicated(self, points
        """

        :param points: a list of Points
        :return: int
        """

        hash_map = {}  # key -> inner_dict, where key = (k, b), inner_dict is index -> list

        length = le.(points)
        for i in xrange(length
            for j in xrange(i+1, length
                point1 = points[i]
                point2 = points[j]
                __ point1.x __ point2.x:
                    key = (1 << 32, point1.x)
                ____
                    slope = float(point1.y-point2.y)/(point1.x-point2.x)
                    intersection = slope*point1.x - point1.y

                    slope = int(slope*1000) # avoid numeric errors
                    intersection = int(intersection*1000) # avoid numeric errors

                    key = (slope, intersection)  # only tuples can be hashed, whereas lists cannot

                __ key not in hash_map:
                    hash_map[key] = [0 for _ in points]
                hash_map[key][i] = 1  # avoid duplicate
                hash_map[key][j] = 1


        __ (length<=1
            r_ length

        __(le.(hash_map)__0
            r_ 0

        maxa = -1<<32
        for key, item in hash_map.items(
            # current = le.(filter(lambda x: x==1, item)) # increase complexity
            current = item.count(1)
            __ current>maxa:
                maxa = current

        r_ maxa

    ___ maxPoints(self, points
        """
        reference: http://fisherlei.blogspot.sg/2013/12/leetcode-max-points-on-line-solution.html
        :param points: a list of Points
        :return: int
        """
        maxa = -1<<32
        length = le.(points)
        __ (length<=1
            r_ length

        for i in xrange(length
            hash_map = {}
            duplicate = 1 # point_i itself
            for j in xrange(length
                __ i__j:
                    continue

                point1 = points[i]
                point2 = points[j]
                __ point1.x__point2.x and point1.y__point2.y:
                    duplicate += 1
                    continue
                __ point1.x__point2.x:
                    key = 1<<32
                ____
                    slope = float(point1.y-point2.y)/(point1.x-point2.x)
                    slope = int(slope*10000) # avoid numeric errors
                    # no need to calculate intersection. During this iteration, all lines pass point1
                    key = slope

                __ key not in hash_map:
                    hash_map[key] = 0
                hash_map[key]+=1


            __ hash_map:
                max_key = max(hash_map, key=hash_map.get)
                max_value = hash_map[max_key]
            ____
                max_value  = 0
            maxa = max(maxa, max_value+duplicate)

        r_ maxa






__ __name____"__main__":
    points = [(560, 248), (0, 16), (30, 250), (950, 187), (630, 277), (950, 187), (-212, -268), (-287, -222), (53, 37),
              (-280, -100), (-1, -14), (-5, 4), (-35, -387), (-95, 11), (-70, -13), (-700, -274), (-95, 11), (-2, -33),
              (3, 62), (-4, -47), (106, 98), (-7, -65), (-8, -71), (-8, -147), (5, 5), (-5, -90), (-420, -158),
              (-420, -158), (-350, -129), (-475, -53), (-4, -47), (-380, -37), (0, -24), (35, 299), (-8, -71), (-2, -6),
              (8, 25), (6, 13), (-106, -146), (53, 37), (-7, -128), (-5, -1), (-318, -390), (-15, -191), (-665, -85),
              (318, 342), (7, 138), (-570, -69), (-9, -4), (0, -9), (1, -7), (-51, 23), (4, 1), (-7, 5), (-280, -100),
              (700, 306), (0, -23), (-7, -4), (-246, -184), (350, 161), (-424, -512), (35, 299), (0, -24), (-140, -42),
              (-760, -101), (-9, -9), (140, 74), (-285, -21), (-350, -129), (-6, 9), (-630, -245), (700, 306), (1, -17),
              (0, 16), (-70, -13), (1, 24), (-328, -260), (-34, 26), (7, -5), (-371, -451), (-570, -69), (0, 27),
              (-7, -65), (-9, -166), (-475, -53), (-68, 20), (210, 103), (700, 306), (7, -6), (-3, -52), (-106, -146),
              (560, 248), (10, 6), (6, 119), (0, 2), (-41, 6), (7, 19), (30, 250)]

    points = [Point(point[0], point[1]) for point in points]
    print Solution().maxPoints(points)
    assert Solution().maxPoints(points)__22