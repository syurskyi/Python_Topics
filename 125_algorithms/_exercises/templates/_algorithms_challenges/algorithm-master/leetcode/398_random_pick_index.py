____ r__ _______ randint


c_ Solution:
    ___ - , A
        """
        :type A: List[int]
        """
        A = A

    ___ pick  target
        """
        :type target: int
        :rtype: int
        """
        res = -1
        cnt = 0

        ___ i __ r..(l..(A)):
            __ A[i] != target:
                _____
            cnt += 1
            __ randint(1, cnt) __ cnt:
                res = i

        r.. res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
