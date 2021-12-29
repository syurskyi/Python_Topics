class Solution:
    ___ twoSum(self, nums: List[i..], target: i..) -> List[i..]:
        m  {}
        n  len(nums)
        for i in range(0,n):
            goal  target - nums[i]
            __(goal in m):
                return [m[goal], i]
            m[nums[i]]  i
        