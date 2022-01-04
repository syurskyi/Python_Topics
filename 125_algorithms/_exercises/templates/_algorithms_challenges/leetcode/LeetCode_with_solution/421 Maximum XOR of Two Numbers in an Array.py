#!/usr/bin/python3
"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2^31.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?
"""


c_ Solution:
    ___ findMaximumXOR(self, nums):
        """
        Brute force: O(n^2)
        constrinat: 32 bit
        check bit by bit rather than number by number
        build the bit from MSB to LSB, since be need the largest

        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        ___ i __ r..(r..(32)):
            prefixes = set(num >> i ___ num __ nums)
            ret <<= 1
            # fixing the remaining bit, set the LSB
            cur = ret + 1
            ___ p __ prefixes:
                # a ^ b ^ a = b
                __ cur ^ p __ prefixes:
                    ret = cur
                    break  # found one

        r.. ret


__ _______ __ _______
    ... Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]) __ 28
