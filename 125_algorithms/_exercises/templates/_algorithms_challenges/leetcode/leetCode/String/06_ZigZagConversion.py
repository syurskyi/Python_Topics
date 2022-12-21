c.. Solution o..
    ___ convert  s, numRows
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        __ n.. s:
            r_ ""
        __ numRows __ 1:
            r_ s

        len_s = l..(s)
        zigzag_list   # list
        magic_number = 2 * numRows - 2

        ___ row __ r..(numRows
            index = row
            _____ index < len_s:
                zigzag_list.append(s[index])
                __ row != 0 and row != numRows - 1:
                    next_num = magic_number + index - 2 * row
                    __ next_num < len_s:
                        zigzag_list.append(s[next_num])
                index += magic_number

        r_ "".join(zigzag_list)

"""
""
1
"ABC"
1
"PAYPALISHIRING"
5
"""
