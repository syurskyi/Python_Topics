class Solution:
    ___ maxArea(self, H
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ not H:
            r_ ans

        left, right = 0, le.(H) - 1
        w___ left < right:
            area = min(H[left], H[right]) * (right - left)
            __ area > ans:
                ans = area

            __ H[left] < H[right]:
                left += 1
            ____
                right -= 1

        r_ ans
