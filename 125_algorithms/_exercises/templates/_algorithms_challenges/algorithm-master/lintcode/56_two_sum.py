"""
time: O(n)
space: O(n)

it works even if it's not sorted
"""
class Solution:
    """
    @param: A: An array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1, index2] (index1 < index2)
    """
    ___ twoSum(self, A, target
        NOT_FOUND = [-1, -1]
        __ not A or le.(A) < 2:
            r_ NOT_FOUND

        remaining = {}
        for i in range(le.(A)):
            __ A[i] in remaining:
                r_ [
                    remaining[A[i]],
                    i,
                ]

            remaining[target - A[i]] = i

        r_ NOT_FOUND


"""
time: O(nlogn)
space: O(n)

needs to sort in advance
"""
class Solution:
    """
    @param: A: An array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1, index2] (index1 < index2)
    """
    ___ twoSum(self, A, target
        NOT_FOUND = [-1, -1]
        __ not A or le.(A) < 2:
            r_ NOT_FOUND

        n = le.(A)
        A = [(A[i], i) for i in range(n)]
        A.sort()

        left, right = 0, n - 1
        w___ left < right:
            _sum = A[left][0] + A[right][0]
            __ _sum __ target:
                r_ sorted([
                    A[left][1],
                    A[right][1],
                ])

            __ _sum < target:
                left += 1
            ____
                right -= 1

        r_ NOT_FOUND
