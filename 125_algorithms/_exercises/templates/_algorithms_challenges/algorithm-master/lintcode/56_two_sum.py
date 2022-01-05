"""
time: O(n)
space: O(n)

it works even if it's not sorted
"""
c_ Solution:
    """
    @param: A: An array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1, index2] (index1 < index2)
    """
    ___ twoSum  A, target):
        NOT_FOUND = [-1, -1]
        __ n.. A o. l..(A) < 2:
            r.. NOT_FOUND

        remaining    # dict
        ___ i __ r..(l..(A)):
            __ A[i] __ remaining:
                r.. [
                    remaining[A[i]],
                    i,
                ]

            remaining[target - A[i]] = i

        r.. NOT_FOUND


"""
time: O(nlogn)
space: O(n)

needs to sort in advance
"""
c_ Solution:
    """
    @param: A: An array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1, index2] (index1 < index2)
    """
    ___ twoSum  A, target):
        NOT_FOUND = [-1, -1]
        __ n.. A o. l..(A) < 2:
            r.. NOT_FOUND

        n = l..(A)
        A = [(A[i], i) ___ i __ r..(n)]
        A.s..()

        left, right = 0, n - 1
        w.... left < right:
            _sum = A[left][0] + A[right][0]
            __ _sum __ target:
                r.. s..([
                    A[left][1],
                    A[right][1],
                ])

            __ _sum < target:
                left += 1
            ____:
                right -= 1

        r.. NOT_FOUND
