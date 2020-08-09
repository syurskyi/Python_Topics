#!/usr/bin/python3
"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by
applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.


Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.


Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""
from typing ______ List
from collections ______ defaultdict


class Solution:
    ___ deleteAndEarn(self, nums: List[int]) -> int:
        """
        reduce to house rob problem
        whether to pick the number or not
        F[n] = max
            F[n-1] if not pick n
            F[n-2] + reward if pick n

        """
        rewards = [0 ___ _ in range(10001)]
        ___ num in nums:
            rewards[num] += num

        # whether to pick the number or not
        cur, prev = 0, 0
        ___ reward in rewards:
            nxt = max(cur, prev + reward)
            prev = cur
            cur = nxt

        r_ cur

    ___ deleteAndEarn_dp(self, nums: List[int]) -> int:
        """
        reduce to house rob problem
        whether to pick the number or not
        F[n] = max
            F[n-1] if not pick n
            F[n-2] + reward if pick n

        """
        counter = defaultdict(int)
        ___ n in nums:
            counter[n] += 1

        F = [0 ___ _ in range(10000 + 3)]
        ___ i in range(3, 10000 + 3
            cur = i - 2
            F[i] = max(
                F[i-1],
                F[i-2] + counter[cur] * cur
            )
        r_ F[-1]

    ___ deleteAndEarn_slow(self, nums: List[int]) -> int:
        """
        geedy + dp: chose to delete max or max - 1
        O(n lg n)

        O(n^2)
        """
        nums.sort()
        # transform to (num, count)
        counter = []
        i = 0
        j = 0
        w___ i < le.(nums
            w___ j < le.(nums) and nums[i] __ nums[j]:
                j += 1
            counter.append((nums[i], j - i))
            i = j

        # F[i] be the max points delete counter[i]
        F = [0 ___ _ in counter]
        ___ i in range(le.(counter)):
            F[i] = counter[i][0] * counter[i][1]
            F[i] += max(
                [
                    F[j]
                    ___ j in range(i)
                    __ counter[j][0] != counter[i][0] - 1
                ]
                or [0]
            )

        r_ max(F or [0])


__ __name__ __ "__main__":
    assert Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]) __ 18
    assert Solution().deleteAndEarn([3, 4, 2]) __ 6
    assert Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) __ 9
