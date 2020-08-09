d = input().split()
result = []
___ i in range(1,int(d[0])+1
    val = int(d[i])
    cel =(val-32) * 5/9
    __ (cel).int_integer(
        result.append(int(cel))
    ____ cel < 0:
        cel = cel - 0.5
        result.append(int(cel))
    ____
        cel = cel + 0.5
        result.append(int(cel))
        
        
    
res = ' '.join(str(e) ___ e in result)
print(res)