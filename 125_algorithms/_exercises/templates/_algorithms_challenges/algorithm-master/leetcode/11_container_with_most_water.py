c_ Solution:
    ___ maxArea  H
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ n.. H:
            r.. ans

        left, right = 0, l..(H) - 1
        w.... left < right:
            area = m..(H[left], H[right]) * (right - left)
            __ area > ans:
                ans = area

            __ H[left] < H[right]:
                left += 1
            ____
                right -= 1

        r.. ans
