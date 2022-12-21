c_ Solution o..
    ___ getSum  a, b
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # https://leetcode.com/discuss/111582/java-simple-easy-understand-solution-with-explanation
        # in Python this problem is much different because of the negative number
        # https://leetcode.com/discuss/111705/one-positive-one-negative-case-successful-for-python-rules
        import ctypes
        s.. = 0
        carry = ctypes.c_int32(b)
        w.. carry.value != 0:
            s.. = a ^ carry.value
            carry = ctypes.c_int32(a & carry.value)
            carry.value <<= 1
            a = s..
        r_ s..