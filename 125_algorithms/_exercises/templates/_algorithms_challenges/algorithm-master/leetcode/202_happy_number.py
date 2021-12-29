class Solution:
    ___ isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.square_sum(n)
        fast = self.square_sum(slow)

        w.... slow != fast:
            slow = self.square_sum(slow)
            fast = self.square_sum(
                self.square_sum(fast)
            )

        r.. True __ slow __ 1 ____ False

    ___ square_sum(self, a):
        res = b = 0

        w.... a != 0:
            b = a % 10
            res += b * b
            a //= 10

        r.. res
