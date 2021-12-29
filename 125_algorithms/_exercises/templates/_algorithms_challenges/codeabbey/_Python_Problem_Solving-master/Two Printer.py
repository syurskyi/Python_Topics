___ i __ r..(int(input())):
    x,y,n = l..(map(float, input().s..()))
    x_1 = int(y*n / (x+y))
    y_1 = int(x*n/ (x+y))
    n = n - (x_1 + y_1)
    x_ans = int(max( (x_1 + n)* x, y_1 * y))
    y_ans = int(max( x_1 * x, (y_1 + n) * y))
    
    print(m..(x_ans,y_ans),end=' ')