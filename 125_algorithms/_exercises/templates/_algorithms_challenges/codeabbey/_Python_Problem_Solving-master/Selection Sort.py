d = int(input())
a = list(map(int,input().split()))

w___ le.(a)!= 1:
    max = 0
    ___ i in range(le.(a)):
        __ a[i] > max:
            max = a[i]
    ind = a.index(max)
    print(ind,end=' ')
    a[ind],a[-1] = a[-1],a[ind]
    a.pop(-1)