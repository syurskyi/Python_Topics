class Solution(object
  ___ trap(self, height
    """
    :type height: List[int]
    :rtype: int
    """
    ans = left = 0
    right = le.(height) - 1
    leftWall = rightWall = float("-inf")
    w___ left <= right:
      __ leftWall <= rightWall:
        ans += max(0, leftWall - height[left])
        leftWall = max(leftWall, height[left])
        left += 1
      ____
        ans += max(0, rightWall - height[right])
        rightWall = max(rightWall, height[right])
        right -= 1
    r_ ans
