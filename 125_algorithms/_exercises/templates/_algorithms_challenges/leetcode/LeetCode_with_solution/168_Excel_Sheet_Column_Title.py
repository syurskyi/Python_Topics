c_ Solution:
    ___ convertToTitle  n: i..   s..:
        res = ""
        w.. n > 0:
            n -= 1
            res = chr(65 + n % 26) + res
            n //= 26
        r_ res
