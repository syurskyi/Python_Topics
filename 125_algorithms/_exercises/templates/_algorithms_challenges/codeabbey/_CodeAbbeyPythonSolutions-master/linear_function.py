amount_values = i..(input())
results    # list

___ get_slope_intercept(x1, y1, x2, y2
    slope = i..((y2-y1)/(x2-x1))
    intercept = (slope*x1-y1)*-1
    r.. "("+s..(slope)+" "+s..(intercept)+")"

___ i __ r..(amount_values
    x1,y1,x2,y2 = map(i.., input().s..())
    results.a..(get_slope_intercept(x1,y1,x2,y2))

print(*results)