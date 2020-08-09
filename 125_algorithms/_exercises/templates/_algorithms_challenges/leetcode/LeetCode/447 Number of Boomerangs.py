#!/usr/bin/python3
"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a
tuple of points (i, j, k) such that the distance between i and j equals the
distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and
coordinates of points are all in the range [-10000, 10000] (inclusive).
"""
from collections ______ Counter


class Solution:
    ___ distance(self, a, b
        r_ (a[0] - b[0])**2 + (a[1] - b[1])**2

    ___ numberOfBoomerangs(self, points
        """
        Reverse look up
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        ___ i in range(le.(points)):
            dist_cnt = Counter()
            ___ j in range(le.(points)):
                __ i != j:
                    d = self.distance(points[i], points[j])
                    dist_cnt[d] += 1

            ___ v in dist_cnt.values(
                # Permutation: P v 2
                ret += v * (v - 1)

        r_ ret

    ___ numberOfBoomerangs_TLE(self, points
        """
        Reverse look up
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        ___ i in range(le.(points)):
            dist_cnt = Counter()
            dist_lst = []
            ___ j in range(le.(points)):
                __ i != j:
                    d = self.distance(points[i], points[j])
                    dist_lst.append(d)
                    dist_cnt[d] += 1

            ___ d in dist_lst:
                ret += (dist_cnt[d] - 1)

        r_ ret


__ __name__ __ "__main__":
    assert Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]) __ 2
