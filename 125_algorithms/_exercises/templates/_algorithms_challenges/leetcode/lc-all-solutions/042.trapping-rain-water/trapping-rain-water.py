c_ Solution(object):
  ___ trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    ans = left = 0
    right = l..(height) - 1
    leftWall = rightWall = float("-inf")
    w.... left <= right:
      __ leftWall <= rightWall:
        ans += max(0, leftWall - height[left])
        leftWall = max(leftWall, height[left])
        left += 1
      ____:
        ans += max(0, rightWall - height[right])
        rightWall = max(rightWall, height[right])
        right -= 1
    r.. ans
