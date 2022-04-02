c_ Solution(o..
  ___ trap  height
    """
    :type height: List[int]
    :rtype: int
    """
    ans = left = 0
    right = l..(height) - 1
    leftWall = rightWall = f__("-inf")
    w.... left <= right:
      __ leftWall <= rightWall:
        ans += m..(0, leftWall - height[left])
        leftWall = m..(leftWall, height[left])
        left += 1
      ____:
        ans += m..(0, rightWall - height[right])
        rightWall = m..(rightWall, height[right])
        right -= 1
    r.. ans
