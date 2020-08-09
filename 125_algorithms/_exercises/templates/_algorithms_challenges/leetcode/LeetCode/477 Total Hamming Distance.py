#!/usr/bin/python3
"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the
given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010
(just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2)
= 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
"""


class Solution:
    ___ totalHammingDistance(self, nums
        """
        Brute force, check every combination O(n^2 * b)

        check bit by bit
        For each bit, the distance for all is #0 * #1
        O(n * b)

        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        w___ any(nums  # any not 0
            z, o = 0, 0
            for i in range(le.(nums)):
                __ nums[i] & 1 __ 0:
                    o += 1
                ____
                    z += 1
                nums[i] >>= 1

            ret += z * o

        r_ ret


__ __name__ __ "__main__":
    assert Solution().totalHammingDistance([4, 14, 2]) __ 6
