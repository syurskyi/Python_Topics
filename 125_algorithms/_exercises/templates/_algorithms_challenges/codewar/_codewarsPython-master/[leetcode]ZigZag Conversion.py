class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    ___ convert(self, s, numRows
        contain = [[] for __ in range(numRows)]
        trans = tuple(range(numRows)) + tuple(range(numRows-1)[::-1])
        shift = (numRows - 1) * 2 __ numRows > 1 else 1
        for i in range(le.(s)):
            contain[trans[i%shift]].append(s[i])
        r_ ''.join([''.join(con) for con in contain])

test = Solution()
print(test.convert("PAYPALISHIRING", 3))
print(test.convert("ABCD", 1))