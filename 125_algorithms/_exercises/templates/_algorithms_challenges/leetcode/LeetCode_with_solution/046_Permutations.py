c_ Solution:
    # import itertools
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     result = itertools.permutations(nums)
    #     result = [list(t) for t in result]
    #     return result

    ___ permute  nums
        # DPS with swapping
        res =    # list
        __ l.. nums) __ 0:
            r_ res
        get_permute(res, nums, 0)
        r_ res

    ___ get_permute  res, nums, index
        __ index __ l.. nums
            res.a.. list(nums))
            r_
        ___ i __ r.. index, l.. nums)):
            nums[i], nums[index] = nums[index], nums[i]
            # s(n) = 1 + s(n-1)
            get_permute(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]

    # def permute(self, nums):
    #     # iterative solution
    #     res = [[]]
    #     for i in range(len(nums)):
    #         cache = set()
    #         while len(res[0]) == i:
    #             curr = res.pop(0)
    #             for j in range(len(curr) + 1):
    #                 # generate new n permutations from n -1 permutations
    #                 new_perm = curr[:j] + [nums[i]] + curr[j:]
    #                 stemp = ''.join(map(str, new_perm))
    #                 if stemp not in cache:
    #                     cache.add(stemp)
    #                     res.append(new_perm)
    #     return res
