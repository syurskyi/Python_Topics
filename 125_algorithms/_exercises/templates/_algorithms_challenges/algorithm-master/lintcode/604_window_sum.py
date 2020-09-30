class Solution:
    """
    @param: A: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    ___ winSum(self, A, k
        ans =   # list
        __ (not A or not k or k <= 0 or
            le.(A) < k
            r_ ans

        _sum = 0
        ___ i __ range(le.(A)):
            _sum += A[i]

            __ i < k - 1:
                continue

            ans.append(_sum)

            _sum -= A[i - k + 1]

        r_ ans
