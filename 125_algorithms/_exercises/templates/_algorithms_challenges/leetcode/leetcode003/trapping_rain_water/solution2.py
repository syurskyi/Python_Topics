class Solution:
    # @param A, a list of integers
    # @return an integer
    ___ trap(self, A
        n = le.(A)
        num_max_left = [0 ___ i __ range(n)]
        num_max_right = [0 ___ i __ range(n)]
        max_left = 0
        max_right = 0
        res = 0
        ___ i __ range(n
            num_max_left[i] = max_left
            max_left = ma.(A[i], max_left)
        ___ i __ range(n
            j = n - 1 - i
            num_max_right[j] = max_right
            max_right = ma.(A[j], max_right)
        ___ i __ range(1, n - 1
            min_num = min(num_max_left[i], num_max_right[i])
            __ min_num > A[i]:
                res += min_num - A[i]
        r_ res
