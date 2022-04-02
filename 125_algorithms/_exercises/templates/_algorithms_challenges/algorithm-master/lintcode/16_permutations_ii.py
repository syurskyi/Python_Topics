c_ Solution:
    """
    dfs with ignoring self and same num
    """
    ___ permuteUnique  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        __ n.. nums:
            r.. [[]]

        ans    # list

        nums.s..()
        dfs(nums, ans, [])

        r.. ans

    ___ dfs  nums, ans, path
        __ n.. nums:
            ans.a..(path | )
            r..

        ___ i __ r..(l..(nums)):
            """
            ignore same num
            """
            __ i > 0 a.. nums[i] __ nums[i - 1]:
                _____

            """
            ignore self
            """
            path.a..(nums[i])
            dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()


c_ Solution:
    """
    dfs with visited indices
    """
    ___ permuteUnique  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        __ n.. nums:
            r.. [[]]

        ans    # list
        visited = [F..] * l..(nums)

        nums.s..()
        dfs(nums, visited, ans, [])

        r.. ans

    ___ dfs  nums, visited, ans, path
        __ l..(path) __ l..(nums
            ans.a..(path | )
            r..

        ___ i __ r..(l..(nums)):
            __ visited[i]:
                _____

            """
            example: [0, 3, 3', 3"]
            if current iteration is `3"`
            we need to ensure `3`, `3'` is picked
            otherwise repeated result will be included
            """
            __ i > 0 a.. n.. visited[i - 1] a.. nums[i] __ nums[i - 1]:
                _____

            visited[i] = T..
            path.a..(nums[i])
            dfs(nums, visited, ans, path)
            visited[i] = F..
            path.pop()
