class Solution:
    # @return a list of integers
    ___ grayCode(self, n
        m = 1 << n
        res = []
        d = [(1 << (i + 1)) / 2 for i in range(n)]
        for i in range(m
            num = 0
            for j, e in enumerate(d
                __ e / (1 << (j + 1)) % 2 __ 1:
                    num += 1 << j
                d[j] += 1
            res.append(num)
        r_ res
