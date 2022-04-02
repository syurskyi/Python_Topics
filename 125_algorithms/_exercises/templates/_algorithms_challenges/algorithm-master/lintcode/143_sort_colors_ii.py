"""
Rainbow Sort
time: O(nlogk)
"""
c_ Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """
    ___ sortColors2  colors, k
        __ n.. colors o. n.. k:
            r..
        rainbow_sort(colors, 0, l..(colors) - 1, 1, k)

    ___ rainbow_sort  colors, start, end, color_from, color_to
        """
        like quick sort
        """
        __ color_from >= color_to:
            r..
        __ start >= end:
            r..

        left, right = start, end
        color_mid = (color_from + color_to) // 2
        w.... left <= right:
            w.... left <= right a.. colors[left] <= color_mid:
                left += 1
            w.... left <= right a.. colors[right] > color_mid:
                right -= 1
            __ left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        rainbow_sort(colors, start, right, color_from, color_mid)
        rainbow_sort(colors, left, end, color_mid + 1, color_to)


"""
TLE
Extend from sort color
time: O(nk)
"""
c_ Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """
    ___ sortColors2  colors, k
        """
        1. ensure the `min_color` in the `left_scope`,
           and the `max_color` in the `right_scope`
           in every iteration
        2. keep sorting the `mid_scope` to
           pick min/max color to the left/right scope
        """
        count = 0
        n = l..(colors)
        left, right = 0, n - 1
        i = _min = _max = 0

        w.... count < k:
            _min = _max = colors[left]
            ___ i __ r..(left + 1, right + 1
                __ colors[i] < _min:
                    _min = colors[i]
                __ colors[i] > _max:
                    _max = colors[i]

            i = left
            w.... i <= right:
                __ colors[i] __ _min:
                    colors[left], colors[i] = colors[i], colors[left]
                    left += 1
                    i += 1
                ____ _min < colors[i] < _max:
                    # leave it to
                    # the next iteration of `while count < k` to sort
                    i += 1
                ____:
                    colors[i], colors[right] = colors[right], colors[i]
                    right -= 1

            count += 2
