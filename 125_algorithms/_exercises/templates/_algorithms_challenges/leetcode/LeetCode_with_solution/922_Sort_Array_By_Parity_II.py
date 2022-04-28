c_ Solution o..
    # def sortArrayByParityII(self, A):
    #     N = len(A)
    #     ans = [None] * N
    #     t = 0
    #     for i, x in enumerate(A):
    #         if x % 2 == 0:
    #             ans[t] = x
    #             t += 2
    #     t = 1
    #     for i, x in enumerate(A):
    #         if x % 2 == 1:
    #             ans[t] = x
    #             t += 2
    #     # We could have also used slice assignment:
    #     # ans[::2] = (x for x in A if x % 2 == 0)
    #     # ans[1::2] = (x for x in A if x % 2 == 1)
    #     return ans

    ___ sortArrayByParityII  A):
        odd = 1
        ___ i __ xrange(0, l.. A), 2):
            __ A[i] % 2:
                w.. A[odd] % 2:
                    odd += 2
                A[i], A[odd] = A[odd], A[i]
        r_ A
