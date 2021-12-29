"""
REF: https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
REF: http://www.cnblogs.com/grandyang/p/4985506.html

Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
obj.update(i,val)
param_2 = obj.sumRange(i,j)
"""


class NumArray:
    ___ __init__(self, nums):
        """
        :type nums: List[int]
        """
        __ n.. nums:
            r..

        n = l..(nums)
        self.bits = [0] * (n + 1)  # bits
        self.incr = [0] * (n + 1)  # increments

        ___ i __ r..(n):
            self.update(i, nums[i])

    ___ update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void

        It must increase `i` here, since this api is public,
        so look from outside, the `i` is just the index of `nums`
        """
        j = i + 1
        delta = val - self.incr[j]
        self.incr[j] = val

        w.... j < l..(self.incr):
            self.bits[j] += delta
            j += (j & -j)

    ___ sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        r.. self.s..(j + 1) - self.s..(i)

    ___ s..(self, i):
        res = 0
        j = i

        w.... j > 0:
            res += self.bits[j]
            j -= (j & -j)

        r.. res
