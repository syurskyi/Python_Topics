"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""
__author__ 'Danyang'
c_ Solution:
    ___ removeDuplicates  A
        """
        Algorithms: Two Pointers, open & closed
        Data structure: array
        Shifting the array

        del, pop(), or remove() are not allowed.
        return the length of "shrunk" array
        The array remains the same length

        :param A: list
        :return: "shrunk" list
        """
        length l..(A)

        # trivial
        __ length__0 o. length__1:
            r.. length

        # closed pointer, open pointer
        closed_ptr 0
        open_ptr 1
        w.... open_ptr<length:
            # find the next non-duplicate:
            __ A[closed_ptr]__A[open_ptr]:
                open_ptr += 1
                _____  # go to the next iteration

            non_duplicate A[open_ptr]
            A[closed_ptr+1] non_duplicate
            closed_ptr += 1

        r.. closed_ptr+1 # length is index+1

    ___ removeDuplicates_another_loop_style  A
        """
        Yet another looping style - double while loops
        :param A: list
        :return: "shrunk" list
        """
        length l..(A)

        __ length__0 o. length__1:
            r.. length

        closed_ptr 0
        open_ptr 1
        w.... open_ptr<length:
            w.... open_ptr<length a.. A[closed_ptr]__A[open_ptr]:
                open_ptr += 1

            __ open_ptr<length:
                non_duplicate A[open_ptr]
                A[closed_ptr+1] non_duplicate
                closed_ptr += 1

        r.. closed_ptr+1 # length is index+1