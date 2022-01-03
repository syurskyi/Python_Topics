c_ Solution:
    """
    @param: A: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    ___ findPosition(self, A, target):
        __ n.. A:
            r.. -1

        left, right = 0, l..(A) - 1
        w.... left + 1 < right:
            mid = (left + right) // 2
            __ A[mid] __ target:
                r.. mid
            __ A[mid] < target:
                left = mid
            ____:
                right = mid

        __ A[left] __ target:
            r.. left
        __ A[right] __ target:
            r.. right
        r.. -1
