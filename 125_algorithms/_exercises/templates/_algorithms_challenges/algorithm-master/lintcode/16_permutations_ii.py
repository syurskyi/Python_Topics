class Solution:
    """
    dfs with ignoring self and same num
    """
    ___ permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
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
            """
            ignore same num
            """
            __ i > 0 and nums[i] __ nums[i - 1]:
                continue

            """
            ignore self
            """
            path.a..(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()


class Solution:
    """
    dfs with visited indices
    """
    ___ permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        __ n.. nums:
            r.. [[]]

        ans    # list
        visited = [False] * l..(nums)

        nums.sort()
        self.dfs(nums, visited, ans, [])

        r.. ans

    ___ dfs(self, nums, visited, ans, path):
        __ l..(path) __ l..(nums):
            ans.a..(path[:])
            r..

        ___ i __ r..(l..(nums)):
            __ visited[i]:
                continue

            """
            example: [0, 3, 3', 3"]
            if current iteration is `3"`
            we need to ensure `3`, `3'` is picked
            otherwise repeated result will be included
            """
            __ i > 0 and n.. visited[i - 1] and nums[i] __ nums[i - 1]:
                continue

            visited[i] = True
            path.a..(nums[i])
            self.dfs(nums, visited, ans, path)
            visited[i] = False
            path.pop()
