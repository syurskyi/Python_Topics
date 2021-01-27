class Solution:
    ___ twoSum(self, nums, target):
        store = {}

        ___ i __ range(le.(nums)):
            __ nums[i] __ store:
                r_ [store[nums[i]], i]
            ____
                store[target-nums[i]] = i


## Example Execution ##
obj = Solution()
result = obj.twoSum([2,7,11,15], 9)
print(result)