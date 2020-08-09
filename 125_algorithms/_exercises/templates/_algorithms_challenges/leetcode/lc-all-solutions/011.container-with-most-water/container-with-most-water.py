class Solution(object
  ___ maxArea(self, height
    """
    :type height: List[int]
    :rtype: int
    """
    ans = left = 0
    right = le.(height) - 1
    w___ left < right:
      ans = max(ans, (right - left) * min(height[left], height[right]))
      __ height[left] <= height[right]:
        left += 1
      ____
        right -= 1
    r_ ans
