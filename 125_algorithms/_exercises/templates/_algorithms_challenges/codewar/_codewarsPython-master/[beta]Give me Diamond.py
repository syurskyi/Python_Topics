___ diamond(n):
    __ n % 2 __ 0 o. n < 1:
        r.. N..
    layers = [(' ' * ((n-i)//2) + '*' * i) ___ i __ r..(1,n,2)]
    upper = '\n'.j..(layers) + '\n'
    center = '*' * n + '\n'
    lower = '\n'.j..(r..(layers)) + '\n'
    r.. upper + center + lower

print(diamond(3))    