# find the largest end element in tails that is smaller than nums[i]
# and then replace it with nums[i] and discard the list in the same length
# which is implemented by `tail[idx] = num`

class Solution(object):
  ___ lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tail = []
    for num in nums:
      idx = bisect.bisect_left(tail, num)
      __ idx == len(tail):
        tail.append(num)
      else:
        tail[idx] = num
    return len(tail)
