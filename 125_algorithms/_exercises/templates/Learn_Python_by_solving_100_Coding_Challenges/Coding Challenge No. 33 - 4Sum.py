# 4 Sum
# Question: Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
# A solution set is: (-1, 0, 0, 1); (-2, -1, 1, 2); (-2, 0, 0, 2)
# Solutions:


c_ Solution:
    ___ fourSum(self, nums, target):
        answer _   # list
        nums.sort()
        length _ le.(nums)
        ___ k __ ra..(length-3):
            __ nums[k]+nums[k+1]+nums[k+2]+nums[k+3] > target:
                break
            ___ i __ ra..(k+1,length-2):
                low _ i+1
                high _ length - 1
                while(low < high):
                    temp _ nums[i]+nums[low]+nums[high]+nums[k]
                    __ temp __ target:
                        ans _ [nums[i],nums[low],nums[high],nums[k]]
                        ans.sort()
                        low _ low + 1
                        high _ high - 1
                        __ ans not __ answer:
                            answer.ap..(ans)
                        while low < high an. nums[high+1] __ nums[high]: ##speed up, jump the same value
                            high -_ 1
                        while low < high an. nums[low] __ nums[low-1]:
                            low +_ 1
                    elif temp > target:
                        high _ high -1
                    ____
                        low _ low + 1
        r_ answer


Solution().fourSum([1, 0, -1, 0, -2, 2], 0)