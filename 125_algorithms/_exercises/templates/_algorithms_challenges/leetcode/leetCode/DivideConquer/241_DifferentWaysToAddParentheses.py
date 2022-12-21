#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    """
    Recursive way: easy to understand.  The key idea for this solution is:
    each operator in this string could be the last operator to be operated.
    We just iterator over all these cases.
    """

    ___ diffWaysToCompute  input
        __ input.isdigit(
            r_ [int(input)]

        res   # list
        ___ i __ xrange(l..(input)):
            __ input[i] __ "+-*":
                res_left = self.diffWaysToCompute(input[:i])
                res_right = self.diffWaysToCompute(input[i + 1:])
                ___ left __ res_left:
                    ___ right __ res_right:
                        res.append(self.computer(left, right, input[i]))
        r_ res

    ___ computer  m, n, op
        __ op __ "+":
            r_ m + n
        ____ op __ "-":
            r_ m - n
        ____
            r_ m * n


c.. Solution_2 o..
    # Use cache to avoid repeating subquestions in recursive way.
    ___ diffWaysToCompute  input
        self.cache _ # dict
        r_ self.computerWithCache(input)

    ___ computerWithCache  input
        __ input.isdigit(
            self.cache[input] = [int(input)]
            r_ [int(input)]

        res   # list
        ___ i __ xrange(l..(input)):
            __ input[i] __ "+-*":
                left_str = input[:i]
                res_left = (self.cache[left_str] __ left_str __ self.cache
                            else self.computerWithCache(input[:i]))
                right_str = input[i + 1:]
                res_right = (self.cache[right_str] __ right_str __ self.cache
                             else self.computerWithCache(input[i + 1:]))

                ___ left __ res_left:
                    ___ right __ res_right:
                        res.append(self.computer(left, right, input[i]))
        self.cache[input] = res
        r_ res

    ___ computer  m, n, op
        __ op __ "+":
            r_ m + n
        ____ op __ "-":
            r_ m - n
        ____
            r_ m * n

"""
"0"
"2-1-1"
"2*3-4*5"
"3-6*7+8-12*1"
"""
