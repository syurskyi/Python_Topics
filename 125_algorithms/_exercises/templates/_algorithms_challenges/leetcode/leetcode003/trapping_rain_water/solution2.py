c_ Solution:
    # @param A, a list of integers
    # @return an integer
    ___ trap  A
        n l..(A)
        num_max_left [0 ___ i __ r..(n)]
        num_max_right [0 ___ i __ r..(n)]
        max_left 0
        max_right 0
        res 0
        ___ i __ r..(n
            num_max_left[i] max_left
            max_left m..(A[i], max_left)
        ___ i __ r..(n
            j n - 1 - i
            num_max_right[j] max_right
            max_right m..(A[j], max_right)
        ___ i __ r..(1, n - 1
            min_num m..(num_max_left[i], num_max_right[i])
            __ min_num > A[i]:
                res += min_num - A[i]
        r.. res
