from math import sqrt

__author__ = 'randy'


class Distance:
    def distance2d(self, pts0: [], pts1: []):
        a = pts1[0] - pts0[0]
        b = pts1[1] - pts0[1]
        c_squared = a * a + b * b
        c = sqrt(c_squared)
        return c

    def distance3d(self, pts0: [], pts1: []):
        a = pts1[0] - pts0[0]
        b = pts1[1] - pts0[1]
        c = pts1[2] - pts0[2]
        d_squared = a * a + b * b + c * c
        d = sqrt(d_squared)
        return d
