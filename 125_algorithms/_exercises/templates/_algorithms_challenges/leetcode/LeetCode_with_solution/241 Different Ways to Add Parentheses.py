"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to
group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""
_______ __

__author__ = 'Daniel'


c_ Solution:
    ___ diffWaysToCompute  input
        """
        Looping + Divide & Conquer

        :type: input
        :rtype: list[]
        """
        input_lst = __.s..(r"(\D)", input)  # capturing parentheses
        nums = map(i.., f.. l.... x: __.m..(r"\d+", x), input_lst
        ops = f.. l.... x: __.m..(r"\D", x), input_lst)
        ret = dfs_eval(nums, ops)
        r.. ret

    ___ dfs_eval  nums, ops
        ret    # list
        __ n.. ops:
            ... l..(nums) __ 1
            r.. nums

        ___ i, op __ e..(ops
            left_vals = dfs_eval(nums[:i+1], ops[:i])
            right_vals = dfs_eval(nums[i+1:], ops[i+1:])
            ___ l __ left_vals:
                ___ r __ right_vals:
                    ret.a..(_eval(l, r, op

        r.. ret

    ___ _eval  a, b, op
        r.. {
            "+": l.... a, b: a+b,
            "-": l.... a, b: a-b,
            "*": l.... a, b: a*b,
        }[op](a, b)


__ _______ __ _______
    ... Solution().diffWaysToCompute("1+1") __ [2]
