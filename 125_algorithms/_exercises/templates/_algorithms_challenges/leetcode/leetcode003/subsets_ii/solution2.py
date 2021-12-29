class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    ___ subsetsWithDup(self, nums):
        nums.sort()
        r.. self.subsets_aux(nums)

    ___ subsets_aux(self, nums):
        __ n.. nums:
            r.. [[]]
        ____:
            res = [[]]
            ___ i, e __ enumerate(nums):
                __ i > 0 and nums[i] __ nums[i - 1]:
                    continue
                rest_subsets = self.subsets_aux(nums[i + 1:])
                ___ subset __ rest_subsets:
                    subset.insert(0, e)
                res += rest_subsets
            r.. res

s = Solution()
print s.subsetsWithDup([1, 2, 2])
