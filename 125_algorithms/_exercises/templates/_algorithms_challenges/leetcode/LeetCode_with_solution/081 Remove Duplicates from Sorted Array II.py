"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""
__author__ = 'Danyang'
c_ Solution:
    ___ removeDuplicates_complicated  A):
        """
        Two pointers algorithm, open_ptr & closed_ptr
        :param A: a list of integers
        :return: an integer
        """
        length = l..(A)
        __ length<=2:
            r.. length

        closed_ptr = 0
        duplicate_count = 0
        open_ptr = closed_ptr+1
        w.... open_ptr<length:
            __ A[closed_ptr]__A[open_ptr]:
                __ duplicate_count>=1:
                    # find next non-duplicate
                    ___
                        w.... A[closed_ptr]__A[open_ptr]:
                            open_ptr+=1
                        duplicate_count = 0
                    ______ IndexError:
                        break

                # one duplicate
                ____:
                    duplicate_count +=1
            ____:
                duplicate_count = 0

            A[closed_ptr+1] = A[open_ptr]
            closed_ptr += 1
            open_ptr += 1

        r.. closed_ptr+1  # length

    ___ removeDuplicates  A):
        """
        Two pointers algorithm, open_ptr & closed_ptr
        :param A: a list of integers
        :return: an integer
        """
        length = l..(A)
        __ length<=2:
            r.. length

        close_ptr = 0
        duplicate_once = F..  # flag
        ___ open_ptr __ r..(close_ptr+1, length):
            __ A[close_ptr]!=A[open_ptr]:  # found non-duplicate
                duplicate_once = F..
                close_ptr += 1
                A[close_ptr] = A[open_ptr]
            ____ n.. duplicate_once:  # found duplicate, but not duplicated before
                duplicate_once = T..
                close_ptr += 1
                A[close_ptr] = A[open_ptr]
            ____:  # found duplicate, and duplicated before, continue searching
                _____  # find next non-duplicate

        r.. close_ptr+1





__ _____ __ ____
    Solution().removeDuplicates([1, 1, 2, 2])