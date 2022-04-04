c_ Solution:
    """
    @param: A: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    ___ winSum  A, k
        ans    # list
        __ (n.. A o. n.. k o. k <_ 0 o.
            l..(A) < k
            r.. ans

        _sum = 0
        ___ i __ r..(l..(A:
            _sum += A[i]

            __ i < k - 1:
                _____

            ans.a..(_sum)

            _sum -= A[i - k + 1]

        r.. ans
