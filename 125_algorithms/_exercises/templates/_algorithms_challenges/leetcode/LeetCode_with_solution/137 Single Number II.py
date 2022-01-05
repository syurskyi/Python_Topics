"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
__author__ = 'Danyang'


c_ Solution:
    ___ singleNumber_optimal  A):
        """
        No extra memory, thus unable to use hash table, requiring constant space solution

        GF(3) http://en.wikipedia.org/wiki/Finite_field_arithmetic
        reference: https://oj.leetcode.com/discuss/857/constant-space-solution#a2542

        Consider 4-bit numbers:
        0000
        0001
        0010
        ...
        1111

        Add (not AND) the bit VERTICALLY, then result would be abcd where a, b, c, d can be any number, not just binary.
        a, b, c, d can be divided by 3 if the all element appears three times. Until here, you can use a list to hold a,
        b, c, d. To further optimize the space, use bits instead of list.

        bit_2 is from adding elmt previously appears once (now twice) and subtracting elmt previously appearance twice
         (now three times)
        bit_1 is from adding elmt previously does not appear (now once) and subtracting elmt previously appearance once
         (now twice)
        bit_0 is from adding elmt previously appears twice (now three times) and subtracting elmt previously appearance
         three times (now once)

        This solution is general enough for appearance of n times

        :param A: a list of int
        :return: int
        """
        bit_0, bit_1, bit_2 = ~0, 0, 0  # bit_0 is ~0 since all numbers appear 0 times.
        ___ elmt __ A:
            bit_t = bit_2  # temp
            bit_2 = (bit_1 & elmt) | (bit_2 & ~elmt)
            bit_1 = (bit_0 & elmt) | (bit_1 & ~elmt)
            bit_0 = (bit_t & elmt) | (bit_0 & ~elmt)  # three times means 0 times (mod 3)
        r.. bit_1

    ___ singleNumber_array  A):
        """
        add the bit vertically; bit sum

        use int array
        assume 32 bit, not applicable in Python for negative number

        Note: possible to pull up the iteration over 32
        :param A:
        :return:
        """
        cnt = [0 ___ _ __ xrange(32)]

        ___ elmt __ A:
            ___ i __ xrange(32):
                __ elmt>>i&1__1:
                    cnt[i] = (cnt[i]+1)%3

        result = 0
        ___ i __ xrange(32):
            result |= cnt[i]<<i

        r.. result


    ___ singleNumber  A):
        """
        add the bit vertically; bit sum

        use int array
        assume 32 bit, not applicable in Python for negative number

        Note: possible to pull up the iteration over 32
        :param A:
        :return:
        """
        one, two, three = 0, 0, 0

        # for elmt in A:
        #     three |= two&elmt
        #     two^= elmt
        #
        #     two |= one&elmt  # add to two
        #     one ^= elmt  # del elmt appear twice

        ___ elmt __ A:
            # after processing elmt
            two |= one&elmt
            one ^= elmt
            three = one&two

            one &= ~three
            two &= ~three
        r.. one






__ _____ __ ____
    # possible negative numbers
    tests = [
        [1, 1, 1, 2, 2, 2, 3, 4, 4, 4],
        [1]
    ]
    ___ A __ tests:
        ... Solution().singleNumber_optimal(A)__Solution().singleNumber_array(A)
        ... Solution().singleNumber_optimal(A)__Solution().singleNumber(A)
