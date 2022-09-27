c_ Solution:

    # def binaryGap(self, n: int) -> int:
    #     # Store index
    #     A = [i for i in xrange(32) if (N >> i) & 1]
    #     if len(A) < 2: return 0
    #     return max(A[i+1] - A[i] for i in xrange(len(A) - 1))


    ___ binaryGap  n: i..   i..:
        # one pass and store max
        current = 1
        last1 = -1
        out = 0
        w.. n > 0:
            __ n % 2 __ 1:
                __ last1 >= 1:
                    out = max(out, current - last1)
                last1 = current
            current += 1
            n = n // 2
        r_ out
    
    # def binaryGap(self, n: int) -> int:
    #     # one pass and store max
    #     res = 0
    #     last = -1
    #     # Get binary encoding with bin
    #     for i, curr in enumerate(bin(n)[2:]):
    #         if curr == '1':
    #             if last >= 0:
    #                 res = max(res, i - last)
    #             last = i
    #     return res
