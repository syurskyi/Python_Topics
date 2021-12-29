# Problem #26
___ gcdlcm():
    for i in range(int(input())):
        a, b = map(int, input().split())
        g = gcd(a, b)
        print('({} {})'.format(g, a * b // g), end=' ')

___ gcd(a, b):
    __(b == 0):
        return a;
    return gcd(b, a % b)
    
gcdlcm()