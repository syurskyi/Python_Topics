import sys


# Recursive Approach
___ mcm(seq, i, j
    __ i __ j:
        r_ 0
    min_ops = sys.maxsize
    ___ k __ range(i, j
        ops = mcm(seq, i, k) + mcm(seq, k+1, j) + seq[i-1]*seq[k]*seq[j]
        min_ops = min(ops, min_ops)
    r_ min_ops


# DP : Top Down Approach
___ mcm_topdown(seq, i, j, arr
    __ i __ j:
        r_ 0
    __ arr[i][j] >= 0:
        r_ arr[i][j]
    min_ops = sys.maxsize
    ___ k __ range(i, j
        min_ops = min(min_ops, (mcm_topdown(seq, i, k, arr) + mcm_topdown(seq, k+1, j, arr) + seq[i-1]*seq[k]*seq[j]))
    arr[i][j] = min_ops
    r_ arr[i][j]


# DP : Bottom Up Approach
___ mcm_bottomup(seq, n
    arr = [[0 ___ i __ range(n)] ___ i __ range(n)]
    ___ i __ range(n
        arr[i][i] = 0
    ___ le_ __ range(2, n
        ___ i __ range(1, n-le_+1
            j = i + le_ - 1
            __ j __ n:
                continue
            min_ops = sys.maxsize
            ___ k __ range(i, j
                min_ops = min(min_ops, (arr[i][k] + arr[k+1][j] + seq[i - 1] * seq[k] * seq[j]))
            arr[i][j] = min_ops
    ___ i __ range(n
        ___ j __ range(n
            print(arr[i][j], end=' ')
        print()
    r_ arr[1][n-1]


__ ___ __ '__main__':
    seq = [4, 3, 2, 1, 5]
    n = le_(seq)
    print(mcm(seq, 1, n - 1))

    arr = [[-1 ___ i __ range(n)]___ i __ range(n)]
    print('top down:', mcm_topdown(seq, 1, n-1, arr))

    print('bottom up:', mcm_bottomup(seq, n))
