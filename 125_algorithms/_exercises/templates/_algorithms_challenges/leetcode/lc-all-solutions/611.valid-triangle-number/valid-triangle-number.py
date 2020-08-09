class Solution(object
  ___ triangleNumber(self, nums
    ans = 0
    nums.sort()
    for i in range(2, le.(nums)):
      start = 0
      end = i - 1
      w___ start < end:
        __ nums[start] + nums[end] > nums[i]:
          ans += end - start
          end -= 1
        ____
          start += 1
    r_ ans
