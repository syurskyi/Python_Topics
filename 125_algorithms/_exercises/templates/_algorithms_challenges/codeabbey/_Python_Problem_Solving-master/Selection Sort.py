d = int(input())
a = list(map(int,input().split()))

w___ le.(a)!= 1:
    ma. = 0
    ___ i __ range(le.(a)):
        __ a[i] > ma.:
            ma. = a[i]
    ind = a.index(ma.)
    print(ind,end=' ')
    a[ind],a[-1] = a[-1],a[ind]
    a.pop(-1)