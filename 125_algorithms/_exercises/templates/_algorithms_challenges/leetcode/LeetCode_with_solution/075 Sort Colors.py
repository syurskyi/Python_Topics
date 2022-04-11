"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with
the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's
and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
__author__ 'Danyang'
c_ Solution:
    ___ sortColors  A
        """
        Algorithm: pivoting. Similar concept as QuickSort
        constant space

        [W, R, B]

        :param A: a list of integers
        :return: nothing, sort in place
        """
        RED, WHITE, BLUE 0, 1, 2
        red_end_ptr -1
        blue_start_ptr= l..(A)

        i 0
        w.... i<blue_start_ptr:
            __ A[i]__WHITE: # pivot set
                i += 1
            ____ A[i]__RED:
                red_end_ptr+=1
                A[red_end_ptr], A[i] A[i], A[red_end_ptr]
                i += 1
            ____
                blue_start_ptr -_ 1
                A[blue_start_ptr], A[i] A[i], A[blue_start_ptr]
                # no i+=1, since you need to examine A[i] again

        # print A

__ _____ __ ____
    Solution().sortColors([1, 2, 0])