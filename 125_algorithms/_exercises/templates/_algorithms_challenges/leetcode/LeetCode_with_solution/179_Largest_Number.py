c_ LargerNumKey(s..):
    ___ -l(x, y):
        r_ x + y > y + x


c_ Solution:
    ___ largestNumber  nums):
        largest_num = ''.join(sorted(map(s.., nums), key=LargerNumKey))
        r_ '0' __ largest_num[0] __ '0' ____ largest_num
