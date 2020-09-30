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
      r_   # list
    ans =   # list
    start = 0
    ___ i __ range(0, le.(nums) - 1
      __ nums[i] + 1 != nums[i + 1]:
        ans.append(outputRange(nums[start], nums[i]))
        start = i + 1
    ans.append(outputRange(nums[start], nums[-1]))
    r_ ans
