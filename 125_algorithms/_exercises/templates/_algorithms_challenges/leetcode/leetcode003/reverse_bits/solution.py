class Solution:
    # @param n, an integer
    # @return an integer
    ___ reverseBits(self, n):
        res = 0
        size = 32
        ___ i __ r..(size):
            __ self.test_bit(n, i):
                print(i)
                res = self.set_bit(res, size - 1 - i)
        r.. res

    ___ test_bit(self, n, i):
        mask = 1 << i
        __ n & mask > 0:
            r.. True
        r.. False

    ___ set_bit(self, n, i):
        mask = 1 << i
        r.. n | mask

s = Solution()
print(bin(43261596))
res = s.reverseBits(43261596)
print(bin(res))
