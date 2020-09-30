# Single Number II
# Question: Given an array of integers, every element appears three times except for one. Find that single one.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Solutions:


class Solution:
    # @param A, a list of integer
    # @return an integer
    ___ singleNumber(self, A):
        bit = [0 ___ i __ range(32)]
        ___ number __ A:
            ___ i __ range(32):
                if (1 << i) & number == 1 << i:
                    bit[i] += 1
        res = 0
        if bit[31] % 3 == 0:
            ___ i __ range(31):
                if bit[i] % 3 == 1:
                    res += 1 << i
        else:
            ___ i __ range(31):
                if bit[i] % 3 == 0: res += 1 << i
            res = -(res + 1)
        r_ res


Solution().singleNumber([1, 2, 1, 2, 1, 2, 0, 0])