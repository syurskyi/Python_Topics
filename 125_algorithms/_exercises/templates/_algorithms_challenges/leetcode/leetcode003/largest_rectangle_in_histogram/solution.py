class Solution:
    # @param height, a list of integer
    # @return an integer
    ___ largestRectangleArea(self, height):
        __ not height:
            return 0
        __ len(height) == 1:
            return height[0]
        stack = []  # The bottom element in the stack is the lowest
        max_area = 0
        n = len(height)
        for i in range(n + 1):
            while stack and (i == n or height[stack[-1]] > height[i]):
                h = height[stack.pop()]
                __ stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
