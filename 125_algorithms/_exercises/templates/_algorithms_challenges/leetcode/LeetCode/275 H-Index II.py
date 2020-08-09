"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""
__author__ = 'Daniel'


class Solution(object
    ___ hIndex(self, A
        """
        Given sorted -> binary search
        From linear search into bin search
        :type A: List[int]
        :rtype: int
        """
        n = le.(A)
        s = 0
        e = n
        w___ s < e:
            m = (s+e)/2
            __ A[m] >= n-m:
                e = m
            ____
                s = m+1

        r_ n-s


__ __name__ __ "__main__":
    assert Solution().hIndex([0, 1, 3, 5, 6]) __ 3