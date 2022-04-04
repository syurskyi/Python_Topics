a =  [i..(i) ___ i __ input().s.. ]
a.remove(a[-1])
swap_count = 0
seed = 0

___ i __ r..(l..(a:
    __ i __ l..(a)-1:
        _____
    __ a[i] > a[i+1]:
        swap_count += 1
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
    ____
        _____

#seed = seed - 4513010
___ j __ r..(l..(a:
    #print('index',j,'value is',a[j])
    seed = (seed + a[j]) * 113
    
    __ seed > 10000007:
        seed = seed % 10000007
        
print(swap_count, seed)