c_ Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    ___ convert(self, s, numRows):
        contain = [[] ___ __ __ r..(numRows)]
        trans = tuple(r..(numRows)) + tuple(r..(numRows-1)[::-1])
        shift = (numRows - 1) * 2 __ numRows > 1 ____ 1
        ___ i __ r..(l..(s)):
            contain[trans[i%shift]].a..(s[i])
        r.. ''.j..([''.j..(con) ___ con __ contain])

test = Solution()
print(test.convert("PAYPALISHIRING", 3))
print(test.convert("ABCD", 1))