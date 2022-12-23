c_ Solution o..
    ___ largestRectangleArea  heights
        """
        :type heights: List[int]
        :rtype: int
        """
        # https://leetcode.com/discuss/70983/4ms-java-solution-using-o-n-stack-space-o-n-time
        largest_rectangle = 0
        ls = l.. heights)
        # heights[stack[top]] > heights[pos] > heights[stack[top - 1]]
        # keep the increase order
        stack = [-1]
        top, pos = 0, 0
        ___ pos __ r.. ls
            w.. top > 0 a.. heights[stack[top]] > heights[pos]:
                largest_rectangle = m..(largest_rectangle, heights[stack[top]] * (pos - stack[top - 1] - 1))
                top -= 1
                stack.pop()
            stack.a.. pos)
            top += 1
        w.. top > 0:
            largest_rectangle = m..(largest_rectangle, heights[stack[top]] * (ls - stack[top - 1] - 1))
            top -= 1
        r_ largest_rectangle


__ __name__ __ "__main__":
    s  ?
    print s.largestRectangleArea([2,1,5,6,2,3])
