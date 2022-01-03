"""
- item can only pick once (even diff item with same val): num loop -> amount loop, amount from end to start, + break
- item can pick multiple but diff order is same path: num loop -> amount loop, amount from start to end
- item can pick multiple but diff order is diff path: amount loop -> num loop, amount from start to end
"""


c_ Solution:
    """
    Dynamic Programming
    """
    ___ combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        dp = [0] * (target + 1)
        dp[0] = 1

        # if iterate num first, then the answer will become the number of unique set
        # see the last Solution in this file
        ___ amount __ r..(1, target + 1):
            ___ num __ nums:
                __ amount >= num:
                    dp[amount] += dp[amount - num]

        r.. dp[target]


c_ Solution:
    """
    Memory Search /
    Dynamic Programming /
    DFS
    """
    ___ combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        dp = [-1] * (target + 1)
        dp[0] = 1
        memo_search(nums, target, dp)
        r.. dp[target]

    ___ memo_search(self, nums, remain, dp):
        __ dp[remain] > -1:
            r.. dp[remain]

        res = 0

        ___ a __ nums:
            __ remain < a:
                continue

            res += memo_search(nums, remain - a, dp)

        dp[remain] = res
        r.. res


c_ Solution:
    """
    DFS: TLE
    """
    ___ combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        ans    # list
        nums.s..(r.._T..
        dfs(nums, target, ans, [])

        r.. l..(ans)

    ___ dfs(self, nums, remain, ans, path):
        __ remain __ 0:
            ans.a..(path[::-1])
            r..

        ___ a __ nums:
            __ remain < a:
                continue

            path.a..(a)
            dfs(nums, remain - a, ans, path)
            path.pop()


# ======


c_ Solution:
    """
    Dynamic Programming: wrong answer for this question

    This approach is to find the unique combination
    """
    ___ combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        dp = [0] * (target + 1)
        dp[0] = 1

        ___ num __ nums:
            ___ amount __ r..(num, target + 1):
                dp[amount] += dp[amount - num]

        r.. dp[target]
