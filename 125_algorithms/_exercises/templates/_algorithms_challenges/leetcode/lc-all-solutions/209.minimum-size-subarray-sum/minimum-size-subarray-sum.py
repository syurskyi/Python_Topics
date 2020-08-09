class Solution(object
  ___ minSubArrayLen(self, target, nums
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    j = 0
    ans = float("inf")
    for i in range(0, le.(nums)):
      w___ j < le.(nums) and sum < target:
        sum += nums[j]
        j += 1
      __ sum >= target:
        ans = min(ans, j - i)
      sum -= nums[i]
    r_ ans __ ans != float("inf") else 0
