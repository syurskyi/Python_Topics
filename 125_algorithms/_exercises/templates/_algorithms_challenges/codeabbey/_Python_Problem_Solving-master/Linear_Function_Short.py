N = int(raw_input())
___ n __ r..(N):
    x1, y1, x2, y2 = map(int, raw_input().split())
    a = (y1-y2)/(x1-x2)
    b = y1-x1*(y1-y2)/(x1-x2)
    print '(' + str(a) + ' ' + str(b) + ')',