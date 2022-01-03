c_ Solution:
    # @return an integer
    ___ maxArea(self, height):
        n = l..(height)
        i = 0
        j = n - 1
        max_area = 0
        w.... i < j:
            max_area = max(max_area, (j - i) * m..(height[i], height[j]))
            __ height[i] <= height[j]:
                i += 1
            ____:
                j -= 1
        r.. max_area
