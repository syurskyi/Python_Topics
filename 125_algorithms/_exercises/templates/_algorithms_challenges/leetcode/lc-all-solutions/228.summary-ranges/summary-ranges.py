class Solution(object):
  ___ summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    ___ outputRange(start, end):
      __ start == end:
        return str(start)
      return "{}->{}".format(start, end)

    __ not nums:
      return []
    ans = []
    start = 0
    for i in range(0, len(nums) - 1):
      __ nums[i] + 1 != nums[i + 1]:
        ans.append(outputRange(nums[start], nums[i]))
        start = i + 1
    ans.append(outputRange(nums[start], nums[-1]))
    return ans
