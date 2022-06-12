c_ Solution o..
    ___ - ____:
        base = 1337

    ___ superPow  a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # One knowledge: ab % k = (a%k)(b%k)%k
        # a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
        __ b is N.. or l.. b) __ 0:
            r_ 1
        last_digit = b.pop()
        r_ powmod(superPow(a, b), 10) * \
            powmod(a, last_digit) % base

    ___ powmod  a, k):
        a %= base
        result = 1
        ___ i __ r.. k):
            result = (result * a) % base
        r_ result
