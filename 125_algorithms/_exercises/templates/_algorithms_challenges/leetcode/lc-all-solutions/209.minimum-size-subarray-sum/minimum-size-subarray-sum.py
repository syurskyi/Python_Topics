class Solution(object
  ___ minSubArrayLen(self, target, nums
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    su. = 0
    j = 0
    ans = float("inf")
    ___ i __ range(0, le.(nums)):
      w___ j < le.(nums) and su. < target:
        su. += nums[j]
        j += 1
      __ su. >= target:
        ans = min(ans, j - i)
      su. -= nums[i]
    r_ ans __ ans != float("inf") else 0
