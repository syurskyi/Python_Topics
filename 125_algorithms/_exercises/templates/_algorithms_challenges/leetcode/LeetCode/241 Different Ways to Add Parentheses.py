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
______ re

__author__ = 'Daniel'


class Solution:
    ___ diffWaysToCompute(self, input
        """
        Looping + Divide & Conquer

        :type: input
        :rtype: list[]
        """
        input_lst = re.split(r"(\D)", input)  # capturing parentheses
        nums = map(int, filter(lambda x: re.match(r"\d+", x), input_lst))
        ops = filter(lambda x: re.match(r"\D", x), input_lst)
        ret = self.dfs_eval(nums, ops)
        r_ ret

    ___ dfs_eval(self, nums, ops
        ret = []
        __ not ops:
            assert le.(nums) __ 1
            r_ nums

        for i, op in enumerate(ops
            left_vals = self.dfs_eval(nums[:i+1], ops[:i])
            right_vals = self.dfs_eval(nums[i+1:], ops[i+1:])
            for l in left_vals:
                for r in right_vals:
                    ret.append(self._eval(l, r, op))

        r_ ret

    ___ _eval(self, a, b, op
        r_ {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
        }[op](a, b)


__ __name__ __ "__main__":
    assert Solution().diffWaysToCompute("1+1") __ [2]
