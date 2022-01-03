#!/usr/bin/python3
"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a
tuple of points (i, j, k) such that the distance between i and j equals the
distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and
coordinates of points are all in the range [-10000, 10000] (inclusive).
"""
____ collections _______ Counter


c_ Solution:
    ___ distance(self, a, b):
        r.. (a[0] - b[0])**2 + (a[1] - b[1])**2

    ___ numberOfBoomerangs(self, points):
        """
        Reverse look up
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        ___ i __ r..(l..(points)):
            dist_cnt = Counter()
            ___ j __ r..(l..(points)):
                __ i != j:
                    d = distance(points[i], points[j])
                    dist_cnt[d] += 1

            ___ v __ dist_cnt.v..
                # Permutation: P v 2
                ret += v * (v - 1)

        r.. ret

    ___ numberOfBoomerangs_TLE(self, points):
        """
        Reverse look up
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        ___ i __ r..(l..(points)):
            dist_cnt = Counter()
            dist_lst    # list
            ___ j __ r..(l..(points)):
                __ i != j:
                    d = distance(points[i], points[j])
                    dist_lst.a..(d)
                    dist_cnt[d] += 1

            ___ d __ dist_lst:
                ret += (dist_cnt[d] - 1)

        r.. ret


__ __name__ __ "__main__":
    ... Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]) __ 2
