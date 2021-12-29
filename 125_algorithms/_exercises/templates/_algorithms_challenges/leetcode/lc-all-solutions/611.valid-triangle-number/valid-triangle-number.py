class Solution(object):
  ___ triangleNumber(self, nums):
    ans = 0
    nums.sort()
    for i in range(2, len(nums)):
      start = 0
      end = i - 1
      while start < end:
        __ nums[start] + nums[end] > nums[i]:
          ans += end - start
          end -= 1
        else:
          start += 1
    return ans
