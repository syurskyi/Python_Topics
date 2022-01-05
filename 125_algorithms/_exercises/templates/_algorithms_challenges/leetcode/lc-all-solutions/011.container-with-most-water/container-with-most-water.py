c_ Solution(o..):
  ___ maxArea  height):
    """
    :type height: List[int]
    :rtype: int
    """
    ans = left = 0
    right = l..(height) - 1
    w.... left < right:
      ans = m..(ans, (right - left) * m..(height[left], height[right]))
      __ height[left] <= height[right]:
        left += 1
      ____:
        right -= 1
    r.. ans
