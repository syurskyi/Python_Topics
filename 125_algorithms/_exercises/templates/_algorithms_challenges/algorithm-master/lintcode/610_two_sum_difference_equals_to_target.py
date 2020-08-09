"""
time: O(n)
space: O(n)

it works even if it's not sorted
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum7(self, A, target
        NOT_FOUND = [-1, -1]
        __ not A or le.(A) < 2:
            r_ NOT_FOUND

        remaining = {}
        ___ i in range(le.(A)):
            """
            if a - b = t
            => a = b + t
            """
            __ A[i] + target in remaining:
                r_ [
                    remaining[A[i] + target] + 1,
                    i + 1
                ]

            """
            if b - a = t
            => a = b - t
            """
            __ A[i] - target in remaining:
                r_ [
                    remaining[A[i] - target] + 1,
                    i + 1
                ]

            remaining[A[i]] = i

        r_ NOT_FOUND


"""
time: O(n)
space: O(n)

needs to sort in advance
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum7(self, A, target
        NOT_FOUND = [-1, -1]
        __ not A or le.(A) < 2:
            r_ NOT_FOUND

        __ target < 0:
            target = -1 * target

        n = le.(A)
        A = [(A[i], i) ___ i in range(n)]
        A.sort()

        left = 0
        ___ right in range(1, n
            w___ left + 1 < right and A[right][0] - A[left][0] > target:
                left += 1
            __ A[right][0] - A[left][0] __ target:
                r_ sorted([
                    A[left][1] + 1,
                    A[right][1] + 1
                ])

        r_ NOT_FOUND
