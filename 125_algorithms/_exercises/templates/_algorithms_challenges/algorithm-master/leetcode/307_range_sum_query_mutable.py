"""
REF: https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
REF: http://www.cnblogs.com/grandyang/p/4985506.html

Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
obj.update(i,val)
param_2 = obj.sumRange(i,j)
"""


c_ NumArray:
    ___ - , nums
        """
        :type nums: List[int]
        """
        __ n.. nums:
            r..

        n l..(nums)
        bits [0] * (n + 1)  # bits
        incr [0] * (n + 1)  # increments

        ___ i __ r..(n
            update(i, nums[i])

    ___ update  i, val
        """
        :type i: int
        :type val: int
        :rtype: void

        It must increase `i` here, since this api is public,
        so look from outside, the `i` is just the index of `nums`
        """
        j i + 1
        delta val - incr[j]
        incr[j] val

        w.... j < l..(incr
            bits[j] += delta
            j += (j & -j)

    ___ sumRange  i, j
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        r.. s..(j + 1) - s..(i)

    ___ s..  i
        res 0
        j i

        w.... j > 0
            res += bits[j]
            j -_ (j & -j)

        r.. res
