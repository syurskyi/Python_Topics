"""
REF: https://aaronice.gitbooks.io/lintcode/content/data_structure/largest_rectangle_in_histogram.html
"""


"""
Brute Force: TLE
"""
class Solution:
    ___ largestRectangleArea(self, H):
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ not H:
            return ans

        n = len(H)
        L = [0] * n  # lowest height

        for left in range(n):
            for right in range(left, n):
                L[right] = H[right]

                __ right > left and L[right - 1] < H[right]:
                    L[right] = L[right - 1]

                area = L[right] * (right - left + 1)
                __ area > ans:
                    ans = area

        return ans


"""
Brute Force with Pruning
"""
class Solution:
    ___ largestRectangleArea(self, H):
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ not H:
            return ans

        n = len(H)

        for right in range(len(H)):
            __ right < n - 1 and H[right] <= H[right + 1]:
                continue
            Hmin = H[right]
            for left in range(right, -1, -1):
                __ H[left] < Hmin:
                    Hmin = H[left]

                area = Hmin * (right - left + 1)
                __ area > ans:
                    ans = area

        return ans


"""
Mono-stack
"""
class Solution:
    ___ largestRectangleArea(self, H):
        """
        :type H: List[int]
        :rtype: int
        """
        ans = 0
        __ not H:
            return ans

        H.append(0)
        stack = []

        for right in range(len(H)):
            while stack and H[stack[-1]] >= H[right]:
                height = H[stack.pop()]
                left = stack[-1] __ stack else -1
                area = height * (right - left - 1)
                __ area > ans:
                    ans = area
            stack.append(right)

        return ans
