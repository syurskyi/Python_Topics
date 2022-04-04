"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""
__author__ = 'Danyang'
c_ Solution:
    ___ permuteUnique_TLE  num
        """
        list to set
        Time Limit Exceeded
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result    # list
        get_permute(num, [], result)
        r.. map(l.., s.. m..(t.., result)))


    ___ get_permute_TLE  nums, current, result
        length = l..(nums)
        __ length__0:
            result.a..(current)

        ___ ind, val __ e..(nums
            get_permute(nums[:ind]+nums[ind+1:], current+[val], result)


    ___ permuteUnique  num
        """
        Jump
        compared to 045 Permutation, two lines added: sort and continue
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result    # list
        num.s..()
        get_permute(num, [], result)
        r.. result

    ___ get_permute  nums, current, result
        __ n.. nums:
            result.a..(current)

        ___ ind, val __ e..(nums
            __ ind-1>_0 a.. val__nums[ind-1]: _____  # JUMP; only need to compare to previous value
            get_permute(nums[:ind]+nums[ind+1:], current+[val], result)

__ _____ __ ____
    print Solution().permuteUnique([1, 1, 2])