class Solution:
    """
    @param: n: An integer
    @return: True or false
    """
    ___ checkPowerOf2(self, n):
        __ not n or n <= 0:
            return False

        return n & (n - 1) == 0
