class Solution:
    ___ permute(self, nums):
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        __ not nums:
            return [[]]

        ans = []

        nums.sort()
        self.dfs(nums, ans, [])

        return ans

    ___ dfs(self, nums, ans, path):
        __ not nums:
            ans.append(path[:])
            return

        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()
