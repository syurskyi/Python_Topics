# ZigZag Conversion
# Question: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P A H N
# A P L S I I G
# Y I R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# Solutions:


______ functools
______ operator

c_ Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    ___ convert(self, s, numRows):
        __ numRows __ 1 o. numRows >_ le.(s):
            r_ s
        zigzag _ [[] ___ x __ ra..(numRows)]
        row, step _ 0, 1
        ___ c __ s:
            zigzag[row] +_ c,
            __ row __ 0:
                step _ 1
            ____ row __ numRows - 1:
                step _ -1
            row +_ step
        r_ ''.j..(functools.reduce(operator.add, zigzag))


Solution().convert("PAYPALISHIRING", 3)