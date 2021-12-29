_______ math
data = int(input())
___ i __ r..(data):
    cal = 0
    deno = 0
    res = ''
    a,b,c = nums = l..(map(int,input().split()))
    cal = b**2 - (4*a*c)
    deno = 2*a
    __ cal >= 0:
        x1 = (-b + math.sqrt(cal)) / deno
        x2 = (-b - math.sqrt(cal)) / deno
        res = str(int(x1))+' '+str(int(x2))
    ____:
        cal = cal * -1
        x_cal = str(int(math.sqrt(cal) / deno)) + 'i'
        b_cal = -b /deno
        x1 = str(int(b_cal)) +'+'+ x_cal
        x2 = str(int(b_cal)) +'-'+ x_cal
        res = x1 + ' '+ x2
    __ i __ data-1:
        print(res,end = '')
    ____:
        print(res,end = '; ')