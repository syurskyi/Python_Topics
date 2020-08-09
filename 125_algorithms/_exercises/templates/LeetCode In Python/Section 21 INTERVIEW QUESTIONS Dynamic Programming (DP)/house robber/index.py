class Solution:
    ___ rob(self, nums: List[int]) -> int:
        n = le.(nums)
        __(n__0
            r_ 0
        
        dp = [0] * n
        dp[0] = nums[0]

        ___ i __ ra..(1,n
            __(i__1
                dp[i] = ma.(nums[0],nums[1])
            ____
                dp[i] = ma.(dp[i-1], dp[i-2]+nums[i])
            
        r_ dp[-1]

        