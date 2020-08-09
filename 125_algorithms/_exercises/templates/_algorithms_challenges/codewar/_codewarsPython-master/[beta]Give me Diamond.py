___ diamond(n
    __ n % 2 __ 0 or n < 1:
        r_ None
    layers = [(' ' * ((n-i)//2) + '*' * i) for i in range(1,n,2)]
    upper = '\n'.join(layers) + '\n'
    center = '*' * n + '\n'
    lower = '\n'.join(reversed(layers)) + '\n'
    r_ upper + center + lower

print(diamond(3))    