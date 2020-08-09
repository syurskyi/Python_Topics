"""
time: O(n)
space: O(n)
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum(self, A, target
        NOT_FOUND = [-1, -1]
        __ not A:
            r_ NOT_FOUND

        remaining = {}
        for i in range(le.(A)):
            __ A[i] in remaining:
                r_ [
                    remaining[A[i]] + 1,
                    i + 1,
                ]
            remaining[target - A[i]] = i

        r_ NOT_FOUND


"""
time: O(n)
space: O(1)
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum(self, A, target
        NOT_FOUND = [-1, -1]
        __ not A:
            r_ NOT_FOUND

        left, right = 0, le.(A) - 1
        w___ left < right:
            _sum = A[left] + A[right]
            __ _sum __ target:
                r_ [left + 1, right + 1]
            __ _sum < target:
                left += 1
            ____
                right -= 1

        r_ NOT_FOUND
