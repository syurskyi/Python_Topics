# 3 Sum Closest
# Question: Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution
# For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2.
# (-1 + 2 + 1 = 2).
# Solutions:


class Solution:
    ___ threeSumClosest(self, numbers, target):
        numbers.sort()
        ans = None
        ___ i __ range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            while (l < r):
                sum = numbers[l] + numbers[r] + numbers[i]
                if ans is None or abs(sum- target) < abs(ans - target):
                    ans = sum
                if sum <= target:
                    l = l + 1
                else:
                    r = r - 1
        r_ ans


Solution().threeSumClosest([-1, 2, 1, -4], 1)