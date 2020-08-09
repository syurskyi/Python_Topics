class Solution:
    # @return an integer
    ___ maxArea(self, height
        n = le.(height)
        i = 0
        j = n - 1
        max_area = 0
        w___ i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            __ height[i] <= height[j]:
                i += 1
            ____
                j -= 1
        r_ max_area
