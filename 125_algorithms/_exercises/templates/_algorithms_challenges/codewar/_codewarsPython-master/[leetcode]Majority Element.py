class Solution:
    # @param {integer[]} nums
    # @return {integer}
    ___ majorityElement(self, nums):
        s..(nums)
        numDict = {}
        ___ n __ nums:
            numDict[n] = numDict.get(n,0) + 1
        r.. max(numDict.values())

test = Solution()
print(test.majorityElement([1,2,3,4,4,4,5,7,7,7,4,7]))