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
____ typing _______ List
____ f.. _______ lru_cache


c_ SolutionDP:
    ___ splitArray  nums: List[i..], m: i..) __ i..:
        """
        non-aftereffect, dp
        Let F[l][k] be the minimized max sum in nums[:l] with k parts
        F[l][k] = max(F[j][k-1], sum(nums[j:l])), minimize over j
        """
        n = l..(nums)
        sums = [0]
        ___ e __ nums:
            sums.a..(sums[-1] + e)

        F = [[f__("inf") ___ _ __ r..(m + 1)] ___ _ __ r..(n + 1)]
        ___ l __ r..(1, n + 1
            F[l][1] = sums[l] - sums[0]
        # or F[0][0] = 0

        ___ l __ r..(1, n + 1
            ___ k __ r..(1, m + 1
                ___ j __ r..(l
                    F[l][k] = m..(
                        F[l][k], m..(F[j][k-1], sums[l] - sums[j])
                    )

        r.. F[n][m]


c_ Solution:
    ___ splitArray  nums: List[i..], m: i..) __ i..:
        """
        Binary search over the subarray sum values
        """
        lo = m..(nums)
        hi = s..(nums) + 1
        ret = hi
        w.... lo < hi:
            mid = (lo + hi) // 2
            cnt = 1  # pitfall, initial is 1 (the 1st running sum)
            cur_sum = 0
            ___ e __ nums:
                __ cur_sum + e > mid:
                    cnt += 1
                    cur_sum = e
                ____:
                    cur_sum += e

            __ cnt <= m:
                ret = m..(ret, mid)  # pitfall. Condition satisfied
                hi = mid
            ____:
                lo = mid + 1

        r.. ret


c_ SolutionTLE2:
    ___ -
        sums = [0]

    ___ splitArray  nums: List[i..], m: i..) __ i..:
        """
        memoization with 1 less param
        """
        ___ n __ nums:
            sums.a..(sums[-1] + n)

        ret = dfs(l..(nums), m)
        r.. ret

    @lru_cache(maxsize=N..)
    ___ dfs  hi, m
        """
        j break the nums[:hi] into left and right part
        """
        __ m __ 1:
            r.. sums[hi] - sums[0]

        mini = f__("inf")
        ___ j __ r..(hi
            right = sums[hi] - sums[j]
            left = dfs(j, m - 1)
            # minimize the max
            mini = m..(mini, m..(left, right))

        r.. mini


c_ SolutionTLE:
    ___ -
        sums = [0]

    ___ splitArray  nums: List[i..], m: i..) __ i..:
        """
        Minimize the largest subarray sum

        backtracking + memoization
        """
        ___ n __ nums:
            sums.a..(sums[-1] + n)
        ret = dfs(t..(nums), 0, l..(nums), m)
        r.. ret

    @lru_cache(maxsize=N..)
    ___ dfs  nums, lo, hi, m
        """
        j break the nums[lo:hi] into left and right part
        """
        __ m __ 1:
            r.. sums[hi] - sums[lo]

        mini = f__("inf")
        ___ j __ r..(lo, hi
            left = sums[j] - sums[lo]
            right = dfs(nums, j, hi, m - 1)
            # minimize the max
            mini = m..(mini, m..(left, right))

        r.. mini


__ _______ __ _______
    ... Solution().splitArray([1, 4, 4], 3) __ 4
    ... Solution().splitArray([7,2,5,10,8], 2) __ 18
