class Solution:
    ___ permute(self, nums
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        __ not nums:
            r_ [[]]

        ans = []

        nums.sort()
        self.dfs(nums, ans, [])

        r_ ans

    ___ dfs(self, nums, ans, path
        __ not nums:
            ans.append(path[:])
            r_

        for i in range(le.(nums)):
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()
