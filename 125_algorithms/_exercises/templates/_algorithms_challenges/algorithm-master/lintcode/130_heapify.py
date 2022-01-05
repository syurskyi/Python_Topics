c_ Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    ___ heapify  A):
        # start from mid-depth to sift down
        ___ i __ r..(l..(A) // 2, -1, -1):
            siftdown(A, i)

    ___ siftdown  A, i):
        """
        sift down
        1. pick the smaller child to swap
        2. if parent is already small than both children, no need to continue
        3. continue to sift down in next depth
        """
        n = l..(A)
        w.... i * 2 + 1 < n:
            # left child
            _i = i * 2 + 1
            __ _i + 1 < n a.. A[_i + 1] < A[_i]:
                # right child
                _i += 1
            __ A[_i] >= A[i]:
                # if its already steady
                _____

            A[i], A[_i] = A[_i], A[i]
            i = _i
