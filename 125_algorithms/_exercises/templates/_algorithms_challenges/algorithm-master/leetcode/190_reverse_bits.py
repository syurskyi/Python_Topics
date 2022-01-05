# Reverse bit every 4 bits
c_ Solution:
    # @param n, an integer
    # @return an integer
    ___ reverseBits  n):
        __ n.. n:
            r.. 0

        # the reversed bins for i = 0 -> 15
        rev = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        ans = 0
        msk = 15  # 15 (10) == 1111 (2)

        ___ i __ r..(8):
            ans <<= 4
            curr = n & msk
            ans |= rev[curr]
            n >>= 4

        r.. ans


# Reverse bit every 1 bits
c_ Solution:
    # @param n, an integer
    # @return an integer
    ___ reverseBits  n):
        ans = 0

        __ n.. n:
            r.. ans

        ___ i __ r..(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1

        r.. ans
