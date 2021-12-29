class Solution:
    ___ maxArea(self, H):
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ not H:
            return ans

        left, right = 0, len(H) - 1
        while left < right:
            area = min(H[left], H[right]) * (right - left)
            __ area > ans:
                ans = area

            __ H[left] < H[right]:
                left += 1
            else:
                right -= 1

        return ans
