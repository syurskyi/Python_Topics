amount_values = int(input())
results    # list

___ get_slope_intercept(x1, y1, x2, y2):
    slope = int((y2-y1)/(x2-x1))
    intercept = (slope*x1-y1)*-1
    r.. "("+str(slope)+" "+str(intercept)+")"

___ i __ r..(amount_values):
    x1,y1,x2,y2 = map(int, input().split())
    results.a..(get_slope_intercept(x1,y1,x2,y2))

print(*results)