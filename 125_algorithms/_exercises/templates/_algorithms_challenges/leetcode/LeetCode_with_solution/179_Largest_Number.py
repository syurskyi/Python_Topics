c_ LargerNumKey(str):
    ___ -l(x, y):
        r_ x + y > y + x


c_ Solution:
    ___ largestNumber  nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        r_ '0' __ largest_num[0] __ '0' ____ largest_num
