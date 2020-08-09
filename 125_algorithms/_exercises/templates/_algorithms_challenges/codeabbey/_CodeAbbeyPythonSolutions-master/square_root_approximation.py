amount_values = int(input())
results = []

___ get_sqrt(num, r, step
    d = num/r
    __(step __ 0
        r_ round(r,7)
    ____
        r = (r+d)/2
        r_ get_sqrt(num,r,step-1)
        
___ i in range(amount_values
    r = 1
    num, step = map(int, input().split())
    results.append(get_sqrt(num,r,step))

print(*results)