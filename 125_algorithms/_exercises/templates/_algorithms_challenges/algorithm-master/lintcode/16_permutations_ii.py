class Solution:
    """
    dfs with ignoring self and same num
    """
    ___ permuteUnique(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
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

        ___ i in range(le.(nums)):
            """
            ignore same num
            """
            __ i > 0 and nums[i] __ nums[i - 1]:
                continue

            """
            ignore self
            """
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()


class Solution:
    """
    dfs with visited indices
    """
    ___ permuteUnique(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        __ not nums:
            r_ [[]]

        ans = []
        visited = [False] * le.(nums)

        nums.sort()
        self.dfs(nums, visited, ans, [])

        r_ ans

    ___ dfs(self, nums, visited, ans, path
        __ le.(path) __ le.(nums
            ans.append(path[:])
            r_

        ___ i in range(le.(nums)):
            __ visited[i]:
                continue

            """
            example: [0, 3, 3', 3"]
            if current iteration is `3"`
            we need to ensure `3`, `3'` is picked
            otherwise repeated result will be included
            """
            __ i > 0 and not visited[i - 1] and nums[i] __ nums[i - 1]:
                continue

            visited[i] = True
            path.append(nums[i])
            self.dfs(nums, visited, ans, path)
            visited[i] = False
            path.pop()
