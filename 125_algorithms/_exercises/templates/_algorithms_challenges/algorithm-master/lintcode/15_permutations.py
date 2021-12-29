class Solution:
    ___ permute(self, nums):
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        __ n.. nums:
            r.. [[]]

        ans    # list

        nums.sort()
        self.dfs(nums, ans, [])

        r.. ans

    ___ dfs(self, nums, ans, path):
        __ n.. nums:
            ans.a..(path[:])
            r..

        ___ i __ r..(l..(nums)):
            path.a..(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()
