"""
- item can only pick once (even diff item with same val num loop -> amount loop, amount from end to start, + break
- item can pick multiple but diff order is same path: num loop -> amount loop, amount from start to end
- item can pick multiple but diff order is diff path: amount loop -> num loop, amount from start to end
"""


class Solution:
    """
    Dynamic Programming
    """
    ___ combinationSum4(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ not nums:
            r_ 0

        dp = [0] * (target + 1)
        dp[0] = 1

        # if iterate num first, then the answer will become the number of unique set
        # see the last Solution in this file
        ___ amount in range(1, target + 1
            ___ num in nums:
                __ amount >= num:
                    dp[amount] += dp[amount - num]

        r_ dp[target]


class Solution:
    """
    Memory Search /
    Dynamic Programming /
    DFS
    """
    ___ combinationSum4(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ not nums:
            r_ 0

        dp = [-1] * (target + 1)
        dp[0] = 1
        self.memo_search(nums, target, dp)
        r_ dp[target]

    ___ memo_search(self, nums, remain, dp
        __ dp[remain] > -1:
            r_ dp[remain]

        res = 0

        ___ a in nums:
            __ remain < a:
                continue

            res += self.memo_search(nums, remain - a, dp)

        dp[remain] = res
        r_ res


class Solution:
    """
    DFS: TLE
    """
    ___ combinationSum4(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ not nums:
            r_ 0

        ans = []
        nums.sort(reverse=True)
        self.dfs(nums, target, ans, [])

        r_ le.(ans)

    ___ dfs(self, nums, remain, ans, path
        __ remain __ 0:
            ans.append(path[::-1])
            r_

        ___ a in nums:
            __ remain < a:
                continue

            path.append(a)
            self.dfs(nums, remain - a, ans, path)
            path.pop()


# ======


class Solution:
    """
    Dynamic Programming: wrong answer for this question

    This approach is to find the unique combination
    """
    ___ combinationSum4(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ not nums:
            r_ 0

        dp = [0] * (target + 1)
        dp[0] = 1

        ___ num in nums:
            ___ amount in range(num, target + 1
                dp[amount] += dp[amount - num]

        r_ dp[target]
