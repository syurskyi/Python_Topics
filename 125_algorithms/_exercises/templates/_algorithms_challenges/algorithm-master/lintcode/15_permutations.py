c_ Solution:
    ___ permute  nums
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        __ n.. nums:
            r.. [[]]

        ans    # list

        nums.s..()
        dfs(nums, ans, [])

        r.. ans

    ___ dfs  nums, ans, p..
        __ n.. nums:
            ans.a..(p.. | )
            r..

        ___ i __ r..(l..(nums:
            p...a..(nums[i])
            dfs(nums[:i] + nums[i + 1:], ans, p..)
            p...p.. )
