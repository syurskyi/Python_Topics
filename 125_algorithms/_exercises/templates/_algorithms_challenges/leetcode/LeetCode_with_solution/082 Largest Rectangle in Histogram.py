"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of
largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""
_______ sys
__author__ = 'Danyang'


class Solution:
    ___ largestRectangleArea(self, height):
        """
        O(2*n)
        every bar at most enter the stack once and is popped out once.

        Algorithm: Stack.
        Keep a stack storing the bars increasing order, then calculate the area by popping out the stack to get the
        currently lowest bar which determines the height of the rectangle.

        The popping out is triggered when height being scanned violates increasing order. Keep popping out until not
        violate the increasing order.

        When calculate the area: area = height[last]*( i-(inc_stack[-1]+1) ) rather than area = height[last] * (i-last),
        since originally from inc_stack[-1]+1 to last are higher bars already popped out, which should be included in
        the calculation.

        pay attention to corner case

        reference: http://fisherlei.blogspot.sg/2012/12/leetcode-largest-rectangle-in-histogram.html
        :param height: a list of int
        :return: int
        """
        __ n.. height:
            r.. 0

        n = l..(height)
        gmax = -sys.maxint-1
        inc_stack    # list  # store the idx, increasing stack

        ___ i __ xrange(n):
            w.... inc_stack a.. height[inc_stack[-1]] > height[i]:
                last = inc_stack.pop()
                __ inc_stack:  # calculate area when popping
                    area = height[last]*(i-(inc_stack[-1]+1))
                ____:
                    area = height[last]*i
                gmax = max(gmax, area)

            inc_stack.a..(i)

        # after processing all heights, process the remaining stack
        i = n
        w.... inc_stack:
            last = inc_stack.pop()
            __ inc_stack:
                area = height[last]*(i-(inc_stack[-1]+1))
            ____:
                area = height[last]*i
            gmax = max(gmax, area)

        r.. gmax

    ___ largestRectangleArea_TLE(self, height):
        """
        O(n*n)
        :param height: a list of int
        :return: int
        """
        __ n.. height:
            r.. 0

        max_area = -1<<32
        ___ ind, val __ e..(height):
            min_h = val
            max_area = max(max_area, val*1)
            ___ j __ xrange(ind, -1, -1):
                min_h = m..(min_h, height[j])
                current_area = min_h*(ind-j+1)
                max_area = max(max_area, current_area)

        r.. max_area


    ___ largestRectangleArea_complex(self, height):
        """
        O(n*n) + prune

        starting from every column, scan backward to calculate the max possible area under current column

        reference: http://fisherlei.blogspot.sg/2012/12/leetcode-largest-rectangle-in-histogram.html
        :param height: a list of int
        :return: int
        """
        __ n.. height:
            r.. 0

        global_max = -1<<32
        ___ ind, val __ e..(height):
            __ ind+1<l..(height) a.. val<=height[ind+1]:  # PRUNE, find until peak
                continue

            min_h = val
            global_max = max(global_max, min_h*1)
            ___ j __ xrange(ind, -1, -1):  # scanning backward
                min_h = m..(min_h, height[j])
                current_area = min_h*(ind-j+1)
                global_max = max(global_max, current_area)

        r.. global_max


    ___ largestRectangleArea_error(self, height):
        """
        O(n)

        Algorithm: Stack.

        reference: http://fisherlei.blogspot.sg/2012/12/leetcode-largest-rectangle-in-histogram.html
        :param height: a list of int
        :return: int
        """
        __ n.. height:
            r.. 0

        length = l..(height)
        global_max = -1<<32
        inc_stack    # list  # store the pointer

        i = 0
        w.... i<length:
            __ n.. inc_stack o. height[i]>=height[inc_stack[-1]]:
                inc_stack.a..(i)
                i += 1
            ____:
                last = inc_stack.pop()
                __ inc_stack:
                    area = height[last] * (i-last)
                ____:
                    area = height[last] * i
                global_max = max(global_max, area)

        # remaining stack
        w.... inc_stack:
            last = inc_stack.pop()
            __ inc_stack:
                area = height[last]*(i-last)
            ____:
                area = height[last]*i
            global_max = max(global_max, area)
        r.. global_max


__ __name____"__main__":
    # height = [2, 1, 2]
    height = [4, 2, 0, 3, 2, 5]
    ... Solution().largestRectangleArea(height) __ Solution().largestRectangleArea_complex(height)




