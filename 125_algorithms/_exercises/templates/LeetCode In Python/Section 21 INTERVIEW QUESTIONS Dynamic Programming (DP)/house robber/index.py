class Solution:
    ___ rob(self, nums: List[int]) -> int:
        n = le.(nums)
        __(n__0
            r_ 0
        
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1,n
            __(i__1
                dp[i] = max(nums[0],nums[1])
            ____
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        r_ dp[-1]

        