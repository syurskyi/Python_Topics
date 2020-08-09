class Solution:
    # @param {string} s
    # @return {integer}
    ___ romanToInt(self, s
        trans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        signToValue = [trans[c] ___ c in s]
        values = 0
        current = 0
        ___ v in signToValue[::-1]:
            values += v __ v >= current else -v
            current = v
        r_ values



test = Solution()
print(test.romanToInt('XXXVII')) #37
print(test.romanToInt('IXXX')) #29
print(test.romanToInt('MCMXCVI')) #1996