class Solution(object
  ___ longestConsecutive(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    s = set(nums)
    ___ num in nums:
      __ num in s:
        s.discard(num)
        cnt = 1
        right = num + 1
        left = num - 1
        w___ left in s:
          s.discard(left)
          cnt += 1
          left -= 1
        w___ right in s:
          s.discard(right)
          cnt += 1
          right += 1
        ans = max(ans, cnt)
    r_ ans
