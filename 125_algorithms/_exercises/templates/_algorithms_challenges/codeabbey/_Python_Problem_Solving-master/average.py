data = i..(input())
result    # list

___ i __ r..(data):
    sum_numbs = 0
    avg = 0
    avg_numbs = input().s..
    
    ___ j __ r..(l..(avg_numbs)-1):
        #print('value of avg ',j,' is ',avg_numbs[j])
        sum_numbs = sum_numbs + i..(avg_numbs[j])
        #a = [int(x) for x in input().split()]
        #avg = sum(a) / (len(a) - 1)
        
    avg = sum_numbs / (l..(avg_numbs)-1)
    __ avg.is_integer
        result.a..(i..(avg))
    ____:
        avg = avg + 0.5
        result.a..(i..(avg))
        
___ k __ result:
    print(k,end=(' '))