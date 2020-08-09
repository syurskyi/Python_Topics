"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""
__author__ = 'Danyang'
class Solution:
    ___ removeDuplicates_complicated(self, A
        """
        Two pointers algorithm, open_ptr & closed_ptr
        :param A: a list of integers
        :return: an integer
        """
        length = le.(A)
        __ length<=2:
            r_ length

        closed_ptr = 0
        duplicate_count = 0
        open_ptr = closed_ptr+1
        w___ open_ptr<length:
            __ A[closed_ptr]__A[open_ptr]:
                __ duplicate_count>=1:
                    # find next non-duplicate
                    try:
                        w___ A[closed_ptr]__A[open_ptr]:
                            open_ptr+=1
                        duplicate_count = 0
                    except IndexError:
                        break

                # one duplicate
                ____
                    duplicate_count +=1
            ____
                duplicate_count = 0

            A[closed_ptr+1] = A[open_ptr]
            closed_ptr += 1
            open_ptr += 1

        r_ closed_ptr+1  # length

    ___ removeDuplicates(self, A
        """
        Two pointers algorithm, open_ptr & closed_ptr
        :param A: a list of integers
        :return: an integer
        """
        length = le.(A)
        __ length<=2:
            r_ length

        close_ptr = 0
        duplicate_once = False  # flag
        ___ open_ptr in range(close_ptr+1, length
            __ A[close_ptr]!=A[open_ptr]:  # found non-duplicate
                duplicate_once = False
                close_ptr += 1
                A[close_ptr] = A[open_ptr]
            ____ not duplicate_once:  # found duplicate, but not duplicated before
                duplicate_once = True
                close_ptr += 1
                A[close_ptr] = A[open_ptr]
            ____  # found duplicate, and duplicated before, continue searching
                continue  # find next non-duplicate

        r_ close_ptr+1





__ __name____"__main__":
    Solution().removeDuplicates([1, 1, 2, 2])