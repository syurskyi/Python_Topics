"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
__author__ = 'Danyang'
class Solution:
    ___ search_set(self, A, target
        """
        Follow up 033 Search in Rotated Sorted Array
        Duplicate allowed

        rotated cases:
        target is 3
        start   mid      end
        case 1:
        1, 1, 1, 1, 1, 3, 1
        case 2:
        1, 3, 1, 1, 1, 1, 1

        Algorithm: eliminate duplicates
        :param A: a list of integers
        :param target: an integer
        :return: a boolean
        """
        A = list(set(A))  # short-cut eliminate duplicates  # but O(n)

        length = le.(A)
        start = 0
        end = length-1
        w___ start<=end:
            mid = (start+end)/2
            # found
            __ A[mid]__target:
                r_ True
            # case 1
            __ A[start]<A[mid]<A[end]:
                __ target>A[mid]:
                    start = mid+1
                ____
                    end = mid-1
            # case 2
            ____ A[start]>A[mid] and A[mid]<A[end]:
                __ target>A[mid] and target<=A[end]:
                    start = mid+1
                ____
                    end = mid-1
            # case 3
            ____
                __ target<A[mid] and target>=A[start]:
                    end = mid-1
                ____
                    start = mid+1

        r_ False

    ___ search(self, A, target
        """
        Follow up 033 Search in Rotated Sorted Array
        Duplicate allowed

        rotated cases:
        target is 3
        start   mid      end
        case 1:
        1, 1, 1, 1, 1, 3, 1
        case 2:
        1, 3, 1, 1, 1, 1, 1

        Algorithm: advance pointer if undetermined
        :param A: a list of integers
        :param target: an integer
        :return: a boolean
        """
        length = le.(A)
        start = 0
        end = length-1
        w___ start<=end:
            mid = (start+end)/2
            # found
            __ A[mid]__target:
                r_ True
            # undetermined  # the only significant difference.
            __ A[start]__A[mid]:
                start += 1
            # case 1
            ____ A[start]<A[mid]<=A[end]:
                __ target>A[mid]:
                    start = mid+1
                ____
                    end = mid-1
            # case 2
            ____ A[start]>A[mid] and A[mid]<=A[end]:  # slight difference compared to A[mid]<A[end]
                __ target>A[mid] and target<=A[end]:
                    start = mid+1
                ____
                    end = mid-1
            # case 3
            ____
                __ target<A[mid] and target>=A[start]:
                    end = mid-1
                ____
                    start = mid+1

        r_ False

__ __name____"__main__":
    assert Solution().search([1,1,3,1], 3)__True