class Solution:
    # @param A, a list of integer
    # @return an integer
    ___ singleNumber(self, A
        # Assume 32-bit integer
        num_of_bits = 32  # Change this to 64 on 64-bit platform
        res_bit = 0
        res = 0
        # First check whether the single number is negative
        for num in A:
            bit = 1 __ num & (1 << (num_of_bits - 1)) != 0 else 0
            res_bit = (res_bit + bit) % 3
        positive = True __ res_bit __ 0 else False

        for i in range(num_of_bits - 1
            res_bit = 0
            # For each bit of each number, calculate each bit
            # of the single number
            for num in A:
                bit = 1 __ num & (1 << i) != 0 else 0
                res_bit = (res_bit + bit) % 3
            # If single number is positive
            __ positive and res_bit __ 1:
                res += 1 << i
            # If single number is negative
            __ not positive and res_bit __ 0:
                res += 1 << i
        __ not positive:
            res = -(res + 1)
        r_ res
