c_ Solution:
    # @param height, a list of integer
    # @return an integer
    ___ largestRectangleArea  height
        __ n.. height:
            r.. 0
        __ l..(height) __ 1:
            r.. height[0]
        stack    # list  # The bottom element in the stack is the lowest
        max_area = 0
        n = l..(height)
        ___ i __ r..(n + 1
            w.... stack a.. (i __ n o. height[stack[-1]] > height[i]
                h = height[stack.pop()]
                __ stack:
                    w = i - stack[-1] - 1
                ____:
                    w = i
                max_area = m..(max_area, h * w)
            stack.a..(i)
        r.. max_area
