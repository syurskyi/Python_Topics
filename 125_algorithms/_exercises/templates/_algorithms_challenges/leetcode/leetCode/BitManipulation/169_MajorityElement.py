#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ majorityElement  nums
        nums.sort()
        r_ nums[l..(nums) / 2]

    # Boyer–Moore majority vote algorithm. Refer to:
    # https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
    ___ majorityElement_moore  nums
        majority_num = 0
        count = 0
        ___ num __ nums:
            __ count __ 0:
                majority_num = num
            __ majority_num != num:
                count -= 1
            ____
                count += 1
        r_ majority_num

    # Hash table
    ___ majorityElement_hash  nums
        num_len = l..(nums)
        num_hash _ # dict
        ___ num __ nums:
            num_hash[num] = num_hash.get(num, 0) + 1
            __ num_hash[num] > num_len / 2:
                r_ num

    # Bit manipulation
    # Pay attention: in python -2147483648 >> 31 = -1
    ___ majorityElement_bit  nums
        bit_bucket = [0 ___ i __ r..(33)]
        ___ num __ nums:
            bit_bucket[32] += (num >> 32) & 1
            ___ i __ r..(32
                bit_bucket[i] += (abs(num) >> i) & 1

        majority_num = 0
        nums_len = l..(nums)
        ___ i __ r..(32
            __ bit_bucket[i] > nums_len / 2:
                majority_num += 1 << i
        __ bit_bucket[32] > nums_len / 2:
            majority_num *= -1
        r_ majority_num

"""
[1]
[1]
[1,2,2,2]
[7,6,5,7,7]
[-2147483648]
[-2147483648, 2147483648, -2147483648]
[-1,-1,2147483647]
"""
