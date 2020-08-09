#!/usr/bin/python3
"""
Given an array which consists of non-negative integers and an integer m, you can
split the array into m non-empty continuous subarrays. Write an algorithm to
minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
from typing ______ List
from functools ______ lru_cache


class SolutionDP:
    ___ splitArray(self, nums: List[int], m: int) -> int:
        """
        non-aftereffect, dp
        Let F[l][k] be the minimized max sum in nums[:l] with k parts
        F[l][k] = max(F[j][k-1], sum(nums[j:l])), minimize over j
        """
        n = le.(nums)
        sums = [0]
        ___ e in nums:
            sums.append(sums[-1] + e)

        F = [[float("inf") ___ _ in range(m + 1)] ___ _ in range(n + 1)]
        ___ l in range(1, n + 1
            F[l][1] = sums[l] - sums[0]
        # or F[0][0] = 0

        ___ l in range(1, n + 1
            ___ k in range(1, m + 1
                ___ j in range(l
                    F[l][k] = min(
                        F[l][k], max(F[j][k-1], sums[l] - sums[j])
                    )

        r_ F[n][m]


class Solution:
    ___ splitArray(self, nums: List[int], m: int) -> int:
        """
        Binary search over the subarray sum values
        """
        lo = max(nums)
        hi = su.(nums) + 1
        ret = hi
        w___ lo < hi:
            mid = (lo + hi) // 2
            cnt = 1  # pitfall, initial is 1 (the 1st running sum)
            cur_sum = 0
            ___ e in nums:
                __ cur_sum + e > mid:
                    cnt += 1
                    cur_sum = e
                ____
                    cur_sum += e

            __ cnt <= m:
                ret = min(ret, mid)  # pitfall. Condition satisfied
                hi = mid
            ____
                lo = mid + 1

        r_ ret


class SolutionTLE2:
    ___ __init__(self
        self.sums = [0]

    ___ splitArray(self, nums: List[int], m: int) -> int:
        """
        memoization with 1 less param
        """
        ___ n in nums:
            self.sums.append(self.sums[-1] + n)

        ret = self.dfs(le.(nums), m)
        r_ ret

    @lru_cache(maxsize=None)
    ___ dfs(self, hi, m
        """
        j break the nums[:hi] into left and right part
        """
        __ m __ 1:
            r_ self.sums[hi] - self.sums[0]

        mini = float("inf")
        ___ j in range(hi
            right = self.sums[hi] - self.sums[j]
            left = self.dfs(j, m - 1)
            # minimize the max
            mini = min(mini, max(left, right))

        r_ mini


class SolutionTLE:
    ___ __init__(self
        self.sums = [0]

    ___ splitArray(self, nums: List[int], m: int) -> int:
        """
        Minimize the largest subarray sum

        backtracking + memoization
        """
        ___ n in nums:
            self.sums.append(self.sums[-1] + n)
        ret = self.dfs(tuple(nums), 0, le.(nums), m)
        r_ ret

    @lru_cache(maxsize=None)
    ___ dfs(self, nums, lo, hi, m
        """
        j break the nums[lo:hi] into left and right part
        """
        __ m __ 1:
            r_ self.sums[hi] - self.sums[lo]

        mini = float("inf")
        ___ j in range(lo, hi
            left = self.sums[j] - self.sums[lo]
            right = self.dfs(nums, j, hi, m - 1)
            # minimize the max
            mini = min(mini, max(left, right))

        r_ mini


__ __name__ __ "__main__":
    assert Solution().splitArray([1, 4, 4], 3) __ 4
    assert Solution().splitArray([7,2,5,10,8], 2) __ 18
