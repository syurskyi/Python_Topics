class Solution:
    ___ findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        Assuming the answer we want is `Ans = Max(A[i] + A[i+1] + ... + A[i+k-1])`,
        and we define the `P[i] = A[0] + A[1] + ... + A[i-1]`,
        so that `Ans = Max(P[i+k] - P[i])`, and `i+k-1 < n -> i < n-k+1`
        * max index in P is `i+k`, so in A is `(i+k)-1`, `i+k-1 < n`
        """
        """
        P[0] = 0
        P[1] = P[0] + A[0]
        P[2] = P[1] + A[1]
        P[i] = P[i-1] + A[i-1]
             = A[0] + A[1] + ... + A[i-1]
        """
        P = [0]
        ___ x __ nums: P.a..(P[-1] + x)
        max_sum = max(P[i+k] - P[i] ___ i __ r..(l..(nums) - k + 1))
        r.. max_sum / float(k)

class Solution:
    ___ findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        Assuming k = 3
        i: 0 1 2 3
              |--> Start to find max sum
                |--> Start to remove past child
        """
        max_sum, tmp_sum = float('-inf'), 0
        ___ i __ r..(l..(nums)):
            tmp_sum += nums[i]
            __ i >= k:
                tmp_sum -= nums[i-k]
            __ i + 1 >= k:
                max_sum = max(max_sum, tmp_sum)
        r.. max_sum / float(k)
