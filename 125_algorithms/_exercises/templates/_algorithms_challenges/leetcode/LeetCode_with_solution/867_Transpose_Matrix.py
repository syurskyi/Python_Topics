c_ Solution o..
    ___ transpose  A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = l.. A), l.. A[0])
        ans = [[N..] * R ___ _ __ xrange(C)]
        ___ r, row __ e.. A):
            ___ c, val __ e.. row):
                ans[c][r] = val
        r_ ans
        # Alternative Solution:
        # return zip(*A)

    # def transpose(self, A):
    #     res = []
    #     for i in range(len(A[0])):
    #         temp = []
    #         for j in range(len(A)):
    #             temp.append(A[j][i])
    #         res.append(temp)
    #     return res
