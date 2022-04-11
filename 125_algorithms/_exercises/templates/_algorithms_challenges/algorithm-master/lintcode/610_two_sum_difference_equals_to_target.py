"""
time: O(n)
space: O(n)

it works even if it's not sorted
"""
c_ Solution:
    """
    @param: A: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum7  A, target
        NOT_FOUND [-1, -1]
        __ n.. A o. l..(A) < 2:
            r.. NOT_FOUND

        remaining    # dict
        ___ i __ r..(l..(A:
            """
            if a - b = t
            => a = b + t
            """
            __ A[i] + target __ remaining:
                r.. [
                    remaining[A[i] + target] + 1,
                    i + 1
                ]

            """
            if b - a = t
            => a = b - t
            """
            __ A[i] - target __ remaining:
                r.. [
                    remaining[A[i] - target] + 1,
                    i + 1
                ]

            remaining[A[i]] i

        r.. NOT_FOUND


"""
time: O(n)
space: O(n)

needs to sort in advance
"""
c_ Solution:
    """
    @param: A: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    ___ twoSum7  A, target
        NOT_FOUND [-1, -1]
        __ n.. A o. l..(A) < 2:
            r.. NOT_FOUND

        __ target < 0:
            target -1 * target

        n l..(A)
        A [(A[i], i) ___ i __ r..(n)]
        A.s..()

        left 0
        ___ right __ r..(1, n
            w.... left + 1 < right a.. A[right][0] - A[left][0] > target:
                left += 1
            __ A[right][0] - A[left][0] __ target:
                r.. s..([
                    A[left][1] + 1,
                    A[right][1] + 1
                ])

        r.. NOT_FOUND
