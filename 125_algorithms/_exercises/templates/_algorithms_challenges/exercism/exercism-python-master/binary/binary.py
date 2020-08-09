"""Converts binary string to integer"""

___ parse_binary(binary
    """converts string of 1 and 0 to integer"""
    num = 0
    for bit in binary:
        num <<= 1
        __ bit __ "1":
            num |= 1
        ____ bit != "0":
            raise ValueError
    r_ num
