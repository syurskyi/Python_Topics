"""
time: O(n)
space: O(n)
"""
c_ Solution:
    """
    @param: A: an array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum  A, target
        N.. [-1, -1]
        __ n.. A:
            r.. NOT_FOUND

        remaining    # dict
        ___ i __ r..(l..(A:
            __ A[i] __ remaining:
                r.. [
                    remaining[A[i]] + 1,
                    i + 1,
                ]
            remaining[target - A[i]] i

        r.. NOT_FOUND


"""
time: O(n)
space: O(1)
"""
c_ Solution:
    """
    @param: A: an array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum  A, target
        NOT_FOUND [-1, -1]
        __ n.. A:
            r.. NOT_FOUND

        left, right 0, l..(A) - 1
        w.... left < right:
            _sum A[left] + A[right]
            __ _sum __ target:
                r.. [left + 1, right + 1]
            __ _sum < target:
                left += 1
            ____
                right -_ 1

        r.. NOT_FOUND
