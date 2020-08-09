d = input().split()
d.sort()
res = []
d_dic = {}
for i in d:
    __ i in d_dic:
        d_dic[i] += 1
    ____
        d_dic[i] = 1
for i in d_dic:
    __ d_dic[i] > 1:
        __ i not in res:
            res.append(i)
for i in res:
    print(i,end=' ')