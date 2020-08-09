d = input().split()
d.sort()
res = []
d_dic = {}
___ i in d:
    __ i in d_dic:
        d_dic[i] += 1
    ____
        d_dic[i] = 1
___ i in d_dic:
    __ d_dic[i] > 1:
        __ i not in res:
            res.append(i)
___ i in res:
    print(i,end=' ')