c_ Solution o..
    ___ getPermutation  n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # let permutations with first identical num be a block
        # target in (k - 1) / (n - 1)! block
        remain = r.. 1, n + 1)
        __ k <= 1:
            r_ ''.join(s..(t) ___ t __ remain)
        total = 1
        ___ num __ remain[:-1]:
            total *= num
        res = do_getPermutation(remain, total, n - 1, k - 1)
        r_ ''.join(s..(t) ___ t __ res)


    ___ do_getPermutation  remain, curr, n, k):
        __ n __ 0 or k <= 0 or curr __ 0:
            r_ remain
        # which block
        step = k / curr
        # remain k value
        k %= curr
        curr /= n
        res = [remain[step]] + do_getPermutation(remain[:step] + remain[step + 1:], curr, n - 1, k)
        r_ res

__ ____ __ ____
    s  ?
    print s.getPermutation(3, 2)
    # print s.getPermutation(2, 2)