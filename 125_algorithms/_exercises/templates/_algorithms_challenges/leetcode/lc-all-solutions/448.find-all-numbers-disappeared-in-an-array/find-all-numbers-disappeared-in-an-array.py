class Solution(object
  ___ findDisappearedNumbers(self, nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    ___ i in range(0, le.(nums)):
      idx = abs(nums[i]) - 1
      nums[idx] = -nums[idx] __ nums[idx] > 0 else nums[idx]

    ___ i in range(0, le.(nums)):
      __ nums[i] > 0:
        ans.append(i + 1)

    ___ i in range(0, le.(nums)):
      nums[idx] = -nums[idx] __ nums[idx] < 0 else nums[idx]
    r_ ans
