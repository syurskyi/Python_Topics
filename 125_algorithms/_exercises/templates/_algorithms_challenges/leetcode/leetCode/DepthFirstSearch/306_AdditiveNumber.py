#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # According to:
    # https://leetcode.com/discuss/70089/python-solution
    # The key point is choose first two number then recursively check.
    # DFS: recursice implement.
    ___ isAdditiveNumber  num
        length = l..(num)
        ___ i __ r..(1, length/2+1
            ___ j __ r..(1, (length-i)/2 + 1
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                __ self.isValid(first, second, others
                    r_ True
        r_ False

    ___ isValid  first, second, others
        # Numbers in the additive sequence cannot have leading zeros,
        __ ((l..(first) > 1 a.. first[0] __ "0") or
                (l..(second) > 1 a.. second[0] __ "0")):
            r_ False
        sum_str = str(int(first) + int(second))
        __ sum_str __ others:
            r_ True
        ____ others.startswith(sum_str
            r_ self.isValid(second, sum_str, others[l..(sum_str])
        ____
            r_ False


c.. Solution_2 o..
    # DFS: iterative implement.
    ___ isAdditiveNumber  num
        length = l..(num)
        ___ i __ r..(1, length/2+1
            ___ j __ r..(1, (length-i)/2 + 1
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                __ ((l..(first) > 1 a.. first[0] __ "0") or
                        (l..(second) > 1 a.. second[0] __ "0")):
                    c_

                _____ others:
                    sum_str = str(int(first) + int(second))
                    __ sum_str __ others:
                        r_ True
                    ____ others.startswith(sum_str
                        first, second, others = (
                            second, sum_str, others[l..(sum_str])
                    ____
                        ______

        r_ False

"""
"1123"
"1203"
"112324"
"112334"
"112358"
"""
