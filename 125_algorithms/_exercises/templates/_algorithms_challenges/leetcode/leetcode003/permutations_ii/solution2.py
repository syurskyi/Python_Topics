"""
Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

c_ Solution(o..
    ___ permuteUnique  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r.. permute(s..(nums))

    ___ permute  nums
        __ n.. nums:
            r.. [[]]
        ____:
            res    # list
            prev = N..
            ___ i, e __ e..(nums
                __ prev __ N.. o. prev != e:
                    rest = nums[:i] + nums[i + 1:]
                    rest_perms = permute(rest)
                    ___ perm __ rest_perms:
                        perm.a..(e)
                    res += rest_perms
                    prev = e
            r.. res
