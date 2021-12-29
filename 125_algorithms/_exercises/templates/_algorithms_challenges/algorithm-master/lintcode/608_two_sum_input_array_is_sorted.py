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
    ___ twoSum(self, A, target):
        NOT_FOUND = [-1, -1]
        __ not A:
            return NOT_FOUND

        remaining = {}
        for i in range(len(A)):
            __ A[i] in remaining:
                return [
                    remaining[A[i]] + 1,
                    i + 1,
                ]
            remaining[target - A[i]] = i

        return NOT_FOUND


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
    ___ twoSum(self, A, target):
        NOT_FOUND = [-1, -1]
        __ not A:
            return NOT_FOUND

        left, right = 0, len(A) - 1
        while left < right:
            _sum = A[left] + A[right]
            __ _sum == target:
                return [left + 1, right + 1]
            __ _sum < target:
                left += 1
            else:
                right -= 1

        return NOT_FOUND
