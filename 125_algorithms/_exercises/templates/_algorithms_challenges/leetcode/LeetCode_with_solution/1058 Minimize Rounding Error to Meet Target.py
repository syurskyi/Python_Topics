#!/usr/bin/python3
"""
Given an array of prices [p1,p2...,pn] and a target, round each price pi to
Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums
to the given target. Each operation Roundi(pi) could be either Floor(pi) or
Ceil(pi).

Return the string "-1" if the rounded array is impossible to sum to target.
Otherwise, return the smallest rounding error, which is defined as
Σ |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after the
decimal.



Example 1:

Input: prices = ["0.700","2.800","4.900"], target = 8
Output: "1.000"
Explanation:
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) =
0.7 + 0.2 + 0.1 = 1.0 .
Example 2:

Input: prices = ["1.500","2.500","3.500"], target = 10
Output: "-1"
Explanation:
It is impossible to meet the target.


Note:

1 <= prices.length <= 500.
Each string of prices prices[i] represents a real number which is between 0 and
1000 and has exactly 3 decimal places.
target is between 0 and 1000000.
"""
____ typing _______ List
_______ math


c_ Solution:
    ___ minimizeError(self, prices: List[s..], target: i..) __ s..:
        """
        to determine possible, floor all or ceil all

        floor all, sort by floor error inverse, make the adjustment
        """
        A = l..(map(float, prices))
        f_sum = s..(map(math.floor, A))
        c_sum = s..(map(math.ceil, A))
        __ n.. f_sum <= target <= c_sum:
            r.. "-1"

        errors = [
            e - math.floor(e)
            ___ e __ A
        ]
        errors.s..(r.._T..
        ret = 0
        remain = target - f_sum
        ___ err __ errors:
            __ remain > 0:
                ret += 1 - err
                remain -= 1
            ____:
                ret += err

        r.. f'{ret:.{3}f}'
