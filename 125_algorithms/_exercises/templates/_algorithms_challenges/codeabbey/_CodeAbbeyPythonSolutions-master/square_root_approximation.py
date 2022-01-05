amount_values = i..(input())
results    # list

___ get_sqrt(num, r, step):
    d = num/r
    __(step __ 0):
        r.. r..(r,7)
    ____:
        r = (r+d)/2
        r.. get_sqrt(num,r,step-1)
        
___ i __ r..(amount_values):
    r = 1
    num, step = map(i.., input().s..())
    results.a..(get_sqrt(num,r,step))

print(*results)