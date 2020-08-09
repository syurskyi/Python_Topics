class Solution:
    # @param height, a list of integer
    # @return an integer
    ___ largestRectangleArea(self, height
        __ not height:
            r_ 0
        __ le.(height) __ 1:
            r_ height[0]
        stack = []  # The bottom element in the stack is the lowest
        max_area = 0
        n = le.(height)
        ___ i in range(n + 1
            w___ stack and (i __ n or height[stack[-1]] > height[i]
                h = height[stack.pop()]
                __ stack:
                    w = i - stack[-1] - 1
                ____
                    w = i
                max_area = max(max_area, h * w)
            stack.append(i)
        r_ max_area
