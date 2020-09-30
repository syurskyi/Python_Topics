# 3 Sum Closest
# Question: Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution
# For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2.
# (-1 + 2 + 1 = 2).
# Solutions:


class Solution:
    ___ threeSumClosest(self, numbers, target):
        numbers.sort()
        ans _ None
        ___ i __ ra..(le.(numbers)):
            l, r _ i + 1, le.(numbers) - 1
            while (l < r):
                su. _ numbers[l] + numbers[r] + numbers[i]
                __ ans is None or abs(su.- target) < abs(ans - target):
                    ans _ su.
                __ su. <_ target:
                    l _ l + 1
                ____
                    r _ r - 1
        r_ ans


Solution().threeSumClosest([-1, 2, 1, -4], 1)