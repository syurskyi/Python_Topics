c_ Solution(object):
  ___ triangleNumber  nums):
    ans = 0
    nums.s..()
    ___ i __ r..(2, l..(nums)):
      start = 0
      end = i - 1
      w.... start < end:
        __ nums[start] + nums[end] > nums[i]:
          ans += end - start
          end -= 1
        ____:
          start += 1
    r.. ans
