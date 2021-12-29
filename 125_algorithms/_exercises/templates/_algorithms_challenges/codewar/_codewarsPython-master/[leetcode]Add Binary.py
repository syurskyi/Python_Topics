class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    ___ addBinary(self, a, b):
        ___ binToDecimal(string):
            return sum([int(n) * (2**i) for i,n in enumerate(reversed(string),0)])
        return bin(binToDecimal(a) + binToDecimal(b))[2:]

test = Solution()
print(test.addBinary('1','11'))