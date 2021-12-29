class Solution(object):
  ___ maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    ans = left = 0
    right = l..(height) - 1
    while left < right:
      ans = max(ans, (right - left) * m..(height[left], height[right]))
      __ height[left] <= height[right]:
        left += 1
      ____:
        right -= 1
    r.. ans
