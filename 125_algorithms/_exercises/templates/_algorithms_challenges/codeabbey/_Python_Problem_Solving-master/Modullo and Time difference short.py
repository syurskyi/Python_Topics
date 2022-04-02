n = i..(input())
___ i __ r..(n
    d1, h1, m1, s1, d2, h2, m2, s2 = input().s.. 
    d = (i..(d2)-i..(d1)) * 24 * 60 * 60
    h = (i..(h2)-i..(h1)) * 60 * 60
    m = (i..(m2)-i..(m1)) * 60
    s = i..(s2)-i..(s1)
    zman = d + h + m + s
   
    d = zman // (24*60*60)
    zman -= d*24*60*60
    h = zman // 3600
    zman -=  h*3600
    m = zman // 60
    s = zman - 60*m
    print('({} {} {} {})'.f..(d, h, m, s), end = ' ')