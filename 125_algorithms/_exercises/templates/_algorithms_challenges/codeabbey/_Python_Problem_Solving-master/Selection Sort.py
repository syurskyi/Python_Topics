d = int(input())
a = l..(map(int,input().split()))

while l..(a)!= 1:
    max = 0
    ___ i __ r..(l..(a)):
        __ a[i] > max:
            max = a[i]
    ind = a.index(max)
    print(ind,end=' ')
    a[ind],a[-1] = a[-1],a[ind]
    a.pop(-1)