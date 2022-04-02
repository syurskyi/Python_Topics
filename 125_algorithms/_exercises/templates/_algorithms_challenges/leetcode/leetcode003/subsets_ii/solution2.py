c_ Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    ___ subsetsWithDup  nums
        nums.s..()
        r.. subsets_aux(nums)

    ___ subsets_aux  nums
        __ n.. nums:
            r.. [[]]
        ____:
            res = [[]]
            ___ i, e __ e..(nums
                __ i > 0 a.. nums[i] __ nums[i - 1]:
                    _____
                rest_subsets = subsets_aux(nums[i + 1:])
                ___ subset __ rest_subsets:
                    subset.insert(0, e)
                res += rest_subsets
            r.. res

s = Solution()
print s.subsetsWithDup([1, 2, 2])
