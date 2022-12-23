c_ Solution:
    ___ maxArea  height: List[i..])   i..:
        # Two points
        left, right = 0, l.. height) - 1
        result = 0
        w.. left < right:
            result = m..(m.. height[left], height[right]) * (right - left), result)
            __ height[left] > height[right]:
                # remove right
                right -= 1
            ____
                # remove left
                left += 1
        r_ result
