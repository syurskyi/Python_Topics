c_ Solution:
    # @param A, a list of integer
    # @return an integer
    ___ singleNumber  A
        # Assume 32-bit integer
        num_of_bits 32  # Change this to 64 on 64-bit platform
        res_bit 0
        res 0
        # First check whether the single number is negative
        ___ num __ A:
            bit 1 __ num & (1 << (num_of_bits - 1 != 0 ____ 0
            res_bit (res_bit + bit) % 3
        positive T.. __ res_bit __ 0 ____ F..

        ___ i __ r..(num_of_bits - 1
            res_bit 0
            # For each bit of each number, calculate each bit
            # of the single number
            ___ num __ A:
                bit 1 __ num & (1 << i) != 0 ____ 0
                res_bit (res_bit + bit) % 3
            # If single number is positive
            __ positive a.. res_bit __ 1:
                res += 1 << i
            # If single number is negative
            __ n.. positive a.. res_bit __ 0:
                res += 1 << i
        __ n.. positive:
            res -(res + 1)
        r.. res
