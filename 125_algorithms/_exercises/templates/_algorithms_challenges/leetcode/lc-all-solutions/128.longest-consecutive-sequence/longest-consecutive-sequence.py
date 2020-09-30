class Solution(object
  ___ longestConsecutive(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    s = set(nums)
    ___ num __ nums:
      __ num __ s:
        s.discard(num)
        cnt = 1
        right = num + 1
        left = num - 1
        w___ left __ s:
          s.discard(left)
          cnt += 1
          left -= 1
        w___ right __ s:
          s.discard(right)
          cnt += 1
          right += 1
        ans = ma.(ans, cnt)
    r_ ans
