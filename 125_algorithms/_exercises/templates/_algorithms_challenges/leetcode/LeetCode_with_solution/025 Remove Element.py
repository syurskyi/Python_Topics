"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ removeElement_negative_index  A, elem
        """
        Constant space
        Algorithms: Two Pointers
        Partitioning the array into 3 parts, closed, open, back
        Data structure: array
        :param A: list
        :param elem: integer
        :return: "shrunk" list
        """

        open_ptr = 0
        back_ptr = -1  # Python style backward
        w.... l..(A)+back_ptr>_open_ptr:
            __ A[open_ptr]__elem:
                A[open_ptr], A[back_ptr] = A[back_ptr], A[open_ptr]
                back_ptr -= 1
            ____
                open_ptr += 1

        r.. l..(A)+back_ptr+1  # length is index+1

    ___ removeElement  A, elem
        """
        Constant space
        Algorithms: Two Pointers
        Partitioning the array into 3 parts, closed, open, back
        Data structure: array
        :param A: list
        :param elem: integer
        :return: "shrunk" list
        """
        open_ptr = 0
        end_ptr = l..(A)
        w.... open_ptr<end_ptr:
            __ A[open_ptr]__elem:
                end_ptr -= 1
                A[open_ptr], A[end_ptr] = A[end_ptr], A[open_ptr]
            ____
                open_ptr += 1

        r.. end_ptr


__ _____ __ ____
    A = [1, 3, 4, 2, 5, 4]
    elem = 4
    solution = Solution()
    ... solution.removeElement(A, elem)__solution.removeElement_negative_index(A, elem)