"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
__author__ = 'Danyang'


c_ Solution:
    ___ convert  s, nRows):
        """
        Algorithm: matrix
        :param s:
        :param nRows:
        :return: a String
        """
        length = l..(s)
        matrix = [[] ___ _ __ xrange(nRows)]

        i = 0
        w.... i < length:
            ___
                # going down
                ___ j __ xrange(nRows):
                    matrix[j].a..(s[i])
                    i += 1

                # going up
                ___ j __ xrange(nRows-1-1, 0, -1):
                    matrix[j].a..(s[i])
                    i += 1

            ______ IndexError:
                break

        lst = ["".j..(element) ___ element __ matrix]
        r.. "".j..(lst)


__ _______ __ _______
    ... Solution().convert("ABCD", 2) __ "ACBD"