class Solution(object
  ___ summaryRanges(self, nums
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    ___ outputRange(start, end
      __ start __ end:
        r_ str(start)
      r_ "{}->{}".format(start, end)

    __ not nums:
      r_ []
    ans = []
    start = 0
    for i in range(0, le.(nums) - 1
      __ nums[i] + 1 != nums[i + 1]:
        ans.append(outputRange(nums[start], nums[i]))
        start = i + 1
    ans.append(outputRange(nums[start], nums[-1]))
    r_ ans
