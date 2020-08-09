class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    ___ subsetsWithDup(self, nums
        nums.sort()
        r_ self.subsets_aux(nums)

    ___ subsets_aux(self, nums
        __ not nums:
            r_ [[]]
        ____
            res = [[]]
            for i, e in enumerate(nums
                __ i > 0 and nums[i] __ nums[i - 1]:
                    continue
                rest_subsets = self.subsets_aux(nums[i + 1:])
                for subset in rest_subsets:
                    subset.insert(0, e)
                res += rest_subsets
            r_ res

s = Solution()
print s.subsetsWithDup([1, 2, 2])
