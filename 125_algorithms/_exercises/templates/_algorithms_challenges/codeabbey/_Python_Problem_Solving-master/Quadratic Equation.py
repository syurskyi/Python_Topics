_______ math
data = i..(input())
___ i __ r..(data
    cal = 0
    deno = 0
    res = ''
    a,b,c = nums = l.. m..(i..,input().s..()))
    cal = b**2 - (4*a*c)
    deno = 2*a
    __ cal >= 0:
        x1 = (-b + math.sqrt(cal)) / deno
        x2 = (-b - math.sqrt(cal)) / deno
        res = s..(i..(x1))+' '+s..(i..(x2))
    ____:
        cal = cal * -1
        x_cal = s..(i..(math.sqrt(cal) / deno)) + 'i'
        b_cal = -b /deno
        x1 = s..(i..(b_cal)) +'+'+ x_cal
        x2 = s..(i..(b_cal)) +'-'+ x_cal
        res = x1 + ' '+ x2
    __ i __ data-1:
        print(res,end = '')
    ____:
        print(res,end = '; ')