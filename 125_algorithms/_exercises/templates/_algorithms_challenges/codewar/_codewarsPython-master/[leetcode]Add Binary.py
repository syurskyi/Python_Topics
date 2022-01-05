c_ Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    ___ addBinary  a, b):
        ___ binToDecimal(s__):
            r.. s..([i..(n) * (2**i) ___ i,n __ e..(r..(s__),0)])
        r.. bin(binToDecimal(a) + binToDecimal(b))[2:]

test = Solution()
print(test.addBinary('1','11'))