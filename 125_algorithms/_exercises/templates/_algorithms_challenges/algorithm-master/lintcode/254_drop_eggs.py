"""
REF: http://blog.csdn.net/shaya118/article/details/40823225

Main Concept:

assuming the minimum times to drop is `x`
according to REF, the relation of `x` is below

         |
         | x
    |....|
. | |....|
   x + 1

0 + 1 + 2 + ... + x
=> x(x + 1) / 2 >= n
"""


"""
cumulative the sum of the triangle
"""
c_ Solution:
    """
    @param: n: An integer
    @return: The sum of a and b
    """
    ___ dropEggs  n
        __ n <= 0:
            r.. 0

        _sum = 0
        ___ i __ r..(n
            _sum += i
            __ _sum >= n:
                r.. i

        r.. n


"""
optimized: cumulative the sum of the triangle

x(x + 1) / 2 >= n
=> sqrt(x(x + 1)) >= sqrt(2n)
=> sqrt(x(x + 1)) >= sqrt(x^2) == x >= sqrt(2n)

so `x` can start from `sqrt(2n)`
"""
____ m__ _______ sqrt


c_ Solution:
    """
    @param: n: An integer
    @return: The sum of a and b
    """
    ___ dropEggs  n
        __ n <= 0:
            r.. 0

        x = i..(sqrt(2 * n))
        w.... x * (x + 1) // 2 < n:
            x += 1

        r.. x
