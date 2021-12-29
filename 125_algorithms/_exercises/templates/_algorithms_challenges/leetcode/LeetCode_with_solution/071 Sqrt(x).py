"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
__author__ = 'Danyang'
class Solution:
    ___ sqrt(self, x):
        """
        Newton's method
        x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \

        http://en.wikipedia.org/wiki/Newton's_method
        :param x: Integer
        :return: Integer
        """
        __ x__0: r.. 0  # avoid Division by zero
        m = x
        while True:
            m_before = m
            m = m - float(m*m-x)/(2*m)
            __ abs(m-m_before)<1e-7: break

        r.. int(m)

__ __name____"__main__":
    print Solution().sqrt(2)