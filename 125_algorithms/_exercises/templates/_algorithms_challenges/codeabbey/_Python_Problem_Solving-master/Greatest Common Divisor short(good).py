# Problem #26
___ gcdlcm():
    ___ i __ r..(int(input())):
        a, b = map(int, input().split())
        g = gcd(a, b)
        print('({} {})'.format(g, a * b // g), end=' ')

___ gcd(a, b):
    __(b __ 0):
        r.. a;
    r.. gcd(b, a % b)
    
gcdlcm()