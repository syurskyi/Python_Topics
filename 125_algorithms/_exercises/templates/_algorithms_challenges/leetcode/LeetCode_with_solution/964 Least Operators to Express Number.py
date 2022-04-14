#!/usr/bin/python3
"""
Given a single positive integer x, we will write an expression of the form
x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either
addition, subtraction, multiplication, or division (+, -, *, or /).  For
example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happens before
addition and subtraction.
It's not allowed to use the unary negation operator (-).  For example, "x - x"
is a valid expression as it only uses subtraction, but "-x + x" is not because
it uses negation.
We would like to write an expression with the least number of operators such
that the expression equals the given target.  Return the least number of
operators used.


Example 1:
Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.

Example 2:
Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8
operations.

Example 3:
Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.


Note:
2 <= x <= 100
1 <= target <= 2 * 10^8
"""
____ f.. _______ lru_cache


c_ Solution:
    ___ leastOpsExpressTarget  x: i.., target: i..) __ i..
        """
        x/x is 1
        x * x is power 2

        target = a_n * x^n + a_{n-1} * x^{n-1} + ... + a_1 * x^1 + a_0 * x/x

        To make target divisible, it can be target - a0 or target + (x^1 - a0)
        """
        r.. dfs(target, x, 0) - 1

    @lru_cache(maxsize=N..)
    ___ dfs  target, x, power
        """
        power: power, pow(x, power)
        """
        __ target __ 0:
            r.. 0

        __ target __ 1:
            r.. ops(power)

        d, r target // x, target % x
        ret r * ops(power) + dfs(d, x, power + 1)
        # either -r or +(x-r)
        __ r !_ 0:
            ret2 (x - r) * ops(power) + dfs(d + 1, x, power + 1)
            ret m..(ret, ret2)

        r.. ret

    ___ ops  power
        """
        number of ops required

        + x/x
        + x
        + x * x
        + x * x * x
        """
        __ power __ 0:
            r.. 2
        ____
            r.. power


__ _______ __ _______
    ... Solution().leastOpsExpressTarget(3, 19) __ 5
    ... Solution().leastOpsExpressTarget(5, 501) __ 8
    ... Solution().leastOpsExpressTarget(2, 125046) __ 50
